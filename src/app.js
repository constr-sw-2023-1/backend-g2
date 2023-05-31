const express = require('express');
const cors = require('cors');
const swaggerUi = require('swagger-ui-express');
const swaggerSpec = require('../config/swagger');

const app = express();

app.use(cors({ origin: process.env.CORS_ORIGIN }));

app.use(express.json());

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec));

const typesRouter = require('./routes/typesRouter');
app.use('/lessons/types', typesRouter);

const subjectsRouter = require('./routes/subjectsRouter');
app.use('/lessons/subjects', subjectsRouter);

const lessonsRouter = require('./routes/lessonsRouter');
app.use('/lessons', lessonsRouter);

app.get('/', (req, res) => {
    res.send('Bem-vindo ao Sistema de Gerenciamento de Aulas!');
});

app.use(require('./middlewares/errorMiddleware'));

module.exports = app;