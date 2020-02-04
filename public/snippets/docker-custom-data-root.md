# Docker custom data root folder

Edit /etc/docker/daemon.json

Set `data-root` to the new location, then restart the daemon:
sudo service docker restart