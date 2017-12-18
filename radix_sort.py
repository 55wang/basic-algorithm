def main():
    list1 = [6, 4, 5, 1, 2, 8, 7, 3]
    print(radix_sort(list1))


def radix_sort(input_list):
    radix_group = 10
    placement = 1

    for d in range(1, len(str(max(input_list))) + 1):
        # declare and initialize buckets
        buckets = [list() for _ in range(radix_group)]

        for i in input_list:
            jth_digit = i // placement % radix_group
            buckets[jth_digit].append(i)

        input_index = 0
        for group in range(radix_group):
            bucket = buckets[group]
            for i in bucket:
                input_list[input_index] = i
                input_index += 1

        # move to next digit
        placement *= radix_group
    return input_list


if __name__ == '__main__':
    main()
