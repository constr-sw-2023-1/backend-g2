const { DataTypes } = require('sequelize');

'use strict';

module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.createTable('subjects', {
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

    await queryInterface.addConstraint('subjects', {
      fields: ['lessonId'],
      type: 'foreign key',
      name: 'lessonId_fk',
      references: {
        table: 'lessons',
        fields: ['id'],
        key: 'id'
      }
    });

    await queryInterface.addConstraint('subjects', {
      fields: ['typeId'],
      type: 'foreign key',
      name: 'typeId_fk',
      references: {
        table: 'types',
        fields: ['id'],
        key: 'id'
      }
    });
  },

  async down(queryInterface, Sequelize) {
    await queryInterface.dropTable('subjects');
  }
};