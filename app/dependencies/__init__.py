"""This is the dependencies module, this folder should contain all the dependencies
"""


from fastapi import FastAPI

from . import cors, database


def init_app(app: FastAPI):
    cors.init_app(app)
    database.init_app(app)
