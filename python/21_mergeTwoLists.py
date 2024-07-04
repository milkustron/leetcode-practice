class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(list1, list2):
        result = ListNode()
        current = result
        
        while list1 is not None or list2 is not None:
            if list1 is None:
                while list2 is not None:
                    current.next = ListNode(list2.val)
                    list2 = list2.next
                    current = current.next
                break
            if list2 is None:
                while list1 is not None:
                    current.next = ListNode(list1.val)
                    list1 = list1.next
                    current = current.next
                break
                
            if list1.val < list2.val:
                current.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                list2 = list2.next
            current = current.next
        
        return result.next 