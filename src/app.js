const express = require('express');
const cors = require('cors');
const lessonsController = require('./controllers/lessonsController');
const typesController = require('./controllers/typesController');

const app = express();

app.use(cors({ origin: process.env.CORS_ORIGIN }));

app.use(express.json());

app.get('/lessons', lessonsController.getLessons);

app.get('/lessons/:id', lessonsController.getLessonById);

app.post('/lessons', lessonsController.insertLesson);

app.patch('/lessons/:id', lessonsController.updateLesson);

app.delete('/lessons/:id', lessonsController.deleteLesson);

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