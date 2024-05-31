#!/usr/bin/env python3
"""
module personnel data.
"""
from typing import List
import re
import os
import logging
import mysql.connector

PII_FIELDS = (
    "name", "email", "phone", "ssn", "password"
)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """create a connector to database"""
    USER_NAME = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    PASSWORD = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    HOST = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    DATABASE = os.getenv('PERSONAL_DATA_DB_NAME', '')

    connector = mysql.connector.connect(
        host=HOST, port=3306, user=USER_NAME,
        password=PASSWORD, database=DATABASE
    )

    return connector


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
