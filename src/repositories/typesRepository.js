const typesModel = require('../models/typesModel');
const Sequelize = require('sequelize');

function insertType(newType) {
    return typesModel.create(newType);
}

function getTypes() {
    return typesModel.findAll();
}

function getTypeById(id) {
    return typesModel.findByPk(id);
}

async function updateType(id, newType) {
    const currentType = await getTypeById(id);

    if (newType.name && newType.name !== currentType.name) {
        currentType.name = newType.name;
    }

    if (newType.active && newType.active !== currentType.active) {
        currentType.active = newType.active;
    }
    
    await currentType.save();
    return currentType;
}

module.exports = {
    insertType,
    getTypes,
    getTypeById,
    updateType
}