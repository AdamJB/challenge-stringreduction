#!/usr/bin/env python

def getData():
  numInput = int(raw_input().strip())

  llStrings = []
  for i in range(numInput):
    llStrings += [raw_input().strip()]

  return llStrings

def getNumResults(string):
  # Doesn't work .. :(
  # If  even # of each letter => 2 (ex:bac, bbaacc, cababc)
  # If uneven # of each letter => 1 (ex: bbaccc)
  # If all same letters => same # letter (cccccc)
  # Even # of leters with 2 of 2 char: ex: bbaa => bca => aa)
  numA = 0
  numB = 0
  numC = 0
  for s in string:
    if s == "a":
      numA += 1
    if s == "b":
      numB += 1
    if s == "c":
      numC += 1


  # If there's only 1 letter, return length of string
  if numA == len(string) or numB == len(string) or numC == len(string):
    return len(string)

  # If there are even number of letters for all 3 chars:
  if numA == numB and numB == numC:
    return 2

  if numA == numB and numC == 0 and (numA % 2 == 0):
    return 2
  if numA == numC and numB == 0 and (numA % 2 == 0):
    return 2
  if numB == numC and numA == 0 and (numB % 2 == 0):
    return 2

  return 1

def reduceString(string):
  # Create 3 stacks containing each character
  # We'll be pushing and poping to each stack.
  # Pop from the 2 smallest stacks, and push to the largest 1.
  aStack = []
  bStack = []
  cStack = []

  for s in string:
    if s == "a":
      aStack += 'a'
    if s == "b":
      bStack += 'b'
    if s == "c":
      cStack += 'c'

  while 1:
     # this ends when 1 of the stacks remain
    if not aStack and not bStack:
      return len(cStack)
    if not aStack and not cStack:
      return len(bStack)
    if not bStack and not cStack:
      return len(aStack)

    if len(aStack) >= len(bStack) and len(bStack) >= len(cStack) or \
     len(aStack) >= len(cStack) and len(cStack) >= len(bStack):
      if not bStack:
        cStack.pop(0)
        aStack.pop(0)
        bStack += 'b'
      elif not cStack:
        bStack.pop(0)
        aStack.pop(0)
        cStack += 'c'
      else:
        cStack.pop(0)
        bStack.pop(0)
        aStack += 'a'
    elif len(bStack) >= len(aStack) and len(aStack) >= len(cStack) or \
     len(bStack) >= len(cStack) and len(cStack) >= len(aStack):
      if not aStack:
        cStack.pop(0)
        bStack.pop(0)
        aStack += 'a'
      elif not cStack:
        bStack.pop(0)
        aStack.pop(0)
        cStack += 'c'
      else:
        bStack.pop(0)
        cStack.pop(0)
        aStack += 'b'
    elif len(cStack) >= len(aStack) and len(aStack) >= len(bStack) or \
     len(cStack) >= len(bStack) and len(bStack) >= len(aStack):
      if not aStack:
        cStack.pop(0)
        bStack.pop(0)
        aStack += 'a'
      elif not bStack:
        cStack.pop(0)
        aStack.pop(0)
        bStack += 'b'
      else:
        bStack.pop(0)
        aStack.pop(0)
        cStack += 'c'


strings = getData()

for s in strings:
  #print getNumResults(s)
  print reduceString(s)