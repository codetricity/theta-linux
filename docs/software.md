# Software Requirements

## All Software for Live Streaming

You need to download the two GitHub repos below and 
compile the driver and sample code.

* [libuvc-theta](https://github.com/ricohapi/libuvc-theta)
* [libuvc-theta-sample](https://github.com/ricohapi/libuvc-theta-sample)

If you want to use `/dev/video0`, you will also need

* [v4l2loopback](https://github.com/umlaeute/v4l2loopback)

In addition, there are numerous dependencies to compile 
the tools listed above.  However, have no fear, we will
walk you through it.

### How To Compile and Install all Required Software

* [Build and install on x86 Ubuntu 20.04](https://youtu.be/Ji4WDvPHzQk)
* [Jetson Nano with OpenCV and VLC on /dev/video0](https://youtu.be/1xUMOvO_X5E)
* [Compile libuvc-theta on Jetson Nano - silent screencast](https://youtu.be/GoYi1tSIV80)
* [Build and run v4l2loopback on Jetson Nano](https://youtu.be/KrKwUWSYp2U). Needed for `/dev/video0`

## Getting Stream on /dev/video0

Steps:

1. compile and install [libuvc-theta](https://github.com/ricohapi/libuvc-theta)
2. compile and install [libuvc-theta-sample](https://github.com/ricohapi/libuvc-theta-sample)
3. compile and install [v4l2loopack](https://github.com/umlaeute/v4l2loopback)
4. run `gst_loopback` from `libuvc-theta-sample`
5. access the correct video device with OpenCV or any video 4 Linux 2 application such as VLC.  The video device is 
[specified in the source code](https://github.com/ricohapi/libuvc-theta-sample/blob/f8c3caa32bf996b29c741827bd552be605e3e2e2/gst/gst_viewer.c#L190).

### Compile and Install v4l2loopback

```
$ git clone https://github.com/umlaeute/v4l2loopback.git
$ cd v4l2loopback
$ make 
$ sudo make install
$ sudo depmod -a
```

### Load and use

This assumes that you have adjusted the video device in 
`gst_viewer.c`.

```
$ sudo modprobe v4l2loopback
$ cd path_to_gst_loopback_directory
$ ./gst_loopback
$ cvlc v4l2:///dev/video2
VLC media player 3.0.9.2 Vetinari (revision 3.0.9.2-0-gd4c1aefe4d)
[0000556fc2bd6db0] dummy interface: using the dummy interface module...
```


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

#### Check kernel module load

```
$ lsmod
Module                  Size  Used by
bnep                   16562  2
zram                   26166  4
overlay                48691  0
spidev                 13282  0
v4l2loopback           37383  0
nvgpu                1579891  18
bluedroid_pm           13912  0
ip_tables              19441  0
x_tables               28951  1 ip_tables
craig@jetson:/etc/modules-load.d$ 
```

## v4l2loopback tests and examples

### gst-launch-1.0 pipeline

```
$ gst-launch-1.0 v4l2src device=/dev/video2 ! video/x-raw,framerate=30/1 ! xvimagesink
Setting pipeline to PAUSED ...
Pipeline is live and does not need PREROLL ...
Setting pipeline to PLAYING ...
New clock: GstSystemClock
```

![gst-launch-1.0 example](images/software/gst_launch_example.jpg)



## USB API

* [libptp](https://sourceforge.net/projects/libptp/) - next section for detailed walkthrough


