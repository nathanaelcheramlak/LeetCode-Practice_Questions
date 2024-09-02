/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        var dummy = new ListNode();
        var current = dummy;
        
        while (head != null) {
            if (head.val != val) {
                current.next= head;
                current = current.next;
            }           
            head = head.next;
        }
        
        current.next = null; // Don't forget to terminate the list.
        
        return dummy.next;
    }
}