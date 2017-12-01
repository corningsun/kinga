#!/usr/bin/env python
# -*- coding:utf-8 -*-

from peewee import *

mysql_db = MySQLDatabase('kinga', host='127.0.0.1', user='root', password='19890720')


class BaseModel(Model):
    """A base model that will use our MySQL database"""

    class Meta:
        database = mysql_db


class Demo(BaseModel):
    id = PrimaryKeyField()
    string = CharField()


class Message(BaseModel):
    id = PrimaryKeyField()
    member = CharField()


def create_models():
    # Demo.create_table()
    Message.create_table()


if __name__ == '__main__':
    create_models()
