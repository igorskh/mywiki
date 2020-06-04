# Remove Dangling Docker Images
*Tags: #docker #bash *

## Script
```bash
docker rmi $(docker images -f "dangling=true" -q)
```

If some containers are preventing from removing images:
```bash
docker container prune
```