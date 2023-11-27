# EmoMusic
Let's Fill the gap between Emotions and TEchnical Field, by EMSR.
Open to Contribute; Free to Use (Creatibve Commons); Currently under Construction.
Developed by SUKH, (c) 2023.
## Presentation-Preview
[<img src="https://github.com/HEYSUKH/EmoMusic/assets/147260152/7fb9342c-e667-4d6f-a360-56010cc0f96f" width="100%">](https://www.canva.com/design/DAF1SCe5FZM/V857N9f4kJd2nctXopQG2g/edit?utm_content=DAF1SCe5FZM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

, or preview Presentation from [Here](https://www.canva.com/design/DAF1SCe5FZM/V857N9f4kJd2nctXopQG2g/edit?utm_content=DAF1SCe5FZM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)


## Getting Started
### Forking
First things First; [Fork This Repo](https://github.com/HEYSUKH/EmoMusic/fork) in order to getting started.
### 1. add your own emotions to DeepFace existing data; in ```main.emotion```
[preview]
![image](https://github.com/HEYSUKH/EmoMusic/assets/147260152/50664d36-99af-48b3-b7be-77294ad8c6ea)
**Command to add Emottions**:-
```
elif(emotion == "[emotional_state]"):
      [Action]
```

### 2. Input Data Content
Making users upload files or Capturing images directly from User's Webcam, By using JS in Python, As follows:
```
import imutils
import numpy as np
import cv2
from google.colab.patches import cv2_imshow
from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode


def take_photo(filename='[path]', quality=0.8):
  js = Javascript('''
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = 'Capture';
      div.appendChild(capture);

      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});

      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();

      // Resize the output to fit the video element.
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

      // Wait for Capture to be clicked.
      await new Promise((resolve) => capture.onclick = resolve);

      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('[path]', quality);
    }
    ''')
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename
```
if you are using Google colab, then firstly import drive
```
from google.colab import drive
drive.mount('/content/drive')
```
now getting user's pic fronm Camera/webcam
```
image_file = take_photo()
```

### 3. Modifying Locations
Make sure to modify locations, highlighted follows:
![image](https://github.com/HEYSUKH/EmoMusic/assets/147260152/cdd8c5b5-3fbf-44a1-b9d8-4b2bd5f21d78)
![image](https://github.com/HEYSUKH/EmoMusic/assets/147260152/79dfaf80-b0bb-4c26-a37d-786547f99c65)

### 4. Good To Go
Now use this in Your Project Fully freely!

# Rights
Copyright (c) 2023, By [SUKH](https://github.com/HEYSUKH). All Rights Reserved.
