FROM tomsik68/xampp:latest
EXPOSE 80
EXPOSE 443
ENV MYSQL_ROOT_PASSWORD=12345
ENV MYSQL_DATABASE=restaurantweb
VOLUME /opt/lampp/htdocs
CMD ["/opt/lampp/lampp", "start"]
FROM php:latest
VOLUME /var/www/html
COPY ./restaurantweb /www/var/html 

