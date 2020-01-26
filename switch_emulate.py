

if __name__ == '__main__':
    num = int(input("Type number from 1 to 4"))

    switcher = {1: lambda: print("1 selected"),
                2: lambda: print("2 selected"),
                3: lambda: print("3 selected"),
                4: lambda: print("4 selected"),
                }

    switcher.get(num, lambda: print("Default value"))()
