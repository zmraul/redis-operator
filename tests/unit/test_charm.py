# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.

import unittest

from ops.testing import Harness

from charm import RedisOperatorCharm


class TestCharm(unittest.TestCase):
    def setUp(self):
        self.harness = Harness(RedisOperatorCharm)
        self.addCleanup(self.harness.cleanup)
        # self.harness.begin()

    def test_dummy(self):
        self.assertEqual(1, 1)
