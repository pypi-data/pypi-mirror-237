# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0

# DeepSpeed Team

import os

__version__ = "0.0.0"
try:
    from .version import __version__
except ImportError:
    pass


def library_path():
    return os.path.dirname(__file__)
