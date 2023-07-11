# https://www.codewars.com/kata/55d9f257d60c5fd98d00001b

# Write a RemoveDuplicates() function which takes a list sorted in increasing order and deletes any duplicate nodes
# from the list. Ideally, the list should only be traversed once. The head of the resulting list should be returned.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


chain = [
    Node("4"),
    Node("4"),
    Node("6"),
    Node("12"),
    Node("15"),
    Node("15"),
    Node("15"),
    Node("19"),
    Node("25"),
    Node("25"),
    Node("26")
]

for i, link in enumerate(chain[:-1]):
    link.next = chain[i + 1]

head = chain[0]
del chain


def remove_duplicates(head):
    original_head = head
    if not head:
        return None
    elif not head.next:
        return head
    else:
        while head.next:
            if head.data == head.next.data:
                head.next = head.next.next
            else:
                head = head.next
        return original_head


result = remove_duplicates(head)
while result is not None:
    print(result.data)
    result = result.next
else:
    print("None")
