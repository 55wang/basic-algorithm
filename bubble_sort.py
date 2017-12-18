def main():
    list1 = [6, 4, 5, 1, 2, 8, 7, 3]
    print(bubble_sort(list1))


def bubble_sort(input_list):
    for i in range(1, len(input_list), 1):
        swap_flag = False
        for j in range(0, len(input_list)-i, 1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = swap(input_list[j], input_list[j+1])
                swap_flag = True

        if not swap_flag:
            break
    return input_list


def swap(left, right):
    return right, left


if __name__ == '__main__':
    main()
