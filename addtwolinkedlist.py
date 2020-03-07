## Given two numbers as a linked list stored in reverse order, 
## add the two numbers and return them as a linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Takes a linked list and returns it as a list.
def returnList(li):
    results = []
    while li is not None:
        results.append(str(li.val))
        li = li.next
    return results

# The linked lists are converted to lists, reversed, converted to ints,
# added together, converted back into a list, and finally back into a reversed linked list.
def addTwoNumbers(l1, l2):
    listOne = returnList(l1)
    listTwo = returnList(l2)
    listOne.reverse()
    listTwo.reverse()

    result = int("".join(listOne)) + int("".join(listTwo))
    result = list(str(result))

    l3 = ListNode(result[-1])
    l3.next = ListNode(result[-2])
    l3.next.next = ListNode(result[-3])
        
    return l3

def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    l3 = addTwoNumbers(l1, l2)
    print(returnList(l3))

main()