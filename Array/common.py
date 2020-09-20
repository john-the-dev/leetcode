# Check if two lists carry same items without considering the order of the items.
def assert_list_noorder(list1, list2):
    list1.sort()
    list2.sort()
    assert(list1 == list2)

# Assert a sequence of calls return expected results.
def assert_call_sequence(context, calls, args, expected_outputs):
    assert(len(calls) == len(args) == len(expected_outputs[0]))
    assert(len(calls) >= 1)
    output = []
    # Default first item in calls is to create the class object of the solution and the remaining is to call methods of the object.
    solution = context[calls[0]](*args[0])
    output.append(None)
    for i in range(1,len(calls)):
        call = getattr(solution, calls[i])
        output.append(call(*args[i]))
    assert(output in expected_outputs)