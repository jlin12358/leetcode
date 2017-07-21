# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # More elegant solution
        carry = 0
        head = ListNode(0)
        new_list = head
        while l1 != None or l2 != None:
            if l1 == None:
                x = 0
            else:
                x = l1.val
                l1 = l1.next
            if l2 == None:
                y = 0
            else:
                y = l2.val
                l2 = l2.next
            temp = x + y + carry
            carry = temp/10
            new_list.next = ListNode(temp%10)
            new_list = new_list.next
        
        if carry == 1:
            new_list.next = ListNode(1)
        return head.next
    
        '''
        # My Solution
        temp = l1.val + l2.val        
        new_list = ListNode(temp%10)
        carry = temp / 10            
        head = new_list
        l1 = l1.next
        l2 = l2.next
        
        while l1 != None or l2 != None:
            
            if l1 == None:
                x = 0
            else:
                x = l1.val
                l1 = l1.next
            
            if l2 == None:
                y = 0
            else:
                y = l2.val
                l2 = l2.next
            
            temp = carry + x + y
            carry = temp / 10
            new_list.next = ListNode(temp%10)
            new_list = new_list.next
            
        if carry == 1:
            new_list.next = ListNode(1)
        
        return head
