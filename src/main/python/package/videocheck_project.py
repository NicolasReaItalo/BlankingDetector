import cv2
import subprocess as sp
import numpy

from package import timecode

from ffprobe import FFProbe

import os

class VideoCheck():

    def __init__(self):
         self.video_path = ''
         self.report_path = ''
         self.issue_list = []
         self.crop_top = 0
         self.crop_bottom = 0
         self.crop_left = 0
         self.crop_right = 0
         self.duration = 0
         self.framerate = 0
         self.codec = ''
         self.x_res = 0
         self.y_res = 0

    def get_resolution(self):
        if os.path.exists(self.video_path):
            metadata = FFProbe(self.video_path)
            return metadata.streams[0].frame_size()
        return False

    def get_framerate(self):
        if os.path.exists(self.video_path):
            metadata = FFProbe(self.video_path)
            return metadata.streams[0].__dict__.get('framerate')
        return False

    def get_duration_frames(self):
        if os.path.exists(self.video_path):
            metadata = FFProbe(self.video_path)
            return metadata.streams[0].frames()
        return False


    def get_codec(path):
        metadata = FFProbe(path)
        return metadata.streams[0].codec_description()

    def get_duration(path):
        metadata = FFProbe(path)
        return float(metadata.streams[0].__dict__.get('duration'))





