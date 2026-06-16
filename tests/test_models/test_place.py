#!/usr/bin/python3
""" """
import os
import json
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_save(self):
        """ Testing save with required fields """
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            from models.state import State
            from models.city import City
            from models.user import User
            st = State(name="TestState")
            st.save()
            cy = City(name="TestCity", state_id=st.id)
            cy.save()
            us = User(email="p@p.com", password="pwd")
            us.save()
            i = self.value(city_id=cy.id, user_id=us.id, name="TestPlace")
        else:
            i = self.value()
        i.save()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            key = self.name + "." + i.id
            with open('file.json', 'r') as f:
                j = json.load(f)
                self.assertEqual(j[key], i.to_dict())

    def test_city_id(self):
        """ """
        new = self.value()
        new.city_id = "1234-abcd"
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        new.user_id = "1234-abcd"
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        new.name = "House"
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        new.description = "Nice place"
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        new.number_rooms = 0
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        new.number_bathrooms = 0
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        new.max_guest = 0
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        new.price_by_night = 0
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        new.latitude = 0.0
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        new.longitude = 0.0
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
