'''
When given a date, calculates the age between the current dat and the given date.
'''
'''
Testing out Git Stuff
'''


def main():
    test_list = [20, 50, 12, 6, 0, 8]
    maxmin(test_list)


def maxmin(input_list):
    if len(input_list) == 0:
        print(input_list)
        return
    max = input_list[0]
    min = input_list[0]
    for element in input_list:
        if element < min:
            min = element
        if element > max:
            max = element
    print([min, max])


if __name__ == '__main__':
    main()
