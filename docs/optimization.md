# gstreamer optimization on x86

We reduced latency to 220ms from the camera to the screen
by using two gstreamer plug-ins:

* nvdec hardware decoding plug-in for NVIDIA GPUs
* glimagesink OpenGL plug-in

## Overview

nvdec applies hardware decoding to the THETA H.264 stream and
outputs buffers in raw format on the GPU.

## Tests

### nvdec and glimagesink

```
pipe_proc = "nvdec ! glimagesink qos=false sync=false";
```

![gstreamer nvdec](images/optimization/gstreamer_nvdec.png)

foreground: 59.182

THETA video: 58.932

250ms


