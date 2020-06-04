# Clone linux volume remotely using dd and ssh
*Tags: #ubuntu #lvm #dd #ssh * 

## Description
This document describes process of cloning a linux LVM volume from one machine to another remotely using `dd` and `ssh`. The volume is a `root` system volume.

## Tools
We will use the following tools:
* Ubuntu 18.04
* LVM2
* openssh-server
* dd

In addition we would need:
* Two USB sticks with live Ubuntu image
* Ethernet cable

## Process

We clone a linux volume from host to a client. In case we clone a system volume, we ould need two live USB drives both for host and client.

In addition, we have a non-LVM UEFI partition, we have sample partition map of the LVM volume group on the host as following.
```bash
boot ubuntu-vg 2,00g # mounted to /boot
home ubuntu-vg 1000,0g # mounted to /home
root ubuntu-vg 80,0g # mounted to /
swap ubuntu-vg 8,0g # swap partition
```

On the client we reproduce exactly the same partition map and perform Ubuntu installation. Firstly, partition disk to have at least two volumes for EFI and the systems. For example, if the disk is `/dev/sda` you would have `/dev/sda1` for EFI and `/dev/sda2` for your LVM.
```bash
pvcreate /dev/sda2
vgcreate ubuntu-vg /dev/sda2
lvcreate -L2G -n swap ubuntu-vg
lvcreate -L2G -n boot ubuntu-vg
lvcreate -L80G -n root ubuntu-vg
lvcreate -l 100%FREE -n home ubuntu-vg
```

When performing Ubunt installation, choose `/dev/sda1` as your EFI parition, and the swap, boot, root, home with corresponding mount points ant ext4 file system.

### Setup SSH

After installing the OS, we can stay on the live USB. Directly connect by ethernet and configure the SSH on the host:
```bash
# set password for root
sudo passwd root

# install ssh server
sudo apt update 
sudo apt install openssh-server

# allow ssh for root
nano /etc/ssh/sshd_config
# Uncomment and set PermitRootLogin to yes  
```

**Important! If you don't do this, the OS will not be able to boot anymore.**
Using `blkid` we need to get the UUID of the UEFI volume and the root partitions.

### Clone volume

Clone with the following command:
```bash
ssh root@192.168.0.1 dd if=/dev/ubuntu-vg/root bs=16M | dd of=/dev/ubuntu-vg/root bs=16M status=progress 
```

### Restore UUIDs of volumes
Edit /etc/fstab change Boot volume UUID to client’s UEFI volume UUID.

Lastly, restore the UUID of client’s root volume:
tune2fs -U $(rootuuid) /dev/ubuntu-vg/root