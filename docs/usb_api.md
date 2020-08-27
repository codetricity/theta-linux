## USB API with libptp

### Equipment

* Jetson Nano
  * 5V 4amp power connector, set to 10amp
  * PWM fan blowing on heatsink and powered from the Nano board
* Jetpack 4.4, which is Ubuntu 18.04.5 LTS, Bionic Beaver
* RICOH THETA V
  * drawing power over USB cable from Nano

### Download libptp source

[libptp - Picture Transfer Protocol lib](https://sourceforge.net/projects/libptp/)

Get the newest version, which is 2-1.2 right now.

![libptp source download](images/usb_api/01_sourceforge_download.png)

### build libptp

```bash
$ ./configure
$ make
```

If you have a build error when compiling libusb, you may need to install the 
development libraries for libusb.

![libptp configuration error](images/usb_api/02_libptp_configure_error.png)

### install libusb-dev

```bash
$ sudo apt install libusb-dev
```

You may not need this step if you already have the libusb development
libraries installed.

![libusb-dev install](images/usb_api/03_libusb-dev_install.png)

### install libptp

```bash
$ sudo make install
```

![confirm build](images/usb_api/04_build_succeeded.png)

### set /usr/local/lib in library path

The default location of the libptp install is `/usr/local/lib`.  
Make sure that this is in your library path.  If it isn't,
add it to a file such as `libc.conf` in `/etc/ld.so.conf/`.

```
$ cd /etc/ld.so.conf.d/
$ ls
$ cat libc.conf
```

![library path](images/usb_api/05_confirm_usr_local.png)

### run ldconfig

Load the library configuration.

```
$ sudo /sbin/ldconfig -v
```

![ldconfig](images/usb_api/06_ldconfig.png)

### Test ptpcam

Connect RICOH THETA to Jetson with a USB cable.

Version of 2-1.2 of libptp has a bug in it.  Although
ptpcam does take pictures and function normally,
you will
see an error about capture status.

![capture status](images/usb_api/07_capture_status_error.png)

### Fix problem with libptp response

Go to line 77 of `ptp.h` and change `PTP_USB_INT_PACKET_LEN` 
to `28`.

![edit libptp source](images/usb_api/08_edit_libptp_source.png)

After modification, the code will look like this.

![fixed source](images/usb_api/09_libptp_source_fix.png)

### test ptpcam response again

Take a still image picture with `ptpcam --capture`.

![results after fix](images/usb_api/10_fix_results.png)

### Set camera to live streaming mode

Check on camera mode.

```
$ ptpcam --show-property=0x5013
```

Set to live streaming mode.

```
$ ptpcam --set-property=0x5013 --val=0x8005
```

![set to live streaming mode](images/usb_api/11_change_to_live_stream.png)

Using the official 
[RICOH USB API documentation](https://api.ricoh/docs/theta-usb-api/property/still_capture_mode/), you can verify that
`0x8005` is live streaming mode.  The camera LED should show that
the THETA is in LIVE mode.

![live led v](images/usb_api/live_led.png)

In our tests, the RICOH THETA Z1 could charge while streaming
over a USB 3.0 port (blue insert).  

After hours of streaming, the Z1 LED looks like this.

![live led z1](images/usb_api/live_z1.jpeg)

The response codes are shown below.

```
    0x0001 = single-shot shooting
    0x0003 = Interval shooting
    0x8002 = Movie shooting
    0x8003 = Interval composite shooting
    0x8004 = Multi bracket shooting
    0x8005 = Live streaming
    0x8006 = Interval shooting - tripod stabilizatio is off 
             (top/bottom correction and stitching optimized)
    0x8007 = Interval shooting - tripod stabilization is on
```

If you set the camera back to still image, single shot mode,
you will see this response.

```bash
$ ptpcam --set-property=0x5013 --val=0x0001

Camera: RICOH THETA V
'Still Capture Mode' is set to: 0x8005 (-32763)
Changing property value to 0x0001 [(null)] succeeded.
```
