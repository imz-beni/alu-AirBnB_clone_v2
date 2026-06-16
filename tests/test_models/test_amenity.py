#!/usr/bin/python3
""" """
import os
import json
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_save(self):
        """ Testing save with required fields """
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            i = self.value(name="Wifi")
        else:
            i = self.value()
        i.save()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            key = self.name + "." + i.id
            with open('file.json', 'r') as f:
                j = json.load(f)
                self.assertEqual(j[key], i.to_dict())

    def test_name2(self):
        """ """
        new = self.value()
        new.name = "Wifi"
        self.assertEqual(type(new.name), str)
