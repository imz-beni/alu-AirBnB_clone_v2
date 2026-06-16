#!/usr/bin/python3
"""Unit tests for the console's create command with parameters"""
import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 'FileStorage only test')
class TestHBNBCommandCreate(unittest.TestCase):
    """Test create command with parameters (FileStorage)"""

    def tearDown(self):
        """Remove storage file at end of tests"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_create_with_string_param(self):
        """create with a quoted string parameter"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('create State name="California"')
        obj_id = output.getvalue().strip()
        key = 'State.' + obj_id
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key].name, 'California')

    def test_create_with_underscore_in_string(self):
        """underscores in a quoted string become spaces"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('create State name="New_York"')
        obj_id = output.getvalue().strip()
        key = 'State.' + obj_id
        self.assertEqual(storage.all()[key].name, 'New York')

    def test_create_with_float_and_int_params(self):
        """float and int params are cast correctly"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(
                'create Place city_id="0001" user_id="0001" '
                'number_rooms=4 latitude=37.773972')
        obj_id = output.getvalue().strip()
        key = 'Place.' + obj_id
        place = storage.all()[key]
        self.assertEqual(place.number_rooms, 4)
        self.assertIsInstance(place.number_rooms, int)
        self.assertEqual(place.latitude, 37.773972)
        self.assertIsInstance(place.latitude, float)

    def test_create_skips_invalid_param(self):
        """malformed params are skipped, not crashing"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('create State name="Texas" badparam')
        obj_id = output.getvalue().strip()
        key = 'State.' + obj_id
        self.assertIn(key, storage.all())
        self.assertFalse(hasattr(storage.all()[key], 'badparam'))
