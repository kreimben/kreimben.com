FROM node:15.4.0
MAINTAINER aksidionkreimben@gmail.com

RUN mkdir -p /usr/src/front-end
WORKDIR /usr/src/front-end

COPY ./package*.json ./usr/src/front-end
RUN npm install

COPY . /usr/src/front-end

EXPOSE 3000
CMD npm run build && npm run customStart