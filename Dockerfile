FROM node:15.4.0

MAINTAINER aksidionkreimben@gmail.com

RUN mkdir /nextjs
WORKDIR /nextjs

COPY ./package*.json ./
RUN npm install

COPY . .

EXPOSE 3060 8080

ENTRYPOINT npm run server