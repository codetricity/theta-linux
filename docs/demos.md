## Ongoing Tests with Linux Streaming

![canny opencv](images/demos/canny_opencv_demo.png)

Using Nvidia Jetson Nano live streaming from a THETA V.
Processing done with Python3, OpenCV 4.4.

### DetectNet

[DetectNet](https://developer.nvidia.com/blog/detectnet-deep-neural-network-object-detection-digits/) 
first applied to single frame with SSD Mobilenet-v2.  This is not from
a live stream at the moment.  Maybe it will be before
the meetup.  :-)

See [Jetson Nano inference benchmarks](https://developer.nvidia.com/embedded/jetson-nano-dl-inference-benchmarks).

Code is available in the at 
[https://github.com/dusty-nv/jetson-inference](https://github.com/dusty-nv/jetson-inference)

There is super small text in the green box that says, "person".  The
system accurately detected the only person in the image.

It is 88.6 percent confident that I am a person.  Nice.

![detect person](images/demos/detect_close_front.jpg)

Despite the distorted view of my feet, the program does detect 
the human form.

![detect person](images/demos/detect_human.png)

Even at night, in low-light conditions with me on the 
side of the shutter button, the program did detect me.


![detect person](images/demos/output_v.jpg)

However, there were many frames where I was not detected.

To proceed, you will likely need a database of fisheye or 
equirectangular images to build your own model. 


### OpenCV Python

![canny demo](images/demos/canny_only.png)

Works on live stream.  

![community opencv](images/demos/community_opencv.jpeg)

#### Procedure

* install libuvc-theta
* install libuv-theta-sample
* install v4l2loopback
* load kernel modules for v4l2loopback and verify that /dev/video0 or equivalent shows THETA stream
* run Python script with cv2

Recommend you recompile OpenCV 4.4 from source code.
May take 2.5 hours if you compile on the Nano.

Frame resize test.

```python
import cv2

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
```

One script to install OpenCV 4.3 is from AastaNV [here](https://github.com/AastaNV/JEP/blob/master/script/install_opencv4.3.0_Jetson.sh).

The script I used is from mdegans [here](https://github.com/AastaNV/JEP/blob/master/script/install_opencv4.3.0_Jetson.sh)

[Code for OpenCV Demo with Canny from RICOH THETA V](https://gist.github.com/codetricity/d06068bee816e52eb7aba6b94eb5d119).  This is the edge detection demo with the white
lines on black background. 


### OpenPose
Works on live stream with Jetpack 4.3, not 4.4.

![open pose](images/demos/stickman.jpg)

