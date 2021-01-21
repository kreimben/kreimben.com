FROM node:15.4.0
MAINTAINER aksidionkreimben@gmail.com

RUN mkdir -p /nextjs
WORKDIR /nextjs

COPY ./package*.json ./
RUN npm install

COPY . /nextjs

RUN npm run build

FROM nginx:1.19.6

COPY ./nginx.conf ./etc/ngingx/nginx.conf
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /nextjs/out /usr/share/nginx/html

EXPOSE 3000 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]