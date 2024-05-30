#!/usr/bin/env python3
"""
module personnel data.
"""
from typing import List
from re import sub


def filter_datum(
        fields: List[str], redaction: str,
        message: str, separator: str
) -> str:
    """The log message obfuscated"""
    allFields = r"(?P<fields>{})=[^{}]*".format('|'.join(fields), separator)
    replace = r"\g<fields>={}".format(redaction)
    return sub(allFields, replace, message)
