const subjectsModel = require('../models/subjectsModel');
const Sequelize = require('sequelize');

function insertSubject(newSubject) {
    return subjectsModel.create(newSubject);
}

function getSubjects() {
    return subjectsModel.findAll();
}

function getSubjectById(id) {
    return subjectsModel.findByPk(id);
}

async function updateSubject(id, newSubject) {
    const currentSubject = await getSubjectById(id);

    if (newSubject.name && newSubject.name !== currentSubject.name) {
        currentSubject.name = newSubject.name;
    }

    if (newSubject.lessonId && newSubject.lessonId !== currentSubject.lessonId) {
        currentSubject.lessonId = newSubject.lessonId;
    }

    if (newSubject.typeId && newSubject.typeId !== currentSubject.typeId) {
        currentSubject.typeId = newSubject.typeId;
    }

    await currentSubject.save();
    return currentSubject;
}

function deleteSubject(id) {
    return subjectsModel.destroy({
        where: { id }
    });
}

module.exports = {
    insertSubject,
    getSubjects,
    getSubjectById,
    updateSubject,
    deleteSubject
}