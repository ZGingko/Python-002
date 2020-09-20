def my_map(func, args):
    data_list = []
    for i in args:
        c = func(i)
        data_list.append(c)
    yield data_list


if __name__ == "__main__":
    list1 = [1,2,3,4,5]
    list2 = my_map(lambda x:x*x, list1)
    print(list(list2))
    