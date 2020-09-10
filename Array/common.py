# Check if two lists carry same items without considering the order of the items.
def assert_list_noorder(list1, list2):
    list1.sort()
    list2.sort()
    assert(list1 == list2)