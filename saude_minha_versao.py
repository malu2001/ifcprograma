from peewee import *

db = SqliteDatabase = ("saude3.db")


class BaseModelo(Model):
    class Meta():
        database = db