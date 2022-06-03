# Code Snippets

There are two different snippets

1. Reset Power on Jetson USB ports
2. canny edge detection demo with gstthetauvc

## Reset Power on Jetson USB ports

Will turn on THETA V, Z1 if the camera has powered off.

```
$ sudo apt-get install libusb-1.0-0-dev
$ gcc -o power_cycle reset_jetson_usb_power.c -lusb-1.0
$ sudo ./power_cycle
```