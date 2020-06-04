# Setup a reverse proxy in Nginx
*Tags: #nginx #ubuntu *

An application running on a local host. And the reverse proxy can give a public access, add HTTPS support.

First create or edit existing nginx 
``` 
nano /etc/nginx/sites-available/reverse-proxy.conf
```

Here is a configuration for the reverse proxy:
```
server {
  listen 80;
  server_name api2.cloud.roundeasy.ru;
  location / {
    proxy_pass http://localhost:8081;
  }
}
```