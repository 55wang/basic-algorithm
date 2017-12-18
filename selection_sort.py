def main():
    list1 = [6, 4, 5, 1, 2, 8, 7, 3]
    print(selection_sort(list1))


def selection_sort(input_list):

    for i in range(0, len(input_list), 1):
        min_index = i
        for j in range(i+1, len(input_list), 1):
            if input_list[j] < input_list[min_index]:
                min_index = j

        input_list[min_index], input_list[i] = input_list[i], input_list[min_index]

    return input_list


if __name__ == '__main__':
    main()
