const typesRepository = require('../repositories/typesRepository');

async function insertType(req, res, next) {
    const name  = req.body.name;
    const type = await typesRepository.insertType({
        name
    });
    res.json(type);
}

async function getTypes(req, res, next) {
    const types = await typesRepository.getTypes();
    res.json(types);
}

async function getTypeById(req, res, next) {
    const id = req.params.id;
    const type = await typesRepository.getTypeById(id);
    res.json(type);
}

async function updateType(req, res, next) {
    const id = req.params.id;
    const name = req.body.name;
    const type = await typesRepository.updateType(id, {
        name
    });
    res.json(type);
}

async function deleteType(req, res, next) {
    const id = req.params.id;
    const type = await typesRepository.updateType(id, {
        active: "false"
    });
    res.json(type);
}

module.exports = {
    insertType,
    getTypes,
    getTypeById,
    updateType,
    deleteType
}