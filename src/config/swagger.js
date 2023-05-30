const swaggerJSDoc = require('swagger-jsdoc');

const options = {
  swaggerDefinition: {
    info: {
      title: 'Lessons - Grupo 2',
      version: '1.0',
    },
  },
  apis: ['**/*.js'], // Especifique aqui os caminhos para seus arquivos de rota
};
const swaggerSpec = swaggerJSDoc(options);
module.exports = swaggerSpec;