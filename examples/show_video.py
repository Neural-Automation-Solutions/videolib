import cv2
from videolib.video import Video

video = Video()

while True:
  try:
    img, bytes, fstring = video.get_frame_nparr(_return_string=True, _return_bytes=True)
    print(type(fstring))
    print(type(bytes))
    cv2.imshow("feed", img)
    cv2.waitKey(1)
  except KeyboardInterrupt:
    cv2.destroyAllWindows()
    break
