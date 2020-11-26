# USB Tethering iPhone to Raspberry PI

Install packages:

```bash
sudo apt-get install usbmuxd gvfs ipheth-utils libimobiledevice-utils gvfs-backends gvfs-bin gvfs-fuse ifuse
```

As for 25.11.2020, the ipheth driver doesn't work with iOS 14.0+

The `drivers/net/usb/ipheth.c` needs to be updated with following:
```c
#define IPHETH_BUF_SIZE         1514
```