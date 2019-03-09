# Setup secure connection with Let's encrypt for Nginx
*Tags: #ubuntu #https #nginx * 

## Install Let's encrypt
Add the repository:
```
sudo add-apt-repository ppa:certbot/certbot
```

Update the package list and install the certbot:
```
sudo apt-get update
sudo apt-get install python-certbot-nginx
```


## Issue the cerificate
```
sudo certbot --nginx -d example.com -d www.example.com
```