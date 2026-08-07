"""Sanity check that the package scaffold is importable.

This is intentionally the only test at this stage: the project is a
documented architecture scaffold (see README.md "Project status"), and
real behavioral tests will be added alongside each subsystem's
implementation (see docs/development.md).
"""

import aiu


def test_package_importable():
    assert isinstance(aiu.__version__, str)
