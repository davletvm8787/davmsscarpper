"""

This module contains the set of Scrapers' exceptions.
"""


class KimetaException(Exception):
    def __init__(self, message=None):
        super().__init__(message or "An error occurred with Kimeta")


class IndeedException(Exception):
    def __init__(self, message=None):
        super().__init__(message or "An error occurred with Indeed")


class StepstoneException(Exception):
    def __init__(self, message=None):
        super().__init__(message or "An error occurred with Stepstone")

