#!/usr/bin/env python
#
# Copyright (c) 2023 Katonic Pty Ltd. All rights reserved.
#
from katonic.version import get_version


__all__ = ["__version__"]

__version__: str = get_version()
