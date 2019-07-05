"""
Given arrival and departure times of all trains that reach a railway station, find the minimum number of platforms
required for the railway station so that no train waits.

Input:  arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}
        dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
There are at-most three trains at a time (time between 11:00 to 11:20)

GFG: https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
"""


def find_platform(arrival, departed, n):
    arrival_array = sorted(arrival)
    departed_array = sorted(departed)
    i = 1
    j = 0
    result = 1
    platform = 1

    while i < n and j < n:
        if arrival_array[i] < departed_array[j]:
            platform += 1
            i += 1

            if platform > result:
                result = platform

        else:
            platform -= 1
            j += 1

    return result


if __name__ == '__main__':
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    arrival_len = len(arr)

    print("Minimum Number of Platforms Required = ",
          find_platform(arr, dep, arrival_len))
