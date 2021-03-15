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

        font = cv2.FONT_HERSHEY_SIMPLEX
        UpLeftCornerOfText = (0, 50)
        UpLeftCornerOfText_line2 = (0, 70)
        fontScale = 0.5
        fontColor_ok = (255, 255, 128)
        fontColor_issue = (0, 0, 255)
        lineType = 2

        while True:
            # Capture frame-by-frame
            raw_image = pipe.stdout.read(self.x_res * self.y_res * 3)

            image = numpy.frombuffer(raw_image, dtype='uint8')
            image = image.reshape((self.y_res, self.x_res, 3))
            resized = cv2.resize(image, (self.x_res // scale_factor, self.y_res // scale_factor), 1, 1)

            percentage = (round(current_frame/self.end_frame,1))*100


            cv2.putText(resized, f'image:{str(current_frame)} ',
                        UpLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor_ok,
                        lineType)

            cv2.putText(resized, f' {percentage} %',
                        UpLeftCornerOfText_line2,
                        font,
                        fontScale,
                        fontColor_ok,
                        lineType)

            cv2.imshow(f'{os.path.basename(self.video_path)}: Analyse en cours... {self.x_res}x{self.y_res}  Appuyer sur q pour arreter',
                       resized)

           ###  INSERER LE CODE DE VERIF ICI

            top_line = image[0 + self.crop_top:1+self.crop_top, 0 + self.crop_left :self.x_res - self.crop_right]
            bottom_line = image[self.y_res - 1-self.crop_bottom:self.y_res-self.crop_bottom, 0 + self.crop_left:self.x_res- self.crop_right]
            left_line = image[0 + self.crop_top :self.y_res - self.crop_bottom, 0 + self.crop_left:1 + self.crop_left]
            right_line = image[0 + self.crop_top:self.y_res - self.crop_bottom, self.x_res - 1 - self.crop_right:self.x_res- self.crop_right]

            black_lines_detected = []
            if numpy.max(top_line) <= self.treshold:
                black_lines_detected.append('TOP')
            if numpy.max(bottom_line) <= self.treshold:
                black_lines_detected.append('BOTTOM')
            if numpy.max(left_line) <= self.treshold:
                black_lines_detected.append('LEFT')
            if numpy.max(right_line) <= self.treshold:
                black_lines_detected.append('RIGHT')

            if black_lines_detected != []:
                if self.issue_list == []:
                    self.issue_list.append({
                        'start_frm': current_frame,
                        'end_frm': current_frame,
                        'lines_detected': black_lines_detected[:]

                    })
                else:
                    if self.issue_list[-1].get('end_frm') == (current_frame - 1):  ## same issue on previous image
                        self.issue_list[-1]['end_frm'] = current_frame
                        for item in black_lines_detected:
                            if item not in self.issue_list[-1]['lines_detected']:
                                self.issue_list[-1]['lines_detected'].append(item)

                    else: ## new issue
                        self.issue_list.append({
                            'start_frm': current_frame,
                            'end_frm': current_frame,
                            'lines_detected': black_lines_detected[:]

                        })


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
        return self.generate_header()


    def generate_header(self):
        return f"fichier: {os.path.basename(self.video_path)} \n {self.codec} \n cadence: {self.framerate} im.s \n resolution: {self.x_res}x{self.y_res} \n " \
               f"Durée (h:m:s:i) : {timecode.frame_to_tc_02(self.end_frame, self.framerate)}   / {self.end_frame} images "



    def generate_report(self):
        i = 1
        ret= ''
        if len(self.issue_list) < 1:
            return "no issue detected :-)"
        for issue in self.issue_list:
            ret = ret + f'°  issue n° {i}\n'
            ret = ret + f'start tc =  {timecode.frame_to_tc_02(issue.get("start_frm"),self.framerate)}\n'
            ret = ret + f'end tc =  {timecode.frame_to_tc_02(issue.get("end_frm"),self.framerate)}\n'
            ret = ret + f'position =  {issue.get("lines_detected")}\n'
            ret = ret + "\n"
            ret =ret + '    '
            i+=1

        return ret


