const express = require('express');
const router = express.Router();
const subjectsController = require('../controllers/subjectsController');

router.get('/', subjectsController.getSubjects);

router.get('/:id', subjectsController.getSubjectById);

router.post('/', subjectsController.insertSubject);

router.patch('/:id', subjectsController.updateSubject);

router.delete('/:id', subjectsController.deleteSubject);

module.exports = router;