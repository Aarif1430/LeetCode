class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def traverse(self):
        node = self
        while node is not None:
            print('value of node: %s'%node.val)
            node = node.next


class Solution(object):
    @staticmethod
    def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
        sum_vals = l1.val + l2.val
        carr = sum_vals//10
        n3 = ListNode(sum_vals % 10)
        l1 = l1.next
        l2 = l2.next
        l3 = n3
        while l1 or l2 is not None:
            sum_vals = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carr
            carr = sum_vals // 10
            l3.next = ListNode(sum_vals % 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            l3 = l3.next
        if carr > 0:
            l3.next = ListNode(carr)
        return n3


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(8)
    #n3 = ListNode(3)
    n1.next = n2
    #n2.next = n3

    n4 = ListNode(0)
    #n5 = ListNode(6)
    #n6 = ListNode(4)
    #n4.next = n5
    #n5.next = n6
    Solution().addTwoNumbers(n1,n4).traverse()
