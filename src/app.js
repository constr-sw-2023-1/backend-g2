const express = require('express');
const cors = require('cors');
const typesController = require('./controllers/typesController');

const app = express();

app.use(cors({ origin: process.env.CORS_ORIGIN }));

app.use(express.json());

app.get('/lessons/types', typesController.getTypes);

app.get('/lessons/types/:id', typesController.getTypeById);

app.post('/lessons/types', typesController.insertType);

app.patch('/lessons/types/:id', typesController.updateType);

app.delete('/lessons/types/:id', typesController.deleteType);

app.get('/', (req, res) => {
    res.send('Bem-vindo ao Sistema de Gerenciamento de Aulas!');
});

app.use(require('./middlewares/errorMiddleware'));

module.exports = app;