# Run GUI application in Docker
*tags: #docker *


```bash
xhost +local:docker
docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix hello-world
```