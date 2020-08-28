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

Please note these limitations:

It is easier if you don't use a dedicated graphics card on x86. In our tests on Ubuntu 20, Focal Fossa, the gstreamer vaapi plugin can't use the hardware decoder on the NVIDIA GPU with the proprietary NVIDIA driver. The causes gstreamer to use a software decoder instead.

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

On Jetson Xavier, auto plugin selection of the gstreamer seems to be not working well, replacing "decodebin ! autovideosink sync=false" to "nvv4l2decoder ! nv3dsink sync=false" will solve the problem. Edit this 
[line](https://github.com/ricohapi/libuvc-theta-sample/blob/f8c3caa32bf996b29c741827bd552be605e3e2e2/gst/gst_viewer.c#L192) in the sample code and recompile.
