#!/usr/bin/env python
# Copyright 2017 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Fake results processor for testing that just sums some things up.
"""

import fileinput
import re

richards = 0.0
deltablue = 0.0

for line in fileinput.input():
  match = re.match(r'^Richards\d: (.*)$', line)
  if match:
    richards += float(match.group(1))
  match = re.match(r'^DeltaBlue\d: (.*)$', line)
  if match:
    deltablue += float(match.group(1))

print('Richards: %f' % richards)
print('DeltaBlue: %f' % deltablue)
