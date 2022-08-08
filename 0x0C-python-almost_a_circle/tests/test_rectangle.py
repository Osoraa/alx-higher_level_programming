#!/usr/bin/python3
"""Test document for the rectangle module."""

from unittest import TestCase
from models.rectangle import Rectangle


class TestRectangle(TestCase):
    """Tests the Rectangle class."""

    def test_rectangle(self):
        """"""

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual((r1.x, r1.y, r1.width, r1.height, r1.id), (0, 0, 10, 2, 1))

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual((r2.x, r2.y, r2.width, r2.height, r2.id), (0, 0, 2, 10, 2))

        r3 = Rectangle(10, 2, 7, 9, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual((r3.x, r3.y, r3.width, r3.height, r3.id), (7, 9, 10, 2, 12))
