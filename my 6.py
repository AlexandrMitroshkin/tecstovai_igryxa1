def asd():
    a = input()
    print('a')


a = {"z":asd}
for i in a:
    print(i)
    a[i]()