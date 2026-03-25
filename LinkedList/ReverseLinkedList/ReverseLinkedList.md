# 🔄 Reverse a Singly Linked List

> **Level:** Beginner → Intermediate
> **Concepts:** Linked List · Pointers · In-place Reversal
> **Language:** Python

---

## 📌 Problem Description

You are given the **head** of a singly linked list.
Your task is to **reverse the list** and return the new head.

---

### 🧾 Example

```text
Input:  1 → 2 → 3 → None  
Output: 3 → 2 → 1 → None
```

---

## 🧠 Key Idea

A linked list cannot be reversed like an array.
Instead, we **change the direction of links (pointers)** between nodes.

👉 Every node should point to its **previous node** instead of the next.

---

## 🧱 Node Structure

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

## 💡 Approach (Iterative)

We use **three pointers**:

* `prev` → stores previous node
* `curr` → current node
* `nextNode` → temporarily stores next node

---

## 🔧 Solution Code

```python
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nextNode = curr.next   # store next node
            curr.next = prev       # reverse link
            prev = curr            # move prev forward
            curr = nextNode        # move curr forward

        return prev
```

---

## 🔍 Step-by-Step Explanation

Initial state:

```text
prev = None
curr = 1 → 2 → 3
```

---

### 🔁 Iteration 1

* Save next → `2`
* Reverse → `1 → None`
* Move pointers

```text
prev = 1
curr = 2 → 3
```

---

### 🔁 Iteration 2

* Save next → `3`
* Reverse → `2 → 1`
* Move pointers

```text
prev = 2 → 1
curr = 3
```

---

### 🔁 Iteration 3

* Save next → `None`
* Reverse → `3 → 2 → 1`
* Move pointers

```text
prev = 3 → 2 → 1
curr = None (stop)
```

---

## 🏁 Final Result

```text
3 → 2 → 1 → None
```

👉 Return `prev` (new head)

---

## 🧩 Visual Understanding

```
Original:   1 → 2 → 3 → None

Step 1:     1 ←   2 → 3
Step 2:     1 ← 2 ←   3
Step 3:     1 ← 2 ← 3

Final:      3 → 2 → 1 → None
```

---

## ⚠️ Common Mistakes

### ❌ Forgetting to store next node

```python
curr.next = prev   # ❌ you lose rest of list
```

---

### ❌ Not initializing `prev`

```python
prev = None   # ✅ must be done
```

---

### ❌ Returning wrong pointer

```python
return head   # ❌ wrong
return prev   # ✅ correct
```

---

## ⏱️ Complexity Analysis

| Type  | Complexity |
| ----- | ---------- |
| Time  | O(N)       |
| Space | O(1)       |

👉 No extra memory used (in-place reversal)

---

## 🔁 Java Equivalent

```java
public ListNode reverseList(ListNode head) {
    ListNode prev = null;
    ListNode curr = head;

    while(curr != null) {
        ListNode nextNode = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextNode;
    }

    return prev;
}
```

---

## 🎯 Summary

* Traverse the list once
* Reverse links one by one
* Use `prev`, `curr`, `nextNode`
* Return `prev` as new head

---

## 🚀 What to Learn Next

* Reverse Linked List (Recursive)
* Middle of Linked List
* Detect Cycle (Floyd’s Algorithm)
* Merge Two Linked Lists

---
✨ **Key takeaway:**
Reversing a linked list is all about **pointer manipulation**, not value swapping.


