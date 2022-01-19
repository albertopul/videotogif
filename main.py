import sys
import os
import glob
import cv2
from PIL import Image

class Gif:

    TEMP_DIR = 'tmp/'

    def __init__(self, path: str):
        self.movie = cv2.VideoCapture(path)

    def read_frame(self, time: int):
        self.movie.set(cv2.CAP_PROP_POS_MSEC, time)
        return self.movie.read()

    def _get_frames(self, fps):
        time = 1
        success, frame = self.read_frame(time)

        while success:
            cv2.imwrite(f'{Gif.TEMP_DIR}{time}.jpg', frame)
            success, frame = self.read_frame(round(time/fps * 1000))
            time += 1

    def save(self, target: str, fps):
        self._get_frames(fps)
        images = glob.glob(f'{Gif.TEMP_DIR}*.jpg')
        frames = [Image.open(image) for image in images]
        frames[0].save(
            target,
            format='GIF',
            append_images=frames,
            save_all=True,
            duration=200,
            loop=3
            )
            




gif = Gif(input("Enter the path of your file: "))
print("Processing...")
gif.save('dog.gif', 3)
print("Done! You have your gif!")