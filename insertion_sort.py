def main():
    list1 = [6, 4, 5, 1, 2, 8, 7, 3]
    print(insertion_sort(list1))


def insertion_sort(input_list):
    for i in range(1, len(input_list), 1):
        next_value = input_list[i]
        while i > 0 and input_list[i-1] > next_value:
            input_list[i] = input_list[i-1]
            i -= 1

        input_list[i] = next_value

    return input_list


if __name__ == '__main__':
    main()
