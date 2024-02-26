for _ in range(int(input())):
    x = int(input())

    count_set_bits = 0
    for i in range(x.bit_length()):
        if x & (1 << i) != 0:
            count_set_bits += 1

 
    i = 0
    while i < x.bit_length():
        if x & (1 << i) != 0:
            break
        i += 1

    if count_set_bits > 1:
        print(1 << i) 
    else:

        j = 0
        while j < x.bit_length():
            if x & (1 << j) == 0:
                break
            j += 1

        print((1 << i) ^ (1 << j))



