from data_structures_and_algorithms.data_structures.linked_list.linked_list import LinkedList

def zip_lists(first_ll, second_ll):
    if not first_ll:
        return second_ll
    elif not second_ll:
        return first_ll
    result = LinkedList()
    current_of_first = first_ll.head
    current_of_second = second_ll.head
    while current_of_first:
        result.append(current_of_first.info)
        if current_of_second:
            result.append(current_of_second.info)
            current_of_second = current_of_second.next
        current_of_first = current_of_first.next
    while current_of_second:
        result.append(current_of_second.info)
        current_of_second = current_of_second
    return result

if __name__ == '__main__':
    first_ll = LinkedList([1, False, 3, 5])
    second_ll = LinkedList([7, 'Basma', 9, 11])
    third_ll = zip_lists(first_ll, second_ll)
    print(third_ll)