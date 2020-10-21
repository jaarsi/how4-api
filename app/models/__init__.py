from peewee import MySQLDatabase

db = MySQLDatabase('how4-challenge', user='app', password='12345', host='127.0.0.1', port=3306)

from .produto import Produto