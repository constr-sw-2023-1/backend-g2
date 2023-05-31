const lessonsRepository = require('../repositories/lessonsRepository');

async function insertLesson(req, res, next) {
    const { datetime, classroom }  = req.body;
    const lesson = await lessonsRepository.insertLesson({
        datetime,
        classroom
    });
    res.json(lesson);
}

async function getLessons(req, res, next) {
    const lessons = await lessonsRepository.getLessons();
    res.json(lessons);
}

async function getLessonById(req, res, next) {
    const id = req.params.id;
    const lesson = await lessonsRepository.getLessonById(id);
    res.json(lesson);
}

async function updateLesson(req, res, next) {
    const id = req.params.id;
    const { datetime, classroom }  = req.body;
    const lesson = await lessonsRepository.updateLesson(id, {
        datetime,
        classroom
    });
    res.json(lesson);
}

async function deleteLesson(req, res, next) {
    const id = req.params.id;
    const lesson = await lessonsRepository.updateLesson(id, {
        active: "false"
    });
    res.json(lesson);
}

module.exports = {
    insertLesson,
    getLessons,
    getLessonById,
    updateLesson,
    deleteLesson
}