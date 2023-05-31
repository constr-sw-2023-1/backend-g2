const express = require('express');
const router = express.Router();
const typesController = require('../controllers/typesController');

router.get('/', typesController.getTypes);

router.get('/:id', typesController.getTypeById);

router.post('/', typesController.insertType);

router.patch('/:id', typesController.updateType);

router.delete('/:id', typesController.deleteType);

module.exports = router;