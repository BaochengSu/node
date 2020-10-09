# -*- coding: utf-8 -*-
"""
    markupsafe._compat
    ~~~~~~~~~~~~~~~~~~

    Compatibility module for different Python versions.

    :copyright: (c) 2013 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
import sys

PY2 = sys.version_info[0] == 2

if not PY2:
    text_type = str
    string_types = (str,)
    chr = chr
    int_types = (int,)
else:
    text_type = str
    string_types = (str, str)
    chr = chr
    int_types = (int, int)
