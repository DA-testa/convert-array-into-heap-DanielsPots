# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    swaps = []
    for i in range (n // 2, -1, -1):
        heapify(data, swaps, i, n)
    return swaps
def heapify(data, swaps, i, n):
    min_index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child< n and data[left_child] < data[min_index]:
        min_index = left_child

    if right_child < n and data[right_child] < data[min_index]:
        min_index = right_child

    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        heapify(data, swaps, min_index, n)


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    input_type = input().strip()
    if input_type == "I":
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    elif input_type == "F":
        test_number = input().strip()
        with open(f"tests/{test_number}", "r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    else:
        print("Invalid input type")
        return

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
