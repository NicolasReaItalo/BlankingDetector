
def tc_to_frame(hh, mm, ss, ff, frame_rate):
    return ff + (ss + mm*60 + hh*3600) * frame_rate


def frame_to_tc(fn, framerate):
    ff = fn % framerate
    s = fn // framerate
    return (s // 3600, s // 60 % 60, s % 60, ff)

def frame_to_tc_02(fn, framerate):
    ff = fn % framerate
    s = fn // framerate
    return f"{int(s // 3600)}:{int(s // 60 % 60)}:{int(s % 60)}:{int(ff)}"


def tc_split(timecode):
    a = timecode.split(':')
    if len(a) < 4:
        return False
    return int(a[0]), int(a[1]),int(a[2]),int(a[3])

if __name__ == '__main__':
   print(frame_to_tc(2462, 24))
   print(tc_to_frame(hh =0,mm=0,ss=1,ff=0,frame_rate=24))

