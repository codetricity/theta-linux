# Code Snippets

There are two different snippets

1. Reset Power on Jetson USB ports
2. canny edge detection demo with gstthetauvc

## OpenCV canny edge demo

Works with v4l2loopback or gstthetauvc (recommended).

### v4l2loopback

With the RICOH THETA on `/dev/video2`

```text
python3 canny_edge.py --video_device 2
```

### gstthetauvc

with nvdec hardware acceleration

```text
python3 canny_edge.py
```

## Reset Power on Jetson USB ports

Will turn on THETA V, Z1 if the camera has powered off.

```text
sudo apt-get install libusb-1.0-0-dev
gcc -o power_cycle reset_jetson_usb_power.c -lusb-1.0
sudo ./power_cycle
```
