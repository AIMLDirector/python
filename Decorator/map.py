import multiprocessing
import time

def sq(x):
    return x * x

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    input = [2,3,4,5]
    output = pool.map(sq, input)
    print("input: {}".format(input))
    print("output: {}".format(output))