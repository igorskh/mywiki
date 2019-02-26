# Create Custom Ubuntu Service
*Tags: #ubuntu #bash * 

How to setup an executable as a service in Ubuntu.

## Instruction
Create a service file:
```
# nano /etc/systemd/system/service-name.service
```

With the following content:
```
[Unit]
Description=Service Name
[Service]
User=root
#change this to your workspace
WorkingDirectory=/root/service_folder
ExecStart=/root/service_folder/service-exec --host=0.0.0.0 --port=8080
SuccessExitStatus=143
TimeoutStopSec=10
Restart=on-failure
RestartSec=5
[Install]
WantedBy=multi-user.target
```

And reload the daemon, enable the service:
```
# systemctl daemon-reload
# systemctl enable service-name.service
# systemctl start service-name.service
```

The following actions can be performed to start/restart/stop service:
```
# systemctl start service-name.service
# systemctl restart service-name.service
# systemctl stop service-name.service
```