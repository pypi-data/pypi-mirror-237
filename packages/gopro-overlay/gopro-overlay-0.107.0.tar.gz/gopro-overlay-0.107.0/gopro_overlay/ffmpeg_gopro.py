from __future__ import annotations

import datetime
import itertools
import json
import os
import pathlib
import subprocess
from array import array
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from gopro_overlay.common import temporary_file
from gopro_overlay.dimensions import Dimension
from gopro_overlay.ffmpeg import FFMPEG
from gopro_overlay.timeunits import timeunits, Timeunit


class FFMPEGGoPro:

    def __init__(self, exe: FFMPEG):
        self.exe = exe

    def join_files(self, filepaths, output):
        """only for joining parts of same trip"""

        streams = self.find_recording(filepaths[0])

        maps = list(itertools.chain.from_iterable(
            [["-map", f"0:{it.stream}"] for it in [streams.video, streams.audio, streams.meta] if it is not None]))

        with temporary_file() as commandfile:
            with open(commandfile, "w") as f:
                for path in filepaths:
                    f.write(f"file '{path}\n")

            self.exe.run(
                ["-hide_banner",
                 "-y",
                 "-f", "concat",
                 "-safe", "0",
                 "-i", commandfile,
                 "-map_metadata", "0",
                 *maps,
                 "-copy_unknown",
                 "-c", "copy",
                 output]
            )

    def find_frame_duration(self, filepath, data_stream_number):
        ffprobe_output = str(self.exe.ffprobe().invoke(
            ["-hide_banner",
             "-print_format", "json",
             "-show_packets",
             "-select_streams", str(data_stream_number),
             "-read_intervals", "%+#1",
             filepath]
        ).stdout)

        ffprobe_packet_data = json.loads(ffprobe_output)
        packet = ffprobe_packet_data["packets"][0]

        duration = int(packet["duration"])

        return duration

    def find_recording(self, filepath: Path, stat=os.stat) -> GoproRecording:
        ffprobe_output = str(self.exe.ffprobe().invoke(
            [
                "-hide_banner",
                "-print_format", "json",
                "-show_streams",
                filepath
            ]
        ).stdout)

        ffprobe_json = json.loads(ffprobe_output)

        video_selector = lambda s: s["codec_type"] == "video"
        audio_selector = lambda s: s["codec_type"] == "audio"
        data_selector = lambda s: s["codec_type"] == "data" and s["codec_tag_string"] == "gpmd"

        def first_and_only(what, l, p):
            matches = list(filter(p, l))
            if not matches:
                raise IOError(f"Unable to find {what} in ffprobe output")
            if len(matches) > 1:
                raise IOError(f"Multiple matching streams for {what} in ffprobe output")
            return matches[0]

        def only_if_present(what, l, p):
            matches = list(filter(p, l))
            if matches:
                return first_and_only(what, l, p)

        streams = ffprobe_json["streams"]
        video = first_and_only("video stream", streams, video_selector)

        video_meta = VideoMeta(
            stream=int(video["index"]),
            dimension=Dimension(video["width"], video["height"]),
            duration=timeunits(seconds=float(video["duration"]))
        )

        audio = only_if_present("audio stream", streams, audio_selector)
        audio_meta = None
        if audio:
            audio_meta = AudioMeta(stream=int(audio["index"]))

        meta = only_if_present("metadata stream", streams, data_selector)

        if meta:
            data_stream_number = int(meta["index"])

            meta_meta = MetaMeta(
                stream=data_stream_number,
                frame_count=int(meta["nb_frames"]),
                timebase=int(meta["time_base"].split("/")[1]),
                frame_duration=self.find_frame_duration(filepath, data_stream_number)
            )
        else:
            meta_meta = None

        return GoproRecording(
            ffmpeg=self.exe,
            location=filepath,
            file=file_meta(filepath, stat=stat),
            audio=audio_meta,
            video=video_meta,
            meta=meta_meta
        )

    def load_frame(self, filepath: Path, at_time: Timeunit) -> Optional[bytes]:
        if filepath.exists():
            cmd = ["-hide_banner",
                   "-y",
                   "-ss", str(at_time.millis() / 1000),
                   "-i", str(filepath.absolute()),
                   "-frames:v", "1",
                   "-f", "rawvideo",
                   "-pix_fmt", "rgba",
                   "-"
                   ]
            try:
                return self.exe.run(cmd, capture_output=True).stdout
            except subprocess.CalledProcessError as e:
                raise IOError(f"Error: {cmd}\n stderr: {e.stderr}")

    def cut_file(self, input: pathlib.Path, output, start, duration):
        streams = self.find_recording(input)

        maps = list(itertools.chain.from_iterable(
            [["-map", f"0:{it.stream}"] for it in [streams.video, streams.audio, streams.meta] if it is not None]))

        args = [
            "-hide_banner",
            "-y",
            "-i", input,
            "-map_metadata", "0",
            *maps,
            "-copy_unknown",
            "-ss", str(start),
            "-t", str(duration),
            "-c", "copy",
            output
        ]

        self.exe.run(args)


@dataclass(frozen=True)
class FileMeta:
    length: int
    mtime: datetime.datetime
    ctime: datetime.datetime
    atime: datetime.datetime


def file_meta(filepath: Path, stat=os.stat) -> FileMeta:
    sr = stat(filepath)

    return FileMeta(
        length=sr.st_size,
        ctime=datetime.datetime.fromtimestamp(sr.st_ctime, tz=datetime.timezone.utc),
        atime=datetime.datetime.fromtimestamp(sr.st_atime, tz=datetime.timezone.utc),
        mtime=datetime.datetime.fromtimestamp(sr.st_mtime, tz=datetime.timezone.utc)
    )


@dataclass(frozen=True)
class GoproRecording:
    ffmpeg: FFMPEG
    location: Path
    file: FileMeta
    audio: Optional[AudioMeta]
    video: VideoMeta
    meta: Optional[MetaMeta]

    def load_gpmd(self) -> array:
        track = self.meta.stream
        if track:
            cmd = [
                "-hide_banner",
                '-y',
                '-i', self.location,
                '-codec', 'copy',
                '-map', '0:%d' % track,
                '-f', 'rawvideo',
                "-"
            ]
            result = self.ffmpeg.run(cmd, capture_output=True, timeout=10)
            if result.returncode != 0:
                raise IOError(f"ffmpeg failed code: {result.returncode} : {result.stderr.decode('utf-8')}")
            arr = array("b")
            arr.frombytes(result.stdout)
            return arr


@dataclass(frozen=True)
class MetaMeta:
    stream: int
    frame_count: int
    timebase: int
    frame_duration: int


@dataclass(frozen=True)
class VideoMeta:
    stream: int
    dimension: Dimension
    duration: Timeunit


@dataclass(frozen=True)
class AudioMeta:
    stream: int
