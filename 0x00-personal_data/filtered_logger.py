#!/usr/bin/env python3
"""
implement logging
"""
import os
import re
import logging
from typing import List
import mysql.connector


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log messages obfuscated"""
    for field in fields:
        pattern = re.escape('{}='.format(field))
        message = re.sub('{}[^{}]+'.format(pattern, separator),
                         '{}={}'.format(field, redaction), message,
                         flags=re.IGNORECASE)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """intialize"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """return customized radicated log messages"""
        formated = filter_datum(self.fields, self.REDACTION,
                                record.msg, self.SEPARATOR)
        record.msg = formated
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """returns logging.Logger object"""

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    redacting_formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(redacting_formatter)
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """returns a connector to the database"""

    user = os.getenv('PERSONAL_DATA_DB_USERNAME') or "root"
    passwd = os.getenv('PERSONAL_DATA_DB_PASSWORD') or ""
    host = os.getenv('PERSONAL_DATA_DB_HOST') or "localhost"
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')
    connection = mysql.connector.connect(host=host,
                                         user=user,
                                         password=passwd,
                                         database=db_name)

    return connection
