def bubble_sort(data):
    for _ in range(len(data)):
        for index in range(0, len(data) - 1):
            if data[index] > data[index + 1]:
                data[index], data[index + 1] = data[index + 1], data[index]
                # swap the positions if first number is higher than the second
            else:
                pass  # go ahead and check the next pair

    print data


data = [14, 46, 43, 27, 57, 41, 45, 21, 70]
bubble_sort(data)
