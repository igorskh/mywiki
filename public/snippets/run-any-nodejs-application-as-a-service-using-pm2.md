# Run a NodeJS application as a service on Ubuntu using pm2
*Tags: #ubuntu #pm2 #nodejs *

[pm2](http://pm2.keymetrics.io) is a process manager for NodeJS applications.

## Running a JavaScript file
```
pm2 start --name=service-name app.js
```

## Running a npm start script
```
pm2 start --name=service-name npm --start 
```