#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, div, sub, mul
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    n1, op, n2 = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])

    def error(n, nn):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    def switch(op):
        switcher = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div,
        }
        return switcher.get(op, error)
    r = switch(op)(n1, n2)
    print(f"{n1} {op} {n2} = {r}")
