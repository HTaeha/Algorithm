# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur_node = l1
        num1 = ""
        while True:
            num1 += str(cur_node.val)
            cur_node = cur_node.next
            if cur_node == None:
                break
        num1 = num1[::-1]

        cur_node = l2
        num2 = ""
        while True:
            num2 += str(cur_node.val)
            cur_node = cur_node.next
            if cur_node == None:
                break
        num2 = num2[::-1]

        num = int(num1) + int(num2)
        num = str(num)[::-1]
        result = ListNode(num[0])
        prev = result
        for i in range(1, len(num)):
            new_node = ListNode(num[i])
            prev.next = new_node
            prev = new_node
            
        return result
