def returnPositive(*arg):
    print("Positive parameters: ")
    for value in arg:
        if value > 0:
            print(value)

returnPositive(1,-2,3,-4,5,-7)


