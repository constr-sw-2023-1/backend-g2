const subjectsRepository = require('../repositories/subjectsRepository');

async function insertSubject(req, res, next) {
    const { name, lessonId, typeId }  = req.body;
    const subject = await subjectsRepository.insertSubject({
        name,
        lessonId,
        typeId
    });
    res.json(subject);
}

async function getSubjects(req, res, next) {
    const subjects = await subjectsRepository.getSubjects();
    res.json(subjects);
}

async function getSubjectById(req, res, next) {
    const id = req.params.id;
    const subject = await subjectsRepository.getSubjectById(id);
    res.json(subject);
}

async function updateSubject(req, res, next) {
    const id = req.params.id;
    const { name, lessonId, typeId }  = req.body;
    const subject = await subjectsRepository.updateSubject(id, {
        name,
        lessonId,
        typeId
    });
    res.json(subject);
}

async function deleteSubject(req, res, next) {
    const id = req.params.id;
    const subject = await subjectsRepository.deleteSubject(id);
    res.json(subject);
}

module.exports = {
    insertSubject,
    getSubjects,
    getSubjectById,
    updateSubject,
    deleteSubject
}