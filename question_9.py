my_list = [-3, 1, 4, 7, 8, 13]

target = 10

def two_sum(my_list, target):

    x = 0
    y = len(my_list)-1
    while x < y:
        if my_list[x] + my_list[y] == target:
            print(my_list[x], my_list[y])
            return True
        elif my_list[x] + my_list[y] < target:
            x += 1
        else:
            x -= 1
    return False

print(two_sum(my_list, target))
