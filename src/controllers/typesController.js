const typesRepository = require('../repositories/typesRepository');

async function insertType(req, res, next) {
    const type = await typesRepository.insertType({ name: req.body.name });
    res.json(type);
}

async function getTypes(req, res, next) {
    const types = await typesRepository.getTypes();
    res.json(types);
}

async function getTypeById(req, res, next) {
    const type = await typesRepository.getTypeById(req.params.id);
    res.json(type);
}

async function updateType(req, res, next) {
    const type = await typesRepository.updateType(req.params.id, { name: req.body.name });
    res.json(type);
}

async function deleteType(req, res, next) {
    const type = await typesRepository.updateType(req.params.id, { active: "false" });
    res.json(type);
}

module.exports = {
    insertType,
    getTypes,
    getTypeById,
    updateType,
    deleteType
}