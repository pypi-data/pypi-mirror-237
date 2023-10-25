from __future__ import annotations

import os.path
import subprocess
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from re import search
from subprocess import PIPE, Popen
from typing import Any, Literal, overload

from auto_editor.lang.json import Lexer, Parser
from auto_editor.lib.err import MyError
from auto_editor.utils.func import get_stdout
from auto_editor.utils.log import Log

IMG_CODECS = ("png", "mjpeg", "webp")
SUB_EXTS = {"mov_text": "srt", "ass": "ass", "webvtt": "vtt"}


class FFmpeg:
    __slots__ = ("debug", "show_cmd", "path", "version")

    def __init__(
        self,
        ff_location: str | None = None,
        my_ffmpeg: bool = False,
        show_cmd: bool = False,
        debug: bool = False,
    ):
        def _set_ff_path(ff_location: str | None, my_ffmpeg: bool) -> str:
            if ff_location is not None:
                return ff_location
            if my_ffmpeg:
                return "ffmpeg"

            try:
                import ae_ffmpeg

                return ae_ffmpeg.get_path()
            except ImportError:
                return "ffmpeg"

        self.debug = debug
        self.show_cmd = show_cmd
        self.path = _set_ff_path(ff_location, my_ffmpeg)
        try:
            _version = get_stdout([self.path, "-version"]).split("\n")[0]
            self.version = _version.replace("ffmpeg version", "").strip().split(" ")[0]
        except FileNotFoundError:
            if sys.platform == "darwin":
                Log().error(
                    "No ffmpeg found, download via homebrew or install ae-ffmpeg."
                )
            if sys.platform == "win32":
                Log().error(
                    "No ffmpeg found, download ffmpeg with your favorite package "
                    "manager (ex chocolatey), or install ae-ffmpeg."
                )

            Log().error("ffmpeg must be installed and on PATH.")

    def print(self, message: str) -> None:
        if self.debug:
            sys.stderr.write(f"FFmpeg: {message}\n")

    def print_cmd(self, cmd: list[str]) -> None:
        if self.show_cmd:
            sys.stderr.write(f"{' '.join(cmd)}\n\n")

    def run(self, cmd: list[str]) -> None:
        cmd = [self.path, "-hide_banner", "-y"] + cmd
        if not self.debug:
            cmd.extend(["-nostats", "-loglevel", "error"])
        self.print_cmd(cmd)
        subprocess.run(cmd)

    def run_check_errors(
        self,
        cmd: list[str],
        log: Log,
        show_out: bool = False,
        path: str | None = None,
    ) -> None:
        process = self.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        _, stderr = process.communicate()

        if process.stdin is not None:
            process.stdin.close()
        output = stderr.decode("utf-8", "replace")

        error_list = [
            r"Unknown encoder '.*'",
            r"-q:v qscale not available for encoder\. Use -b:v bitrate instead\.",
            r"Specified sample rate .* is not supported",
            r'Unable to parse option value ".*"',
            r"Error setting option .* to value .*\.",
            r"Undefined constant or missing '.*' in '.*'",
            r"DLL .* failed to open",
            r"Incompatible pixel format '.*' for codec '[A-Za-z0-9_]*'",
            r"Unrecognized option '.*'",
            r"Permission denied",
        ]

        if self.debug:
            print(f"stderr: {output}")

        for item in error_list:
            if check := search(item, output):
                log.error(check.group())

        if path is not None and not os.path.isfile(path):
            log.error(f"The file {path} was not created.")
        elif show_out and not self.debug:
            print(f"stderr: {output}")

    def Popen(
        self, cmd: list[str], stdin: Any = None, stdout: Any = PIPE, stderr: Any = None
    ) -> Popen:
        cmd = [self.path] + cmd
        self.print_cmd(cmd)
        return Popen(cmd, stdin=stdin, stdout=stdout, stderr=stderr)

    def pipe(self, cmd: list[str]) -> str:
        cmd = [self.path, "-y"] + cmd

        self.print_cmd(cmd)
        output = get_stdout(cmd)
        self.print(output)
        return output


@dataclass(slots=True)
class VideoStream:
    width: int
    height: int
    codec: str
    fps: Fraction
    duration: str | None
    sar: str | None
    time_base: Fraction
    pix_fmt: str
    color_range: str | None
    color_space: str | None
    color_primaries: str | None
    color_transfer: str | None
    bitrate: str | None
    lang: str | None


@dataclass(slots=True)
class AudioStream:
    codec: str
    samplerate: int
    channels: int
    duration: str | None
    bitrate: str | None
    lang: str | None


@dataclass(slots=True)
class SubtitleStream:
    codec: str
    ext: str
    lang: str | None


