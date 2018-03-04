"""
Problem Statement:
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""

def div_by_zero():
 return 5/0


try:
 div_by_zero()
except ZeroDivisionError as e:
 print("Handle run-time 'div by 0'error:", e)


