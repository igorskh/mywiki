# Matlab Python Engine Installation Failed on macOS

Paths in `setup.py` in `/path/to/MATLAB_R2020a.app/extern/engines/python` have to be configured manually.

The directory are not being recognised corretly by the setup script, find the lines with definition of `_bin_dir` and `_engine_dir` and replace them with absolute paths
```python
_bin_dir = "/path/to/MATLAB_R2020a.app/bin"+os.sep
_engine_dir = "/path/to/MATLAB_R2020a.app/extern/engines/python"+os.sep\
    + "dist" + os.sep + _matlab_package + os.sep + _engine_package + os.sep
```