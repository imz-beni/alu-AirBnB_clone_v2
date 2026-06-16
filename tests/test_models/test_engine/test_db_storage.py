#!/usr/bin/python3
""" Module for testing the database storage engine """
import os
import unittest
from models import storage
from models.state import State


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 'DBStorage only test')
class TestDBStorage(unittest.TestCase):
    """ Class to test the DBStorage engine """

    def test_all_returns_dict(self):
        """ all() returns a dictionary """
        self.assertIsInstance(storage.all(), dict)

    def test_new_save_delete(self):
        """ new(), save() and delete() update the database """
        state = State(name="Washington")
        storage.new(state)
        storage.save()
        key = 'State.' + state.id
        self.assertIn(key, storage.all(State))

        storage.delete(state)
        storage.save()
        self.assertNotIn(key, storage.all(State))

    def test_all_filter_by_class(self):
        """ all(cls) only returns instances of cls """
        state = State(name="Oregon")
        storage.new(state)
        storage.save()
        for obj in storage.all(State).values():
            self.assertIsInstance(obj, State)
        storage.delete(state)
        storage.save()
