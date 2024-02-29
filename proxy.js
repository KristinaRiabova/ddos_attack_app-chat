const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();


app.use('/', createProxyMiddleware({
    target: 'http://localhost:8000', 
    changeOrigin: true,
}));


app.use('/login', createProxyMiddleware({
    target: 'http://localhost:8000', 
    changeOrigin: true,
}));

const port = 3000;
app.listen(port, () => {
    console.log(`The proxy server is running on port ${port}`);
});
