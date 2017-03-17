#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django_bootstrap_calendar
------------

Tests for `django_bootstrap_calendar` modules module.
"""

import unittest
from datetime import datetime

from django.conf import settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_calsqlite.sql',
    }
}

settings.configure(
    DEBUG=True,
    TEMPLATE_DEBUG=True,
    DATABASES=DATABASES,
    DEFAULT_DB_ALIAS='default',
)

from GIP.django_bootstrap_calendar import event_serializer
from GIP.django_bootstrap_calendar import datetime_to_timestamp
from GIP.django_bootstrap_calendar import timestamp_to_datetime


class TestDjango_bootstrap_calendar(unittest.TestCase):

    def setUp(self):
        pass

    def test_convert_datetime_to_timestamp(self):
        value = '1376978400000'
        self.assertEquals(value, datetime_to_timestamp(
            datetime(2013, 8, 20, 8, 00)
        ), msg="testing")

    def test_convert_timestamp_to_datetime(self):
        value = datetime(2013, 8, 20, 8, 00)
        self.assertEquals(
            value,
            timestamp_to_datetime('1376978400000')
        )

    def test_no_calendar_event_response(self):
        print "testing serializer"

        self.assertEqual(
            '{"result": [], "success": 1}',
            event_serializer(None)
        )

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
