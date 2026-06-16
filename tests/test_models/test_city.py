#!/usr/bin/python3
""" """
import os
import json
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_save(self):
        """ Testing save with required fields """
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            from models import storage
            st = State(name="TestState")
            st.save()
            i = self.value(name="TestCity", state_id=st.id)
        else:
            i = self.value()
        i.save()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            key = self.name + "." + i.id
            with open('file.json', 'r') as f:
                j = json.load(f)
                self.assertEqual(j[key], i.to_dict())

    def test_state_id(self):
        """ """
        new = self.value()
        new.state_id = "1234-abcd"
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        new.name = "San Francisco"
        self.assertEqual(type(new.name), str)
