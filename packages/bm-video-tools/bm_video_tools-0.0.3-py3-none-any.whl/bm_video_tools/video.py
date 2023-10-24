from __future__ import annotations
import asyncio
import functools
import math
import os
import tempfile
import cv2
from typing import List
from moviepy.editor import VideoFileClip, concatenate_videoclips

from .media import Media
from .image import Image
from .audio import Audio
from .operate import Operate
from .utils import backslash2slash, pre_operate, subprocess_exec
from .remover.transparent_video import transparent


class Video(Media):
    async def run(self, op: Operate, output_path: str) -> Video:
        """
        执行操作
        :param op: Operation实例对象
        :param output_path: 输出路径
        :return: 媒体对象
        """
        output_path = backslash2slash(output_path)

        cmd = op.exec()
        await subprocess_exec(cmd, self.input_path, output_path)

        return self.__class__(output_path)

    @pre_operate(suffix='.mp4')
    async def screenshot(self, output_path: str, **kwargs) -> Image:
        """
        视频截图
        :param output_path: 输出图片存放路径
        :return: 图片对象
        """
        output_path = backslash2slash(output_path)
        temp_media: Video = kwargs.get("temp_media")
        input_path = temp_media.input_path if temp_media else self.input_path

        cmd = r'ffmpeg -i {} -ss 0 -frames:v 1 -y -v error {}'
        await subprocess_exec(cmd, input_path, output_path)

        return Image(output_path)

    @pre_operate(suffix='.mp4')
    async def remove(self, output_path: str,
                     model_name: str = 'u2net_human_seg',
                     worker_nodes: int = 2, gpu_batch_size: int = 2,
                     frame_limit: int = -1, frame_rate: int = -1, **kwargs) -> Video:
        """
        人像抠图
        :param output_path: 输出路径
        :param model_name: 模型名称
        :param worker_nodes: 工作进程数
        :param gpu_batch_size: GPU批量大小
        :param frame_limit: 总帧数
        :param frame_rate: 帧率
        :return: 视频对象
        """
        output_path = backslash2slash(output_path)
        temp_media: Video = kwargs.get("temp_media")

        if temp_media:
            input_path = temp_media.input_path
            video_info = await temp_media.get_info()
        else:
            input_path = self.input_path
            video_info = await self.get_info()

        total_frames = int(video_info["streams"][0]["nb_frames"])
        if frame_limit != -1:
            total_frames = min(frame_limit, total_frames)

        fr = video_info["streams"][0]["r_frame_rate"]
        if frame_rate == -1:
            print(F"FRAME RATE DETECTED: {fr} (if this looks wrong, override the frame rate)")
            frame_rate = math.ceil(eval(fr))

        print(F"FRAME RATE: {frame_rate} TOTAL FRAMES: {total_frames}")

        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, functools.partial(transparent, input_path, output_path, model_name, worker_nodes, gpu_batch_size, total_frames, frame_rate))

        return self.__class__(output_path)

    @pre_operate(suffix='.mp4')
    async def face_detection(self, model_name: str = 'haarcascade_frontalface_alt2', proportion: float = 0.9, **kwargs) -> bool:
        """
        视频逐帧检测人脸
        :param model_name: 人脸检测模型
        :param proportion: 人脸出现占比（0~1）
        :return 视频中人脸占比是否超过指定值
        """
        temp_media: Video = kwargs.get("temp_media")
        input_path = temp_media.input_path if temp_media else self.input_path

        model_path = os.path.expanduser(os.path.join("~", ".bm-video-tools", model_name + ".xml"))
        if not os.path.exists(model_path):
            raise ValueError(f'{model_path} does not exist')

        def detection():
            video = cv2.VideoCapture(input_path)
            if not video.isOpened():
                raise RuntimeError("the video can not opened, please check the path")

            print("Starting detection")
            # 定义计数器
            total_frames = 0
            total_faces = 0

            face_detector = cv2.CascadeClassifier(model_path)

            while True:
                ret, image = video.read()  # 逐帧读取视频流(ret 是否读取到帧，image 是读取的帧内容)
                if not ret:
                    break

                total_frames += 1
                faces = face_detector.detectMultiScale(image)
                if len(faces) > 0:
                    total_faces += 1

            video.release()
            prop = float(total_faces) / total_frames
            print(f'detection finished：{total_frames=}, {total_faces=}, {prop=}')
            return float(total_faces / total_frames)

        loop = asyncio.get_event_loop()
        _proportion = await loop.run_in_executor(None, detection)

        return _proportion >= proportion

    @staticmethod
    async def concat(output_path: str, video_list: list) -> Video:
        """
        视频拼接
        :param output_path: 输出视频路径
        :param video_list: 视频列表
        :return: 视频对象
        """
        output_path = backslash2slash(output_path)

        clips = []
        temp_path_list = []
        try:
            for item in video_list:
                media = item["media"]
                if not isinstance(media, Video):
                    raise ValueError("only can concat video files")

                if "op" in item and isinstance(item.get("op"), Operate):
                    op = item.get("op")
                    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.ts')
                    temp_file_path = backslash2slash(temp_file.name)
                    temp_file.close()
                    temp_media = await media.run(op, temp_file_path)
                    clips.append(VideoFileClip(temp_media.input_path))
                    temp_path_list.append(temp_media.input_path)
                else:
                    clips.append(VideoFileClip(media.input_path))

            def _content():
                final_clip = concatenate_videoclips(clips)
                final_clip.write_videofile(output_path)

            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, _content)

            return Video(output_path)
        finally:
            for temp_path in temp_path_list:
                if os.path.exists(temp_path):
                    os.remove(temp_path)

    @staticmethod
    async def composite(output_path: str, media_list: List[Video, Image], audio_list: List[Audio], canvas: tuple = None):
        pass
