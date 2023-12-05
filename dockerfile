version: '3'
services:
 xampp:
 image: tomsik68/xampp:latest
 ports:
 -"80:80"
 -"443:443"
 volumes:
 -./restaurantweb:/opt/lampp/htdocs
 networks:
 - mynet
 environment:
 - MYSQL_ROOT_PASSWORD=12345
 - MYSQL_DATABASE=restaurantweb
 php:
 image: php:latest
 volumes:
 - ./restaurantweb:/var/www/html
 networks:
 - mynet
networks:
 mynet
