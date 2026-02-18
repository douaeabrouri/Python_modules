def ft_count_harvest_iterative():
    count = int(input("Days until harvest: "))
    i = 1
    while count >= i:
        print("Day", i)
        i += 1
    print("Harvest time!")
