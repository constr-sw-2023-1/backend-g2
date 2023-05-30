const { DataTypes } = require('sequelize');

'use strict';

module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.createTable('types', {
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
    });
  },

  async down(queryInterface, Sequelize) {
    await queryInterface.dropTable('types');
  }
};