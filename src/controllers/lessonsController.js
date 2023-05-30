const lessonsRepository = require('../repositories/lessonsRepository');

async function insertLesson(req, res, next) {
    const { datetime, classroom }  = req.body;
    const type = await lessonsRepository.insertLesson({
        datetime,
        classroom
    });
    res.json(type);
}

async function getLessons(req, res, next) {
    const types = await lessonsRepository.getLessons();
    res.json(types);
}

async function getLessonById(req, res, next) {
    const id = req.params.id;
    const type = await lessonsRepository.getLessonById(id);
    res.json(type);
}

async function updateLesson(req, res, next) {
    const id = req.params.id;
    const { datetime, classroom }  = req.body;
    const type = await lessonsRepository.updateLesson(id, {
        datetime,
        classroom
    });
    res.json(type);
}

async function deleteLesson(req, res, next) {
    const id = req.params.id;
    const type = await lessonsRepository.updateLesson(id, {
        active: "false"
    });
    res.json(type);
}

module.exports = {
    insertLesson,
    getLessons,
    getLessonById,
    updateLesson,
    deleteLesson
}