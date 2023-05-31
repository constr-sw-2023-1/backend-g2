const lessonsModel = require('../models/lessonsModel');
const Sequelize = require('sequelize');

function insertLesson(newLesson) {
    return lessonsModel.create(newLesson);
}

function getLessons() {
    return lessonsModel.findAll({ where: { active: "true" } });
}

function getLessonById(id) {
    return lessonsModel.findOne({ where: { id: id, active: "true" } });
}

async function updateLesson(id, newLesson) {
    const currentLesson = await getLessonById(id);

    if (newLesson.datetime && newLesson.datetime !== currentLesson.datetime) {
        currentLesson.datetime = newLesson.datetime;
    }

    if (newLesson.classroom && newLesson.classroom !== currentLesson.classroom) {
        currentLesson.classroom = newLesson.classroom;
    }

    if (newLesson.active && newLesson.active !== currentLesson.active) {
        currentLesson.active = newLesson.active;
    }

    await currentLesson.save();
    return currentLesson;
}

module.exports = {
    insertLesson,
    getLessons,
    getLessonById,
    updateLesson
}