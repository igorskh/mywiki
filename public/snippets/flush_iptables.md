# Flush iptables
*Tags: #bash #linux *

```bash
#!/bin/sh
echo "Flushing iptables rules..."
sleep 1
iptables -F
iptables -X
iptables -t nat -F
iptables -t nat -X
iptables -t mangle -F
iptables -t mangle -X
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
```

Source: (https://serverfault.com/questions/200635/best-way-to-clear-all-iptables-rules)[https://serverfault.com/questions/200635/best-way-to-clear-all-iptables-rules]