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
    """
    Method That returns:
        The log message obfuscated

    Args:
        fields <list[str]>: All fields to obfuscate
        redaction <str>: what the field will be obfuscated
        message <str>: The log line
        separator <str>: which character is separating

    Return:
        The log message obfuscated.
    """
    # for field in fields:
    allFields = r"(?P<fields>{})=[^{}]*".format('|'.join(fields), separator)
    replace = r"\g<fields>={}".format(redaction)
    return sub(allFields, replace, message)
