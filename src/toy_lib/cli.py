import argparse
from .greeter import greet

def main():
    parser = argparse.ArgumentParser(description="Say hello from toy-lib")
    parser.add_argument("name", help="Name to greet")
    args = parser.parse_args()
    print(greet(args.name))

if __name__ == "__main__":
    main()
