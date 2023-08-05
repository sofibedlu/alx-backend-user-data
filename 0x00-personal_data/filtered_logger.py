#!/usr/bin/env python3
"""
define filter-datum
"""
import re
import logging
from typing import List, Sequence


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

    def __init__(self, fields: Sequence[str]):
        """intialize"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """return customized radicated log messages"""
        formated = filter_datum(self.fields, self.REDACTION,
                                record.msg, self.SEPARATOR)
        record.msg = formated
        return super(RedactingFormatter, self).format(record)
