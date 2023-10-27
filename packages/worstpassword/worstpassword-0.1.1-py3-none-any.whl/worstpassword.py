import argparse
import random


class WorstPassword:
    __characters__ = ('0', 'O', 'l', '1', 'I', '|', '5', 'S')

    def __init__(self, length=8):
        self.length = length
        self.password = []

    def generate(self):
        for char in range(self.length):
            self.password.append(random.choice(WorstPassword.__characters__))
        return ''.join(self.password)


def main():
    parser = argparse.ArgumentParser(description='Generating a worst passwords.')
    parser.add_argument('-l', '--length', type=int, default=10, help='Length of password. Default: 10')
    args = parser.parse_args()
    wp = WorstPassword(args.length)
    print(wp.generate())


if __name__ == '__main__':
    main()
