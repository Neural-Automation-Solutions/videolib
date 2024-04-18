import cv2
from src.video import Video

video = Video()

while True:
  try:
    cv2.imshow("feed", video.get_frame_nparr())
    cv2.waitKey(0)
  except KeyboardInterrupt:
    cv2.destroyAllWindows()
    break
