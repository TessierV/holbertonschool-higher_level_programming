def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except IndexError:
            new_list.append(0)
            print("wrong type")
        except TypeError:
            new_list.append(0)
            print("wrong type")
        except ZeroDivisionError:
            new_list.append(0)
            print("wrong type")
        finally:
            pass
    return new_list
