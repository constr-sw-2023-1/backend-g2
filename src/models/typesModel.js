const { Sequelize, DataTypes } = require('sequelize');
const database = require('../db');

const TypesModel = database.define('types', {
    id: {
        type: DataTypes.UUID,
        defaultValue: DataTypes.UUIDV4,
        allowNull: false,
        primaryKey: true
    },
    name: {
        type: Sequelize.STRING,
        allowNull: false
    },
    active: {
        type: Sequelize.STRING,
        defaultValue: "true"
    },
    createdAt: Sequelize.DATE,
    updatedAt: Sequelize.DATE
})

module.exports = TypesModel;