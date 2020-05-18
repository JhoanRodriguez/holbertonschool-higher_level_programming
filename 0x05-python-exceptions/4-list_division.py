#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = [0 for item in range(list_length)]
    for item in range(0, list_length):
        try:
            result[item] = (my_list_1[item]) / (my_list_2[item])
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            pass
    return result
