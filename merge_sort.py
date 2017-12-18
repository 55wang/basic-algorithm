def main():
    list1 = [6, 4, 5, 1, 2, 8, 7, 3]
    print(merge_sort(list1))


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    mid = int(len(input_list) / 2)
    left = merge_sort(input_list[:mid])
    right = merge_sort(input_list[mid:])
    return merge(left, right)


if __name__ == '__main__':
    main()
