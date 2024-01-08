# Certbot

A certbot docker image with embind http server and try renew certificates every 2 monthes.

## Get Started 

### Standalone
* Pull docker image  
  $ docker pull yufishing/certbot

* Run standalone  
```  
  $ docker run -v [path-4-cert]:/etc/letsencrypt -p 80:80 yufishing/certbot 
  $ docker exec -it [Container ID] certbot --agree-tos --webroot --webroot-path /srv/www -m [email] -d [domain]  
```  
  
### Docker Compose with Nginx  
  Nginx http config:
```  
  location /.well-known/acme-challenge {
        root /var/www
  }
```    


  Docker Compose volume mapping
```
  nginx:
    volumes:
    - [www-root]:/var/www
    - [path-cert]:/etc/nginx/certs
  
  certbot:
    volumes:
    - [www-root]:/srv/www
    - [path-cert]:/etc/letsencrypt
```
