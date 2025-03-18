## Getting Help

* [Updated Docs and Events](https://theta360.guide/special/linuxstreaming/)
* [Community discussion - Linux Streaming](https://community.theta360.guide/t/live-streaming-over-usb-on-ubuntu-and-linux-nvidia-jetson/4359?u=craig)
* [Community discussion - USB API](https://community.theta360.guide/t/ricoh-theta-api-over-usb-cable-z1-v-s-sc-models/65?u=craig)
* If you want to talk to someone, send email to jcasman@oppkey.com 


## FAQ

### Can I stream indefinitely?

The THETA Z1 can power off the USB-C port and stream at the same time.
Using USB 3.0 or better, the charge increases in our tests.  The
camera does get hot.  Upgrade to the latest firmware.  If possible,
attach a small fan to your tripod and point it at the body of the
THETA.

The V drains slowly.  It will last about 8 hours.  You may be able 
to bypass the battery, but this is not tested.

### /dev/video0 freezes on x86

Change [line 190](https://github.com/ricohapi/libuvc-theta-sample/blob/f8c3caa32bf996b29c741827bd552be605e3e2e2/gst/gst_viewer.c#L190) of gst_viewer.c.

```c
if (strcmp(cmd_name, "gst_loopback") == 0)
    pipe_proc = "decodebin ! autovideoconvert ! "
        "video/x-raw,format=I420 ! identity drop-allocation=true !"
        "v4l2sink device=/dev/video0 qos=false sync=false";
```

### The THETA is not appearing on /dev/video0

Install [v4l2loopback](https://github.com/umlaeute/v4l2loopback).

### How do I reduce the default 4K stream to 2K to improve AI processing?

If your AI processing is going to slowly, try to reduce resolution from 4K to 2K.  You likely need to do this
on Jetson Nano as 4K often hangs due to limited resources on Nano.

In gst_viewer.c, change [line 248](https://github.com/ricohapi/libuvc-theta-sample/blob/f8c3caa32bf996b29c741827bd552be605e3e2e2/gst/gst_viewer.c#L248) from THETAUVC_MODE_UHD_2997 to THETAUVC_MODE_FHD_2997.

Refer to [thetauvc.c#L55](https://github.com/ricohapi/libuvc-theta-sample/blob/f8c3caa32bf996b29c741827bd552be605e3e2e2/gst/thetauvc.c#L55) for definition.

### I can't use it on Xavier

Change to:

"nvv4l2decoder ! nv3dsink sync=false" 

### gstthetauvc showing _Found 1 Theta(s), but none available

If you have another version of libuvc installed, please uninstall it first.

See [this closed issue on GitHub](https://github.com/nickel110/gstthetauvc/issues/1#issuecomment-1100465786).

This is the advice from nickel110, the author of the gstthetauvc.

_That is a typical error when the program is loading the original libuvc.so.
If libuvc package is installed on your system, uninstall it._

This was the error message.

```text
Setting pipeline to PAUSED ...
ERROR: Pipeline doesn't want to pause.
ERROR: from element /GstPipeline:pipeline0/GstThetauvcsrc:thetauvcsrc0: Found 1 Theta(s), but none available.
Additional debug info:
gstthetauvcsrc.c(495): gst_thetauvcsrc_start (): /GstPipeline:pipeline0/GstThetauvcsrc:thetauvcsrc0
Setting pipeline to NULL ...
Freeing pipeline ...
```

This is another [error message from buburider](https://community.theta360.guide/t/live-streaming-over-usb-on-ubuntu-and-linux-nvidia-jetson/4359/339?u=craig).

```text
ERROR: Pipeline doesn't want to pause.
Setting pipeline to NULL ...
ERROR: from element /GstPipeline:pipeline0/GstThetauvcsrc:thetauvcsrc0: Found 1 Theta(s), but none available (No such device).
Additional debug info:
gstthetauvcsrc.c(493): gst_thetauvcsrc_start (): /GstPipeline:pipeline0/GstThetauvcsrc:thetauvcsrc0
Freeing pipeline ...
0:00:00.761629738     8 0x55dc6da40c00 DEBUG            thetauvcsrc gstthetauvcsrc.c:270:gst_thetauvcsrc_finalize:<thetauvcsrc0> finalize
```

This is his [solution](https://community.theta360.guide/t/live-streaming-over-usb-on-ubuntu-and-linux-nvidia-jetson/4359/347?u=craig).

> I’ve just found the issue: my jetson computer had a previous libuvc library installed. So, instead of using libuvc-theta, the application loaded the native version. This is the reason why the same code was working in my laptop. In the laptop, the native version of libuvc didn’t exist. After resolving that, it works fine.
