#!/usr/bin/python
#by v0id

# -*- coding: utf-8 -*-

import sys
import re

pattern = sys.argv[1]

regexp = re.compile(pattern)

for line in sys.stdin:
 result = regexp.search(line)
 if result:
  sys.stdout.write(line)