#!/usr/bin/python3

import glob
import io
from base64 import b64encode
from IPython.display import HTML
from IPython import display as ipythondisplay
from pathlib import Path


def display(videopath:str=None):
    if not videopath:
        mp4list = glob.glob('*.mp4')
        if len(mp4list) > 0:
            videopath = mp4list[0]
        else:
            raise Exception("Could not find video")

    video = io.open(videopath, 'rb').read()

    base64_encoded_mp4 = b64encode(video).decode('ascii')
    ipythondisplay.display(
      HTML(
          data='''
          <video alt="test" autoplay controls style="width: 400px; height: 200px;" id="theVideo">
            <source src="data:video/mp4;base64,{0}" type="video/mp4" />
          </video>
          <script>
          video = document.getElementById("theVideo")
          video.playbackRate = 0.25;
          </script>
          '''.format(base64_encoded_mp4)
          )
    )
    