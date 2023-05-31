const lessonsRepository = require('../repositories/lessonsRepository');
const subjectsRepository = require('../repositories/subjectsRepository');

async function insertLesson(req, res, next) {
    const lesson = await lessonsRepository.insertLesson({ datetime: req.body.datetime, classroom: req.body.classroom });
    res.json(lesson);
}

async function getLessons(req, res, next) {
    const subjects = await subjectsRepository.getSubjects();

    const lessons = (await lessonsRepository.getLessons()).map(lesson => {
        var subs = subjects.map(subject => {
            if (subject.lessonId === lesson.id) {
                return {
                    id: subject.id,
                    name: subject.name,
                    type: subject.typeId
                }
            }
        })
        if (!subs[0]) {
            subs = [];
        }
        return {
            id: lesson.id,
            datetime: lesson.datetime,
            classroom: lesson.classroom,
            subjects: subs
        }
    });

    res.json(lessons);
}

async function getLessonById(req, res, next) {
    const lesson = await lessonsRepository.getLessonById(req.params.id);

    const subjects = (await subjectsRepository.getSubjectByLessonId(req.params.id)).map(subject => {
        return {
            id: subject.id,
            name: subject.name,
            type: subject.typeId
        }
    })

    if (lesson) {
        res.json({
            id: lesson.id,
            datetime: lesson.datetime,
            classroom: lesson.classroom,
            subjects: subjects
        });
    }
    else {
        res.json(null);
    }
}

async function updateLesson(req, res, next) {
    const lesson = await lessonsRepository.updateLesson(req.params.id, { datetime: req.body.datetime, classroom: req.body.classroom });
    res.json(lesson);
}

async function deleteLesson(req, res, next) {
    const lesson = await lessonsRepository.updateLesson(req.params.id, { active: "false" });
    res.json(lesson);
}

module.exports = {
    insertLesson,
    getLessons,
    getLessonById,
    updateLesson,
    deleteLesson
}