#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i, new = 0, []
    while i < list_length:
        try:
            new.append(my_list_1[i] / my_list_2[i])
            i += 1
            continue
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            pass
        new.append(0)
        i += 1
    return new
