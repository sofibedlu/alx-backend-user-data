#!/usr/bin/env python3
"""
define filter-datum
"""
import re


def filter_datum(fields, redaction, message, separator):
    """returns the log messages obfuscated"""
    for field in fields:
        pattern = re.escape('{}='.format(field))
        message = re.sub('{}[^{}]+'.format(pattern, separator),
                         '{}={}'.format(field, redaction), message,
                         flags=re.IGNORECASE)
    return message
