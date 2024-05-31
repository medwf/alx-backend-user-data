#!/usr/bin/env python3
"""
module personnel data.
"""
from typing import List
import re
import logging

PII_FIELDS = (
    "name", "email", "phone", "ssn", "password"
)


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """The log message obfuscated"""
    allFields = r"(?P<fields>{})=[^{}]*".format('|'.join(fields), separator)
    replace = r"\g<fields>={}".format(redaction)
    return re.sub(allFields, replace, message)


def get_logger() -> logging.Logger:
    """
    Methods that return an object of Logger
    """
    login = logging.getLogger("user_data")
    login.setLevel(logging.INFO)
    login.propagate = False
    login.addHandler(logging.StreamHandler().setFormatter(PII_FIELDS))
    return login


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """init instance"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filter values incoming log records"""
        message = super(RedactingFormatter, self).format(record)
        return filter_datum(
            self.fields, self.REDACTION, message, self.SEPARATOR
        )
