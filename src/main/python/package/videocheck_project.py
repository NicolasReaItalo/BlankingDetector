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
         self.framerate = 0
         self.codec = ''
         self.x_res = 0
         self.y_res = 0
         self.start_frame = 0
         self.end_frame = 0
         self.treshold = 2

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


    def get_codec(self):
        if os.path.exists(self.video_path):
            metadata = FFProbe(self.video_path)
            return metadata.streams[0].codec_description()
        return False




    def is_video(self):

        if os.path.exists(self.video_path):
            metadata = FFProbe(self.video_path)
            if len(metadata.streams) > 0:
                if metadata.streams[0].is_video():
                    return True
        return False


    def analyse_video(self):
        if not self.is_video():
            return "Erreur : ce n'est pas un fichier video"

        current_frame = 0
        command = ["ffmpeg",
                   '-i', self.video_path,  # fifo is the named pipe
                   '-pix_fmt', 'bgr24',  # opencv requires bgr24 pixel format.
                   '-vcodec', 'rawvideo',
                   '-an', '-sn',  # we want to disable audio processing (there is no audio)
                   '-f', 'image2pipe', '-']
        pipe = sp.Popen(command, stdout=sp.PIPE, bufsize=10 ** 8)

        if self.x_res > 1998:
            scale_factor = 6
        else:
            scale_factor = 4



        while True:
            # Capture frame-by-frame
            raw_image = pipe.stdout.read(self.x_res * self.y_res * 3)
            # transform the byte read into a numpy array
            image = numpy.frombuffer(raw_image, dtype='uint8')
            image = image.reshape((self.y_res, self.x_res, 3))  # Notice how height is specified first and then width
            resized = cv2.resize(image, (int(self.x_res / scale_factor), int(self.y_res / scale_factor)), 1, 1)
            cv2.imshow(f'{os.path.basename(self.video_path)}: Analyse en cours... {self.x_res}x{self.y_res}  Appuyer sur q pour arreter',
                       resized)

           ###  INSERER LE CODE DE VERIF ICI


            current_frame += 1



            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if current_frame == self.end_frame:
                break
        pipe.stdout.flush()
        cv2.destroyAllWindows()


    def load_video_file(self, path):
        self.video_path = path
        if not self.is_video():
            self.video_path = ''
            return "Erreur : ce n'est pas un fichier video"

        self.x_res, self.y_res = self.get_resolution()
        self.framerate = self.get_framerate()
        self.end_frame = self.get_duration_frames()
        self.codec = self.get_codec()
        return f" {os.path.basename(self.video_path)} \n {self.codec} \n {self.framerate} im.s \n {self.x_res}x{self.y_res} \n " \
               f"Durée : { timecode.frame_to_tc_02(self.end_frame,self.framerate)}   / {self.end_frame} images "




