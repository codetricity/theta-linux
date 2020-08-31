## Hardware Requirements for Linux and the RICOH THETA

![nano with fan](images/usb_api/nano_fan.jpeg)

### Jetson Nano - Reference Platform

Our reference platform is the NVIDIA Jetson Nano
running JetPack 4.4, which is Ubuntu 18.04.
The Nano is an ARM A57 with a 128-core Maxwell GPU,
4GB 64-bit LPDDR4.

The nano is powered by a 5V 4A barrel connector,
not the microUSB which is 5V 2A.  Our Nano has
an external fan on the PWM header and a 64GB
microSD card.

### x86 Linux

We've also tested the libuvc-theta (streaming) and
libuvc-theta-sample (streaming sample application)
on x86 64bit Linux using Ubuntu 20.04 LTS, Focal Fossa.

![x86 screenshot](images/usb_api/x86.jpeg)

![x86 system info](images/usb_api/x86_system.png)

We've tested v4l2loopback with gst_loopback on a low-end Pentium
x86 computer.  It works fine.  Thanks to commuity member Yu You
for this fix to gst_view.c.  Note the addition of `qos=false` to
the pipeline.  This is currently on 
[line 190](https://github.com/ricohapi/libuvc-theta-sample/blob/f8c3caa32bf996b29c741827bd552be605e3e2e2/gst/gst_viewer.c#L190).

```c
if (strcmp(cmd_name, "gst_loopback") == 0)
    pipe_proc = "decodebin ! autovideoconvert ! "
        "video/x-raw,format=I420 ! identity drop-allocation=true !"
        "v4l2sink device=/dev/video0 qos=false sync=false";
```

Screenshot of loopback running on `/dev/video0`, tested with vlc.

![x86 and vlc](images/hardware/x_86.png)



#### Addtional x86 Information

If you're having problems after making the modification
described above, you can try to temporarily disable your
dedicated graphics card on x86. In our tests on Ubuntu 20, Focal Fossa, the gstreamer vaapi plugin can't use the hardware decoder on the NVIDIA GPU with the proprietary NVIDIA driver. The causes gstreamer to use a software decoder instead.

This will likely cause many frame drops on your system. You can verify this by setting the GST_DEBUG environment variable to 2 or 3 and then running gst_loopback. You will likely see many frame drop messages.

There are two possible workarounds:

1. Use the nvdec plugin Although the nvdec plugin is a part of the gstreamer-plugins-bad, it is not included in binary distribution due to license problem. Thus, you have to build the plugin by yourself. You also need to modify the pipeline of the gst_loopback accordingly.
2. Use hardware decoder on the iGPU You may need additional setup to run X server on the iGPU,



### Raspberry Pi

The Raspberry Pi will work great with the USB API.  However, you 
will not have a good experience streaming 4K, even with the 
Raspberry Pi 4.

The Raspberry Pi's H.264 hardware decoder does not support 4K resolution even on the Raspberry Pi4. In addition, older Pis' (Pi to Pi3) memory bandwidth(32bit DDR2) is too poor to handle even FHD stream from THETA V/Z1.

### NVIDIA Jetson Xavier

The Xavier is better for testing.  However, it is more expensive.  If your 
budget permits, it is better to get the Xavier.  You may have problems
with 4K AI processing with the Nano.

On Jetson Xavier, auto plugin selection of the gstreamer seems to be not working well, replacing "decodebin ! autovideosink sync=false" to "nvv4l2decoder ! nv3dsink sync=false" will solve the problem. Edit this 
[line](https://github.com/ricohapi/libuvc-theta-sample/blob/f8c3caa32bf996b29c741827bd552be605e3e2e2/gst/gst_viewer.c#L192) in the sample code and recompile.

### Heat and Cooling of Linux Computer

You need to cool the Nano.  Without a fan, you may get thermal 
throttling when live streaming
with AI processing. 

![nano with fan](images/hardware/cooling_nano.png)

![nano with fan mount](images/hardware/fan_mount.png)

The fan is 5V pwm.  I've also used a 12V fan before I
ordered the 4V fan from Amazon.

