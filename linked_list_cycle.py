class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        reference_store = {}
        while head:
            temp = head.next
            head.next = None
            if head in reference_store:
                return True
            else:
                reference_store[head] = head
            head.next = temp
            head = head.next
        return False
