FROM nginx:1.19.6

COPY ./nginx.conf /etc/nginx/nginx.conf
#COPY ./default.conf /etc/nginx/conf.d/default.conf
RUN rm -rf /etc/nginx/conf.d

EXPOSE 80