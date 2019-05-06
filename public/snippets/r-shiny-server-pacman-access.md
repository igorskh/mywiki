# Pac-Man library for R server in shiny access error
*Tags: #r #shiny #ubuntu *

Problem: When running shiny server with pacman library, get an error:

```
lib = /usr/local/lib/R/site-library is not writable
```

The shiny server is running as a use `shiny` of group `shiny`, so in order to grant access to the packages folder, we need to add user `shiny` to the owner group `staff` as:

```
sudo usermod -a -G staff shiny
```