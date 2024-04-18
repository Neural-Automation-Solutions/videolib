import cv2
import zmq
import base64
import numpy as np

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

  def get_frame_bytes(self) -> bytes:
    '''
    Returns the decoded base64 string from the TCP socket.
    '''
    return base64.b64decode(self.get_frame_string())

  def get_frame_nparr(self) -> np.array:
    '''
    Returns a numpy array of the frame received from the TCP socket.
    '''
    img = self.get_frame_bytes()
    npimg = np.frombuffer(img, dtype=np.uint8)
    return cv2.imdecode(npimg, 1)
