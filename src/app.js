const express = require('express');
const cors = require('cors');

const app = express();

app.use(cors({ origin: process.env.CORS_ORIGIN }));

app.use(express.json());

app.get('/', (req, res) => {
    res.send('Bem-vindo ao Sistema de Gerenciamento de Aulas!');
});

app.use(require('./middlewares/errorMiddleware'));

module.exports = app;