#!/usr/bin/env python
# Copyright 2014 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import unittest

from .pool import Pool

def Run(x):
  if x == 10:
    raise Exception("Expected exception triggered by test.")
  return x

class PoolTest(unittest.TestCase):
  def testNormal(self):
    results = set()
    pool = Pool(3)
    for result in pool.imap_unordered(Run, [[x] for x in range(0, 10)]):
      results.add(result.value)
    self.assertEqual(set(range(0, 10)), results)

  def testException(self):
    results = set()
    pool = Pool(3)
    with self.assertRaises(Exception):
      for result in pool.imap_unordered(Run, [[x] for x in range(0, 12)]):
        # Item 10 will not appear in results due to an internal exception.
        results.add(result.value)
    expect = set(range(0, 12))
    expect.remove(10)
    self.assertEqual(expect, results)

  def testAdd(self):
    results = set()
    pool = Pool(3)
    for result in pool.imap_unordered(Run, [[x] for x in range(0, 10)]):
      results.add(result.value)
      if result.value < 30:
        pool.add([result.value + 20])
    self.assertEqual(set(list(range(0, 10)) + list(range(20, 30)) + list(range(40, 50))),
                      results)
