
# We can improve this O(n) performance by removing the while loop 
# operations and condensing it into the for loop


def removeKthLinkedListNode(head, k):
    # Use two pointers while we traverse the list
    temp = head
    temp2 = head

    # Iterate from the 0 to the kth node
    for i in range(0, k):
        # Move our second pointer next for each element
        temp2 = temp2.next
        # If we find the end, we assign head to next
        if temp2 == None:
            head = head.next
            return head
    # While we move our second pointer and its not None
    while temp2.next != None:
        # We move our second pointer
        temp2 = temp2.next
        # We move our first pointer+
        temp = temp.next
    # Our first pointer's next skips a node
    temp.next = temp.next.next
    # Return the kth node which is our head
    return head