const { Sequelize, DataTypes } = require('sequelize');
const database = require('../db');

const LessonsModel = database.define('lessons', {
    id: {
        type: DataTypes.UUID,
        defaultValue: DataTypes.UUIDV4,
        allowNull: false,
        primaryKey: true
    },
    datetime: {
        type: Sequelize.DATE,
        allowNull: false
    },
    classroom: {
        type: Sequelize.INTEGER,
        allowNull: false
    },
    active: {
        type: Sequelize.STRING,
        defaultValue: "true"
    },
    createdAt: Sequelize.DATE,
    updatedAt: Sequelize.DATE
})

module.exports = LessonsModel;