const subjectsRepository = require('../repositories/subjectsRepository');

async function insertSubject(req, res, next) {
    const subject = await subjectsRepository.insertSubject({ name: req.body.name, lessonId: req.body.lessonId, typeId: req.body.typeId });
    res.json(subject);
}

async function getSubjects(req, res, next) {
    const subjects = await subjectsRepository.getSubjects();
    res.json(subjects);
}

async function getSubjectById(req, res, next) {
    const subject = await subjectsRepository.getSubjectById(req.params.id);
    res.json(subject);
}

async function updateSubject(req, res, next) {
    const subject = await subjectsRepository.updateSubject(req.params.id, { name: req.body.name, lessonId: req.body.lessonId, typeId: req.body.typeId });
    res.json(subject);
}

async function deleteSubject(req, res, next) {
    const subject = await subjectsRepository.deleteSubject(req.params.id);
    res.json(subject);
}

module.exports = {
    insertSubject,
    getSubjects,
    getSubjectById,
    updateSubject,
    deleteSubject
}