import cv2
from src.video import Video

video = Video()

while True:
  try:
    img = video.get_frame_nparr()
    cv2.imshow("feed", img)
    cv2.waitKey(1)
  except KeyboardInterrupt:
    cv2.destroyAllWindows()
    break
