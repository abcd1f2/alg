#coding=utf-8

def binary_search(l, v):
    if len(l) <= 0:
        return None
    begin = 0
    end = len(l)
    middle = (end + begin)/2
    while begin < end:
        print "times"
        middle = (end + begin)/2
        if l[middle] == v:
            return middle
        elif v < l[middle]:
            end = middle - 1
        else:
            begin = middle + 1

if __name__ == '__main__':
    l = [100, 130, 180, 200, 253, 362, 458, 596, 687, 785, 852, 934]
    print binary_search(l, 100)
