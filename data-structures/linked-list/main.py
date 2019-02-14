from node import LinkedList

def isPresent(value, linked_list):
    if linked_list.find(value) is not None:
        print(str(value) + ' is present in find')
    else:
        print(str(value) + ' is not present in find')

def main():
    linked_list = LinkedList(2)
    elems = [32,321,21,55,78,32,1,43,665,31,32,11,21,21]
    for elem in elems:
        linked_list.insert(elem)

    print('Count: '+str(linked_list.count()))

    isPresent(2, linked_list)
    isPresent(4, linked_list)
    start = linked_list.get_values()
    linked_list.remove(2)
    for elem in elems:
        linked_list.remove(elem)
    end = linked_list.get_values()
    print(start)
    print(end)

if __name__ == '__main__':
    main()