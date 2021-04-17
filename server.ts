const express = require('express');
const app = express();
const path = require('path');

// app.get('/', (requst, response) => {
//     response
//         .set("Content-Security-Policy", "default-src *; style-src 'self' http://* 'unsafe-inline'; script-src 'self' http://* 'unsafe-inline' 'unsafe-eval'")
//         .sendFile(path.join(__dirname + '/dist/'));
// });

app.use(express.static(path.join(__dirname, "dist")));

app.listen('8080', () => {
    console.log(`Server starts with ${process.env.PORT}`);
})
