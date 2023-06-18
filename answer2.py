class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode()
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        _sum = x + y + carry
        carry = _sum // 10
        current.next = ListNode(_sum % 10)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next


# Test Case 1
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result1 = addTwoNumbers(l1, l2)

while result1:
    print(result1.val, end=" ")
    result1 = result1.next


print()

# Test Case 2
l3 = ListNode(0)
l4 = ListNode(0)

result2 = addTwoNumbers(l3, l4)

while result2:
    print(result2.val, end=" ")
    result2 = result2.next

print()

# Test Case 3
l5 = ListNode(9)
l5.next = ListNode(9)
l5.next.next = ListNode(9)
l5.next.next.next = ListNode(9)
l5.next.next.next.next = ListNode(9)
l5.next.next.next.next.next = ListNode(9)
l5.next.next.next.next.next.next = ListNode(9)

l6 = ListNode(9)
l6.next = ListNode(9)
l6.next.next = ListNode(9)
l6.next.next.next = ListNode(9)

result3 = addTwoNumbers(l5, l6)

while result3:
    print(result3.val, end=" ")
    result3 = result3.next
