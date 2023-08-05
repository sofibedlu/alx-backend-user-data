#!/usr/bin/env python3
"""
define filter-datum
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log messages obfuscated"""
    for field in fields:
        pattern = re.escape('{}='.format(field))
        message = re.sub('{}[^{}]+'.format(pattern, separator),
                         '{}={}'.format(field, redaction), message,
                         flags=re.IGNORECASE)
    return message
