#! /usr/bin/python3
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
if sys.argv[3] == "+":
    print(a + b)
elif sys.argv[3] == "-":
    print(a - b)
elif sys.argv[3] == "*":
    print(a * b)
elif sys.argv[3] == "/":
    print(a / b)
