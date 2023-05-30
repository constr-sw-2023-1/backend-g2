const { DataTypes } = require('sequelize');

'use strict';

module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.createTable('lessons', {
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
    });
  },

  async down(queryInterface, Sequelize) {
    await queryInterface.dropTable('lessons');
  }
};