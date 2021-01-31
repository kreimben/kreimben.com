FROM node:15.4.0

MAINTAINER aksidionkreimben@gmail.com

RUN mkdir -p /usr/src/nextjs
WORKDIR /usr/src/nextjs

COPY ./package*.json ./
RUN npm install
RUN npm install -g ts-node

COPY . .

RUN npm run build

EXPOSE 3060

ENTRYPOINT npm run server