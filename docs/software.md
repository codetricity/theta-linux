## Software Requirements

### Live Streaming

You need to download the two GitHub repos below and 
compile the driver and sample code.

* [libuvc-theta](https://github.com/ricohapi/libuvc-theta)
* [libuvc-theta-sample](https://github.com/ricohapi/libuvc-theta-sample)

If you want to use `/dev/video0`, you will also need

* [v4l2loopback](https://github.com/umlaeute/v4l2loopback)

In addition, there are numerous dependencies to compile 
the tools listed above.  However, have no fear, we will
walk you through it.

#### How To Compile and Install

* [Build and install on x86 Ubuntu 20.04](https://youtu.be/Ji4WDvPHzQk)
* [Jetson Nano with OpenCV and VLC on /dev/video0](https://youtu.be/1xUMOvO_X5E)
* [Compile libuvc-theta on Jetson Nano - silent screencast](https://youtu.be/GoYi1tSIV80)
* [Build and run v4l2loopback on Jetson Nano](https://youtu.be/KrKwUWSYp2U). Needed for `/dev/video0`

#### How to Load v4l2loopback automatically

In the file `/etc/modules-load.d/modules.conf` add a new line `v4l2loopback`.

```
$ pwd
/etc/modules-load.d
craig@jetson:/etc/modules-load.d$ cat modules.conf 
# /etc/modules: kernel modules to load at boot time.
#
# This file contains the names of kernel modules that should be loaded
# at boot time, one per line. Lines beginning with "#" are ignored.

# bluedroid_pm, supporting module for bluetooth
bluedroid_pm
# modules for camera HAL
nvhost_vi
# nvgpu module
nvgpu

# for RICOH THETA live streaming
# v4l2loopback device on /dev/video0. specify in gst_viewer.c
v4l2loopback

craig@jetson:/etc/modules-load.d$ 
```

### USB API

* [libptp](https://sourceforge.net/projects/libptp/) - next section for detailed walkthrough


