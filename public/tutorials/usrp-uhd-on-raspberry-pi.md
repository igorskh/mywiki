# Install USRP UHD on Raspberry PI 3 with Python Support

## Prerequisites
- Raspberry PI 3 armv71
- Installed Raspbian
- Python 3

## Install
(Initial guide)[https://files.ettus.com/manual/page_build_guide.html]

(Initial guide for Python API)[https://kb.ettus.com/UHD_Python_API]

```bash
sudo apt update
sudo apt-get install libboost-all-dev libusb-1.0-0-dev python3-mako doxygen python3-docutils cmake build-essential 
```

There are some missing packages from the initial guide:
```bash
sudo apt update
sudo apt-get install python3-pip python3-setuptools python3-requests
```

Alternatively, if you use Python 2, replace python3-* packages with python-*.

Install python packages
```bash
pip3 install numpy
```

Clone and generate makefiles
```bash
git clone --recursive git://github.com/EttusResearch/uhd.git
cd uhd/host
mkdir build
cd build
cmake -DENABLE_PYTHON_API=ON -DNEON_SIMD_ENABLE=OFF ../
```

As far as I understand NEON_SIMD_ENABLE option should work, but it didn't for me.

Build and install
```bash
make
make test
sudo make install
```

Setup library path:
```bash
sudo ldconfig
```

If necessary, configure a static IP to the same subnet as your USRP device:
```
sudo ifconfig eth0 192.168.10.1 netmask 255.255.255.0
```

## Check
Try to find a USRP device

```
uhd_find_devices
```