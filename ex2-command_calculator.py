"""
dictionary of functions contains four simple separate functions that get two numbers and use them in a simple
calculation.
• add – Adds the two numbers and prints the result.
• multiply – Multiplies the two numbers and prints the result.
• subtract – Substracts the second number from the first and prints the result.
• divide – Divides the first number by the second number and prints the result.

Probably, the user will only want to use one function at a time. She will probably want a simple, intuitive explanation
on how to run your script by giving an “-h” argument. Also, you may want to add more features: For example, if the user
wants to, she will be able to ask the calculator to print a good morning message by giving a “-w” argument.
"""
import argparse

parser = argparse.ArgumentParser(description='claculate:  a  +|*|-|/  b')
parser.add_argument('operator', choices=['add', 'multiply', 'subtract', 'divide'], metavar='',
                        help="operator ['add', 'multiply', 'subtract', 'divide']")
parser.add_argument('a', type=float, metavar='', help='first float argument a')
parser.add_argument('b', type=float, metavar='', help='second float argument b')
parser.add_argument('-w', '--welcome', action='store_true', help='prints: "good morning love :)"')
args = parser.parse_args()


function_dict = {'add': lambda a, b: a + b, 'multiply': lambda a, b: a * b, 'subtract': lambda a, b: a - b,
                 'divide': lambda a, b: a / b if b!=0 else print('Error: divisor cannot be zero.')}


def main():
    output = float()
    try:
        output = function_dict[args.operator](args.a, args.b)
    except:
        print('it is not you it is us.')

    if args.welcome:
        print('Good morning love :)')
    if output:
        print(output)


if __name__ == '__main__':
    main()
