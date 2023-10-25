import time
import cv2
from multiprocessing import Manager, Process

from .model import load_model


def _producer(input_path, worker_nodes, total_frames, frames_dict):
    video = cv2.VideoCapture(input_path)

    frame_index = 0
    while True:
        if frame_index >= total_frames:
            break
        ret, frame = video.read()
        if not ret:
            break
        frames_dict[frame_index] = frame
        frame_index += 1
        while len(frames_dict) > worker_nodes * 2:
            time.sleep(0.1)
    print(f"Producer finished: {frame_index}")
    video.release()


def _consumer(model_path, worker_nodes, total_frames, frames_dict, faces_dict, consumer_index):
    # 创建人脸检测机器人
    face_detector = cv2.CascadeClassifier(model_path)
    # 分配资源，创建任务批次
    group = [[i + j * worker_nodes for j in range((total_frames - i - 1) // worker_nodes + 1)] for i in range(worker_nodes)]
    print(f'WORKER {consumer_index}: {group[consumer_index]}, LENGTH {len(group[consumer_index])}')

    # 单个进程执行次数
    for idx in group[consumer_index]:
        if idx >= total_frames:
            print(f"Consumer {consumer_index} finished")
            break
        while idx not in frames_dict:
            time.sleep(0.1)
        # 人脸检测
        faces = face_detector.detectMultiScale(frames_dict[idx])
        faces_dict[idx] = len(faces) > 0

        del frames_dict[idx]


def _parallel(input_path: str, model_path: str, total_frames: int, worker_nodes: int) -> int:
    manager = Manager()
    frames_dict = manager.dict()
    faces_dict = manager.dict()

    producer = Process(target=_producer, args=(input_path, worker_nodes, total_frames, frames_dict))
    producer.start()

    consumers = [Process(target=_consumer, args=(model_path, worker_nodes, total_frames, frames_dict, faces_dict, consumer_index)) for consumer_index in range(worker_nodes)]
    for consumer in consumers:
        consumer.start()

    producer.join()
    for consumer in consumers:
        consumer.join()

    return sum(faces_dict.values())


def _non_parallel(input_path: str, model_path: str) -> int:
    video = cv2.VideoCapture(input_path)
    face_detector = cv2.CascadeClassifier(model_path)

    total_faces = 0
    while True:
        ret, image = video.read()  # 逐帧读取视频流(ret 是否读取到帧，image 是读取的帧内容)
        if not ret:
            break

        faces = face_detector.detectMultiScale(image)
        if len(faces) > 0:
            total_faces += 1

    video.release()
    return total_faces


def face_detection(input_path: str, model_name: str, total_frames: int, proportion: float, worker_nodes: int) -> bool:
    video = cv2.VideoCapture(input_path)
    if not video.isOpened():
        raise RuntimeError("the video can not opened, please check the path")
    video.release()

    model_path = load_model(model_name)

    # 判断是否使用多进程
    if not worker_nodes:
        print('face detection start...')
        total_faces = _non_parallel(input_path, model_path)
    else:
        print('face detection parallel start...')
        total_faces = _parallel(input_path, model_path, total_frames, worker_nodes)
    print(f'total frames: {total_frames}, faces scale: {float(total_faces / total_frames)}')

    return float(total_faces / total_frames) >= proportion
