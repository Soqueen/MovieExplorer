# movieExplorerDB.py
# Interface Movie Explorer with the MongoDB database
# Based on Sok Heng's code
# February 2017

import pymongo
from pymongo import MongoClient
import sys


class Agent:
    host = '104.131.51.38'
    port = 27017

    def __init__(self, dbname, host=host, port=port):
        try:
            self._conn = MongoClient(host, port)
            print('connected to DB')
        except pymongo.errors.ConnectionFailure as e:
            print(e)
            sys.exit(-1)

        try:
            self._db = self._conn[dbname]
        except pymongo.errors.InvalidName as e:
            print(e)
            sys.exit(-1)

    def add_user();

    def add_rating();

    def get_user_name();

    def get_user_email();

    def get_user_rating();
