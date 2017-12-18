def main():
    list1 = [6, 4, 5, 1, 2, 8, 7, 3]
    print(quick_sort(list1))


def quick_sort(input_list):
    return quick_sort_helper(input_list, 0, len(input_list)-1)


def quick_sort_helper(input_list, start, end):
    if start >= end:
        return input_list

    input_list, pivot_index = partition(input_list, start, end)
    input_list = quick_sort_helper(input_list, start, pivot_index-1)
    input_list = quick_sort_helper(input_list, pivot_index+1, end)
    return input_list


def partition(input_list, start, end):
    pivot = input_list[start]
    last_s1 = start
    first_unknown = start + 1

    while first_unknown <= end:
        if input_list[first_unknown] < pivot:
            input_list[first_unknown], input_list[last_s1+1] = input_list[last_s1+1], input_list[first_unknown]
            last_s1 += 1
            first_unknown += 1
        else:
            first_unknown += 1

    input_list[start], input_list[last_s1] = input_list[last_s1], input_list[start]
    # print(input_list[start:], input_list[last_s1], pivot)
    return input_list, last_s1


if __name__ == '__main__':
    main()
