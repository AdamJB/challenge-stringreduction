#!/usr/bin/env python

def getData():
  numInput = int(raw_input().strip())

  llStrings = []
  for i in range(numInput):
    llStrings += [raw_input().strip()]

  return llStrings

def reduceString(string):
  # Create 3 stacks containing each character
  # We'll be pushing and poping to each stack.
  # Pop from the 2 largest stacks, and push to the smallest 1.
  aStack = []
  bStack = []
  cStack = []

  for s in string:
    if s == "a":
      aStack += 'a'
    elif s == "b":
      bStack += 'b'
    elif s == "c":
      cStack += 'c'

  while 1:
    # this ends when 1 of the stacks remain
    if not aStack and not bStack:
      return len(cStack)
    if not aStack and not cStack:
      return len(bStack)
    if not bStack and not cStack:
      return len(aStack)

    if len(aStack) <= len(bStack) and len(bStack) <= len(cStack) or \
     len(aStack) <= len(cStack) and len(cStack) <= len(bStack):
      cStack.pop(0)
      bStack.pop(0)
      aStack += 'a'
    elif len(bStack) <= len(aStack) and len(aStack) <= len(cStack) or \
     len(bStack) <= len(cStack) and len(cStack) <= len(aStack):
      aStack.pop(0)
      cStack.pop(0)
      bStack += 'b'
    elif len(cStack) <= len(aStack) and len(aStack) <= len(bStack) or \
     len(cStack) <= len(bStack) and len(bStack) <= len(aStack):
      bStack.pop(0)
      aStack.pop(0)
      cStack += 'c'

strings = getData()

for s in strings:
  print reduceString(s)

"""

aaaacccccccbbbbbbbbb
aaaacccccccbbbbbbbbb



"""