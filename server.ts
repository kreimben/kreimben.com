const express = require('express');
const app = express();
const path = require('path');

app.get('/', (requst, response) => {
    response.sendFile(path.join(__dirname + '/dist/index.html'));
});

app.listen('8080', () => {
    console.log(`Server starts with ${process.env.PORT}`);
})