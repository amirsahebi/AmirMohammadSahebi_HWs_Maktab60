#! /usr/bin/python3
import argparse
parser=argparse.ArgumentParser(description="THIS IS CALCULATOR")
parser.add_argument("number1",help="get the first number for a math operation",type=float)
parser.add_argument("number2",help="get the second number for a math operation",type=float)
group=parser.add_mutually_exclusive_group()
parser.add_argument("-o","--operation",action='store_true',help="use to define the selected math operation")
args=parser.parse_args()
if args.operation=='+':
    print(args.number1+args.number2)
if args.operation=='-':
    print(args.number1-args.number2)
if args.operation=='/':
    print(args.number1/args.number2)
if args.operation=='*':
    print(args.number1*args.number2)



