#!/usr/bin/python3
""" """
import os
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def setUp(self):
        """ """
        pass

    def test_save(self):
        """ Testing save with required fields """
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            i = self.value(email="test@test.com", password="pwd")
        else:
            i = self.value()
        i.save()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            import json
            key = self.name + "." + i.id
            with open('file.json', 'r') as f:
                j = json.load(f)
                self.assertEqual(j[key], i.to_dict())

    def test_first_name(self):
        """ """
        new = self.value()
        new.first_name = "John"
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        new.last_name = "Doe"
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        new.email = "a@b.com"
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        new.password = "secret"
        self.assertEqual(type(new.password), str)
