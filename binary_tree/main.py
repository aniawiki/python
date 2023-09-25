import turtle
import argparse


DEFAULT_BRANCH_COLOR = "brown"
DEFAULT_LEAF_COLOR = "orange"


def parse_args():
    parser = argparse.ArgumentParser(description='Drawing a binary tree')
    parser.add_argument('-b', '--branch', type=str, default=DEFAULT_BRANCH_COLOR, help='Branch color')
    parser.add_argument('-l', '--leaf', type=str, default=DEFAULT_LEAF_COLOR, help='Leaf color')
    parser.add_argument('-s', '--size', type=int, default=70, help='Branch size')
    return parser.parse_args()


def init(branch, leaf, size):
    tu.screen.bgcolor("black")
    tu.pensize(2)
    tu.color(branch)

    tu.left(90)
    tu.backward(size)
    tu.speed(200)

    tree(size, branch, leaf)


def tree(i, branch, leaf):
    if i < 10:
        return
    else:
        tu.forward(i)
        tu.color(leaf)
        tu.circle(2)
        tu.color(branch)

        tu.left(30)
        tree(3*i/4, branch, leaf)
        tu.right(60)
        tree(3*i/4, branch, leaf)
        tu.left(30)
        tu.backward(i)


if __name__ == "__main__":
    tu = turtle.Turtle()
    args = parse_args()
    init(args.branch, args.leaf, args.size)
    turtle.done()
