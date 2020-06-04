# Git shows state modified but no actual changes

## Reason 1
Permission of files changed, we can tell git to ignore chmod changes by:
```
git config core.fileMode false
```