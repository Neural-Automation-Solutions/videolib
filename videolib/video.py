import cv2
import zmq
import base64
import numpy as np

from typing import Union, Tuple, List

class Video:
  '''
  A class that acts as a wrapper around the video capture service.
  Creates a TCP subscription to port 5555.
  Provides a simple API to get the video output in various forms.
  '''

  def __init__(self, port=5555) -> None:
    '''
    :param port: TCP port to listen to
    '''

    self.context = zmq.Context()
    self.footage_socket = self.context.socket(zmq.SUB)
    self.footage_socket.connect(f'tcp://localhost:{port}')
    self.footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode_(''))

  def get_frame_string(self) -> str:
    '''
    Returns the base64 encoded string from the TCP socket.
    '''
    return self.footage_socket.recv_string()

  def get_frame_bytes(self, _return_string=False) -> bytes:
    '''
    Returns the decoded base64 string from the TCP socket.
    '''
    fstring = self.get_frame_string()
    b64 = base64.b64decode(fstring)
    if _return_string:
      return b64, fstring
    return b64

  def get_frame_nparr(self, _return_string=False, _return_bytes=False) -> Union[Tuple[np.ndarray, bytes, str], Tuple[np.ndarray, bytes], Tuple[np.ndarray, str], np.ndarray]:
    '''
    Returns a numpy array of the frame received from the TCP socket.
    '''
    img, fstring = self.get_frame_bytes(_return_string=True)
    npimg = np.frombuffer(img, dtype=np.uint8)
    nparr = cv2.imdecode(npimg, 1)

    if _return_string:
      if _return_bytes:
        return nparr, img, fstring
      else:
        return nparr, fstring

    if _return_bytes:
      return nparr, img

    return nparr
