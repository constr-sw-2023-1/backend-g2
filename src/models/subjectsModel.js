const { Sequelize, DataTypes } = require('sequelize');
const database = require('../db');
const lessonsModel = require('../models/lessonsModel');
const typesModel = require('../models/typesModel');

const subjectsModel = database.define('subjects', {
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
    lessonId: {
        type: DataTypes.UUID,
        allowNull: false
    },
    typeId: {
        type: DataTypes.UUID,
        allowNull: false
    },
    createdAt: Sequelize.DATE,
    updatedAt: Sequelize.DATE
});

subjectsModel.belongsTo(lessonsModel, { foreignKey: 'lessonId' });
subjectsModel.belongsTo(typesModel, { foreignKey: 'typeId' });

module.exports = subjectsModel;