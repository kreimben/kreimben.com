const express = require('express');
const next = require('next');

const dev = process.env.NODE_ENV !== 'production';
const prod = process.env.NODE_ENV === 'production';

const app = next({ prod });
const handle = app.getRequestHandler();

const PORT = 3060;

app.prepare().then(() => {

    const server = express();

    server.get("*", (req, res) => {
        return handle(req, res);
    });

    server.listen(PORT, (err) => {
        if (err) throw err;
        console.log(`Kreimben.com is running on: http://127.0.0.1:${PORT}/`);
    });

}).catch((ex) => {
    console.error(ex.stack);
    process.exit(1);
})

//export { }