def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for item in my_list[:x]:
            print("{}".format(item), end="")
            counter += 1
        print()
    except:
        print("An error occurred, try again")
    return counter
