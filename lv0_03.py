from itertools import groupby
if __name__ == "__main__":
    for x, c in groupby(input()):
        print("(%d, %d)" % (len(list(c)), int(x)), end=' ')