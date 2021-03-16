import cv2
import subprocess as sp
import numpy
import time

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
         self.version_number = 0.5
         self.complete = False
         self.last_frame_analysed = 0
         self.analyse_duration = ''
         self.tc_offset = 0
         self.start_time = 0
         self.elapsed_time = 0


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
        self.issue_list = []
        current_frame = 0
        self.start_time = time.clock()
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

            # resizing original image to show progress
            resized = cv2.resize(image, (self.x_res // scale_factor, self.y_res // scale_factor), 1, 1)


            self.write_on_image(resized,f'frame:{str(current_frame)}',0.5,20,40)
            self.write_on_image(resized,f'progres:{(round(current_frame/self.end_frame,1))*100} %',0.5,20,70)
            self.write_on_image(resized,f'Time-Code:{timecode.frame_to_tc_02(current_frame,self.framerate)}',0.5,20,100)

            cv2.imshow(f'{os.path.basename(self.video_path)}: Analyse en cours  Appuyer sur q pour arreter',
                       resized)

           # cropping the image to get the 4 exterior lines to check

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

            if black_lines_detected != []:  # black lines have been detected
                if self.issue_list == []:  # self.issue_list list the dictionnaries with infos about the issue
                    self.issue_list.append({
                        'start_frm': current_frame,
                        'end_frm': current_frame,
                        'lines_detected': black_lines_detected[:]

                    })
                    # first frame of first issue- save snapshot
                    self.save_snapshot(image, len(self.issue_list),current_frame)
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
                        # first frame of new issue- save snapshot
                        self.save_snapshot(image,len(self.issue_list),current_frame)


            current_frame += 1

            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.last_frame_analysed = current_frame
                self.elapsed_time = time.clock() - self.start_time
                break
            if current_frame == self.end_frame:
                self.complete = True
                self.elapsed_time = time.clock() - self.start_time
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
        ret = ret + f' {len(self.issue_list)} issues found :-( \n\n'
        for issue in self.issue_list:
            ret = ret + f'°issue n° {i}\n'
            ret = ret + f'  start tc =  {timecode.frame_to_tc_02(issue.get("start_frm"),self.framerate)}\n'
            ret = ret + f'  end tc =  {timecode.frame_to_tc_02(issue.get("end_frm"),self.framerate)}\n'
            ret = ret + f'  position =  {issue.get("lines_detected")}\n'
            ret = ret + "\n"
            i+=1

        return ret

    def save_snapshot(self,img,issue_number,image_number):
        # temporaire
        report_path = os.path.dirname(self.video_path)
        report_path = report_path + '/report_snapshots'
        if not os.path.isdir(report_path):
            os.makedirs(report_path)

        filename = os.path.basename(self.video_path).split('.')[0]
        filename = filename + f'_{issue_number}.png'
        # write timecode on image
        self.write_on_image(img,timecode.frame_to_tc_02(image_number,self.framerate),2,img.shape[1]//8,
                            img.shape[0]//8)
        path = report_path + '/'+filename
        cv2.imwrite(filename=path,img=img)
        return


    def write_on_image(self,image,content,size,x,y):
        font = cv2.FONT_HERSHEY_SIMPLEX
        position = (x,y)
        fontScale = size
        fontColor = (20, 20, 220)
        lineType = 2
        cv2.putText(image, content,position,font,fontScale,fontColor,lineType)


    def generate_html_report(self):
        file = os.path.basename(self.video_path).split('.')[0]
        report_path = f'{self.video_path}_report.html'

        html_file ='<!DOCTYPE html><html><head><meta charset="utf-8"><style type="text/css">@page {size: A4 portrait;}\
        body {font: 20px Helvetica, sans-serif;color: #4d4d4d;background-color:  #4d4d4d;}h1 {font: 40px Helvetica,\
        sans-serif;color: white;text-align: center;}p {text-align: center;}code {color: white;}div {\
        background-color: #8c8c8c;width: 1000px;border: none;padding: 10px;\
        margin: 20px;}table,td {table-layout: fixed;width: 235px;padding: 5px;}\
        thead,tfoot {background-color: #8c8c8c;color: #4d4d4d;font: 20px Helvetica, sans-serif;text-align: center;}\
        th{font: 25px Helvetica, sans-serif;color: #4d4d4d;padding: 15px;}tr {text-align: center;padding: 15px;}\
        tr:nth-child(even) {background-color: #595959;color: #fff;}tr:nth-child(odd)  {background-color: #d9d9d9;\
         color:#404040;}.img_thumbnail{width: 235px;}.issue-header {background-color: #8c8c8c;}\
         .logo{align-content: center;width: 100px;}\
         </style><title>Blanking detector Report</title></head><header><div>\
         <img src="logo.png" class="logo"><h1>Blanking detection report<br></h1></div></header><body>'

        html_file = html_file + f' <div>  <ul><li>file checked :  <code>{os.path.basename(self.video_path)}</code></li>\
                                <li>date :  <code>01/02/2020</code></li>\
                                <li>codec :  <code>{self.codec}</code></li>\
                                <li>definition : <code>{self.x_res}x{self.y_res}</code></li>\
                                <li>framerate : <code>{self.framerate}</code></li>\
                                <li>starting timecode : <code>{timecode.frame_to_tc_02((self.start_frame+ self.tc_offset),self.framerate)}</code></li>\
                                <li>Duration:  <code>{timecode.frame_to_tc_02(self.end_frame,self.framerate)}</code></li>\
                                </ul></div>'

        if not self.complete:
            html_file = html_file + f'<div><p style ="font: 20px Helvetica, sans-serif;color:#BE1D11; text-align: center;">\
                                      Alert : analysis not complete - Interrupted by user \
                                      at {timecode.frame_to_tc_02(self.last_frame_analysed,self.framerate)}</p></div>'

        if self.issue_list != []:
            html_file = html_file + f'<div><p style="color: white;"> {self.end_frame} frames checked in {self.elapsed_time} s \
                                <p style="color: #BE1D11;"> {len(self.issue_list)} issues detected</p></p></div>'
        else:
            html_file = html_file + f'<div><p style="color: white;"> {self.end_frame} frames checked in {self.elapsed_time} s \
                                            <p style="color: green;"> {len(self.issue_list)} issues detected</p></p></div>'


        html_file = html_file + f'<div><table><thead><tr><td class="issue-header">Snapshot</td>\
                                <td class="issue-header">Issue type</td><td class="issue-header">Timecode(In/Out)</td>\
                                <td class="issue-header">Details</td></tr></thead><tbody>'

        for issue_number, issue in enumerate(self.issue_list, start=1):
            snapshot_path = f'./report_snapshots/{os.path.basename(self.video_path).split(".")[0]}'+ f'_{issue_number}.png'
            html_file = html_file + f' <tr><td><a href="{snapshot_path}"><img src="{snapshot_path}"class="img_thumbnail">\
            </a></td><td>Black lines detected</td><td>{timecode.frame_to_tc_02(issue.get("start_frm"),self.framerate)}\
            <br>{timecode.frame_to_tc_02(issue.get("end_frm"),self.framerate)}</td><td>{issue.get("lines_detected")}</td></tr>'

        html_file = html_file + f'</tbody></table></div></body><footer></footer></html>'

        report = open(report_path, "w")
        report.write(html_file)
        report.close()
        return
