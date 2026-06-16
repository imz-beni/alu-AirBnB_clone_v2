#!/usr/bin/python3
""" """
import os
import json
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_save(self):
        """ Testing save with required fields """
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            i = self.value(name="California")
        else:
            i = self.value()
        i.save()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            key = self.name + "." + i.id
            with open('file.json', 'r') as f:
                j = json.load(f)
                self.assertEqual(j[key], i.to_dict())

    def test_name3(self):
        """ """
        new = self.value()
        new.name = "California"
        self.assertEqual(type(new.name), str)
