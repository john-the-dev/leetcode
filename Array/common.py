# Check if two lists carry same items without considering the order of the items.
def assert_list_noorder(list1, list2):
    list1.sort()
    list2.sort()
    assert(list1 == list2)

# Assert a sequence of calls return expected results.
def assert_call_sequence(context, calls, args, expected_outputs):
    solution,output = None,[]
    for i,callName in enumerate(calls):
        if callName == 'Solution':
            solution = context[callName](*args[i])
            output.append(None)
        else:
            call = getattr(solution, callName)
            output.append(call(*args[i]))
    assert(output in expected_outputs)