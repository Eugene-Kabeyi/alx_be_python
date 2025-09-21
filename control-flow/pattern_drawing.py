pattern = int(input("Enter the size of the pattern: "))
i = pattern

while pattern >= 0:
    k = 1
    while k <= i:
        print ("*", end="")
        k += 1
    print("")
    pattern -= 1