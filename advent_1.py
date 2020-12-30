with open('input.txt') as numbers
numbers = [int(n) for n in raw.split()]

def sum_2020(arr):
    for i in arr:
        a = 2020 - i
        if a in arr:
            return i * a


def sum_2020_2(arr, total):
    for i in range(len(arr)):
        a = total = arr[i]
        if total == 2020:
            b = sum_2020_2(arr[i+1:], a)
            if b is not None:
                return arr[i] * b
        else:
            if a in arr:
                return a * arr[i]




print(sum_2020(numbers))
print(sum_2020_2(numbers, 2020))
