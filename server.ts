const express = require('express');
const next = require('next');

export { }

const dev = process.env.NODE_ENV !== 'production';
const prod = process.env.NODE_ENV === 'production';

const app = next({ dev });
const handle = app.getRequestHandler();

const PORT = 3060;

app.prepare().then(() => {

    const server = express();

    server.get("*", (req, res) => {
        console.log(`${req.ip} is comming!`);
        return handle(req, res);
    });

    server.listen(PORT, '127.0.0.1', (err?: any) => {
        if (err) return console.error(err);
        console.log(`> Kreimben.com is running on: http://127.0.0.1:${PORT}/`);
    });

}).catch((ex) => {
    console.error(ex.stack);
    process.exit(1);
})