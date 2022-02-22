#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.

"""Charmed Redis Operator.

This is the code that charms the Redis service
"""

import logging

from ops.charm import CharmBase
from ops.main import main

logger = logging.getLogger(__name__)


class RedisOperatorCharm(CharmBase):
    """Charm the service."""

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.framework.on.install, self._on_install)

    def _on_install(self, event):
        """Handle the install event.

        Update apt cache and install Redis
        """
        pass


if __name__ == "__main__":
    main(RedisOperatorCharm)
