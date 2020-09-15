def recurse(some_set):
    print("before", some_set)
    if not some_set:
        return
    some_set.remove(some_set[0])
    recurse(some_set.copy())
    print("after", some_set)

def test(some_set):
    print(some_set)
    recurse(some_set)

if __name__ == '__main__':
    test([1,2,3,4])