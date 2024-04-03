#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    for i in range(list_length):
        try:
            my_result = my_list_1[i] / my_list_2[i]
        except (TypeError):
            print("wrong type")
            my_result = 0
        except (IndexError):
            print("out of range")
            my_result = 0
        except (ZeroDivisionError):
            print("division by 0")
            my_result = 0
        finally:
            my_list.append(my_result)
    return (my_list)
