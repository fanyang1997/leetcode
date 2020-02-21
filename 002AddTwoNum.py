class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def myPrint(self):
        print(self.val)
        if self.next:
            self.next.myPrint()

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        val1, val2 = [l1.val], [l2.val]
        while l1.next:
            val1.append(l1.next.val)
            l1 = l1.next
        while l2.next:
            val2.append(l2.next.val)

        num1 = ''.join(str(i) for i in val1[::-1])
        num2 = ''.join(str(i) for i in val2[::-1])

        tmp = str(int(num1) + int(num2))[::-1]
        res = ListNode(int(tmp[0]))
        run_res = res
        for i in range(1, len(tmp)):
            run_res.next = ListNode(int(tmp[i]))
            run_res = run_res.next
        return res
if __name__ == "__main__":
    listnode = ListNode(1)
    listnode.next = ListNode(2)
    print(listnode.myPrint())