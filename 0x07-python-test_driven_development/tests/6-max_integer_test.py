#!/usr/bin/python3
"""Test module for the 6-max_integer module"""

import unittest
from importlib import import_module

func = import_module("../6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer function."""

    def test_valid_arguments()