class FileInfo:
    __slots__ = (
        "path",
        "bitrate",
        "duration",
        "description",
        "videos",
        "audios",
        "subtitles",
        "label",
    )

    def get_res(self) -> tuple[int, int]:
        if self.videos:
            return self.videos[0].width, self.videos[0].height
        return 1920, 1080

    def get_fps(self) -> Fraction:
        if self.videos:
            return self.videos[0].fps
        return Fraction(30)

    def get_sr(self) -> int:
        if self.audios:
            return self.audios[0].samplerate
        return 48000

    def __init__(self, path: str, ffmpeg: FFmpeg, log: Log, label: str = ""):
        self.label = label
        self.path = Path(path)
        self.videos: list[VideoStream] = []
        self.audios: list[AudioStream] = []
        self.subtitles: list[SubtitleStream] = []
        self.description = None
        self.duration = 0.0

        _dir = os.path.dirname(ffmpeg.path)
        _ext = os.path.splitext(ffmpeg.path)[1]
        ffprobe = os.path.join(_dir, f"ffprobe{_ext}")

        try:
            info = get_stdout(
                [
                    ffprobe,
                    "-v",
                    "-8",
                    "-print_format",
                    "json",
                    "-show_streams",
                    "-show_format",
                    path,
                ]
            )
        except FileNotFoundError:
            log.nofile(ffprobe)
        except Exception as e:
            log.error(e)

        @overload
        def get_attr(name: str, dic: dict[str, str], op: Literal[True]) -> str | None:
            ...

        @overload
        def get_attr(name: str, dic: dict[str, str]) -> str:
            ...

        def get_attr(name: str, dic: dict[str, str], op: bool = False) -> str | None:
            if name in dic:
                if isinstance(dic[name], str):
                    return dic[name]
                log.error(f"'{name}' must be a string")
            if not op:
                log.error(f"'{name}' must be in ffprobe json")
            return None

        try:
            json_info = Parser(Lexer("ffprobe", info)).expr()
            if not isinstance(json_info, dict):
                raise MyError("Expected Object")
            if "streams" not in json_info:
                raise MyError("Key 'streams' not found")
            if "format" not in json_info:
                raise MyError("Key 'format' not found")
        except MyError as e:
            log.error(f"{path}: Could not read ffprobe JSON\n{e}")

        self.bitrate: str | None = None
        if "bit_rate" in json_info["format"]:
            self.bitrate = json_info["format"]["bit_rate"]
        if (
            "tags" in json_info["format"]
            and "description" in json_info["format"]["tags"]
        ):
            self.description = json_info["format"]["tags"]["description"]

        if "duration" in json_info["format"]:
            try:
                self.duration = float(json_info["format"]["duration"])
            except Exception:
                pass

        for stream in json_info["streams"]:
            lang = None
            br = None
            if "tags" in stream and "language" in stream["tags"]:
                lang = stream["tags"]["language"]
            if "bit_rate" in stream:
                br = stream["bit_rate"]

            codec_type = get_attr("codec_type", stream)

            if codec_type in ("video", "audio", "subtitle"):
                codec = get_attr("codec_name", stream)

            if codec_type == "video":
                pix_fmt = get_attr("pix_fmt", stream)
                vduration = get_attr("duration", stream, True)
                color_range = get_attr("color_range", stream, True)
                color_space = get_attr("color_space", stream, True)
                color_primaries = get_attr("color_primaries", stream, True)
                color_transfer = get_attr("color_transfer", stream, True)
                sar = get_attr("sample_aspect_ratio", stream, True)
                fps_str = get_attr("r_frame_rate", stream)
                time_base_str = get_attr("time_base", stream)

                try:
                    fps = Fraction(fps_str)
                except ZeroDivisionError:
                    fps = Fraction(0)
                except ValueError:
                    log.error(f"Could not convert fps '{fps_str}' to Fraction.")

                if fps < 1 and codec in IMG_CODECS:
                    fps = Fraction(25)
                if fps == 0:
                    fps = Fraction(30)

                try:
                    time_base = Fraction(time_base_str)
                except (ValueError, ZeroDivisionError):
                    if codec not in IMG_CODECS:
                        log.error(
                            f"Could not convert time_base '{time_base_str}' to Fraction."
                        )
                    time_base = Fraction(0)

                self.videos.append(
                    VideoStream(
                        stream["width"],
                        stream["height"],
                        codec,
                        fps,
                        vduration,
                        sar,
                        time_base,
                        pix_fmt,
                        color_range,
                        color_space,
                        color_primaries,
                        color_transfer,
                        br,
                        lang,
                    )
                )
            if codec_type == "audio":
                sr = int(stream["sample_rate"])

                if "channels" not in stream:
                    log.error("audio stream has no 'channels' data")
                c = stream["channels"]

                adur = get_attr("duration", stream, True)
                self.audios.append(AudioStream(codec, sr, c, adur, br, lang))
            if codec_type == "subtitle":
                ext = SUB_EXTS.get(codec, "vtt")
                self.subtitles.append(SubtitleStream(codec, ext, lang))
