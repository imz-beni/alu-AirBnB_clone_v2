#!/usr/bin/python3
""" """
import os
import json
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_save(self):
        """ Testing save with required fields """
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            from models.state import State
            from models.city import City
            from models.user import User
            from models.place import Place
            st = State(name="TestState")
            st.save()
            cy = City(name="TestCity", state_id=st.id)
            cy.save()
            us = User(email="r@r.com", password="pwd")
            us.save()
            pl = Place(city_id=cy.id, user_id=us.id, name="TestPlace")
            pl.save()
            i = self.value(
                place_id=pl.id, user_id=us.id, text="Great place")
        else:
            i = self.value()
        i.save()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            key = self.name + "." + i.id
            with open('file.json', 'r') as f:
                j = json.load(f)
                self.assertEqual(j[key], i.to_dict())

    def test_place_id(self):
        """ """
        new = self.value()
        new.place_id = "1234-abcd"
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        new.user_id = "1234-abcd"
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        new.text = "Great place"
        self.assertEqual(type(new.text), str)
