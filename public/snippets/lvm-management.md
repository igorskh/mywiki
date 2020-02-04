# Commands for managing LVM

## Useful commands
```bash
pvs -v # physical volumes list
vgs -v # volume groups list
lvs -v # logical volumes list
```

## Useful links
https://unix.stackexchange.com/questions/306157/resize-root-lvm-partition 
https://blog.shadypixel.com/how-to-shrink-an-lvm-volume-safely/

## Create EFI bootable
mkpart ESP fat32 1MiB 513MiB
parted /dev/sdX
set 1 boot on

## LVM Resize
```bash
# check the file system
e2fsck -f /dev/s93079-vg/root
# resize the volume
resize2fs /dev/s93079-vg/root 90G
# reduce the logical volume
lvreduce -L 100G /dev/s93079-vg/root
```

## Create physical volume
The disk has to be partitioned at least to two partitions - UEFI and OS. The UEFI must be outside of the LVM partition.

Once partitioning is done, create the 
`pvcreate /dev/sdx2`

## Create volume group
`vgcreate ubuntu-vg  /dev/sdx2`

## Create volume
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/logical_volume_manager_administration/lvm_examples 

lvcreate -L 2G -n new_logical_volume new_vol_group

## Remove volume/volume group/physical volume
```bash
lvremove /dev/ubuntu-vg/homevol
vgremove ubuntu-vg
pvremove /dev/sdx2
```

## Create and restore snapshots

lvcreate -s -L 20M -n volume1_snapshot /dev/volume_group/volume1

lvconvert --merge /dev/volume_group/volume1_snapshot

https://computingforgeeks.com/install-arch-linux-with-lvm-on-uefi-system/ 