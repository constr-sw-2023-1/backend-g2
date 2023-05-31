const express = require('express');
const router = express.Router();
const lessonsController = require('../controllers/lessonsController');

router.get('/', lessonsController.getLessons);

router.get('/:id', lessonsController.getLessonById);

router.post('/', lessonsController.insertLesson);

router.patch('/:id', lessonsController.updateLesson);

router.delete('/:id', lessonsController.deleteLesson);

module.exports = router;