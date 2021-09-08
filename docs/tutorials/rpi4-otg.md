# Enable USB OTG on Raspberry PI 4
Edit `/boot/config.txt`, add in the end of the file:
```text
dtoverlay=dwc2
```

Edit `/boot/cmdline.txt`, add after rootwait:
```text
modules-load=dwc2,g_ether
```

Create `/etc/network/interfaces.d/usb0` to assign a static IP address
```text
auto usb0
allow-hotplug usb0
iface usb0 inet static
  address 10.55.0.1
  netmask 255.255.255.248
```

## Windows 10 
A missing driver: [https://modclouddownloadprod.blob.core.windows.net/shared/mod-rndis-driver-windows.zip](https://modclouddownloadprod.blob.core.windows.net/shared/mod-rndis-driver-windows.zip)

It needs to be applied to a *Ports (COM & LPT)* in the Device Manager