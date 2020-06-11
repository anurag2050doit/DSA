#!/bin/python3

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    input_list = [0] * 5
    best = 0
    for query in queries:
        start_pos = query[0] - 1
        end_post = query[1]
        for x in range(start_pos, end_post):
            input_list[x] = input_list[x] + query[2]

    return max(input_list)


if __name__ == '__main__':
    arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]])
