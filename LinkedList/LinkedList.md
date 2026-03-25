# 🔗 Display Values of a Linked List

> **Level:** Beginner
> **Concepts:** Linked List Traversal · Iteration · Output Formatting
> **Language:** Python

---

## 📌 Problem Overview

You are given the **starting node (head)** of a singly linked list.
Your task is to **print all node values in sequence**, separated by spaces.

👉 Important rule:

* Each value should be followed by a space
* Output must end with a newline

### 🧾 Example

```
Input:  1 → 2 → 3 → None  
Output: 1 2 3 
```

---

## 🧠 Key Idea

A linked list does not allow direct access like arrays.
So the only way to read values is to **move step-by-step from the first node to the last**.

---

## 🚶 Traversal Logic (Core Concept)

Think of it like walking through a chain:

1. Start from the head
2. Visit current node
3. Move to next node
4. Stop when you reach `None`

---

## 🧱 Node Structure

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
```

Each node contains:

* `val` → data
* `next` → reference to next node

---

## 💡 Solution Code

```python
class Solution:
    def printNode(self, head):
        curr = head
        result = []

        while curr:
            result.append(str(curr.val))
            curr = curr.next

        print(" ".join(result) + " ")
```

---

## 🔍 Step-by-Step Explanation

### 1️⃣ Initialize pointer

```python
curr = head
```

We use `curr` to move through the list without losing the head.

---

### 2️⃣ Loop through list

```python
while curr:
```

Loop continues until we reach the end (`None`).

---

### 3️⃣ Store values

```python
result.append(str(curr.val))
```

Convert values to string (required for joining later).

---

### 4️⃣ Move forward

```python
curr = curr.next
```

Shift pointer to next node.

---

### 5️⃣ Print result

```python
print(" ".join(result) + " ")
```

* `" ".join(result)` → adds space between values
* `+ " "` → adds required trailing space

---

## 🔄 Example Walkthrough

For:

```
1 → 2 → 3
```

| Step | Current Value | Result List   |
| ---- | ------------- | ------------- |
| 1    | 1             | ['1']         |
| 2    | 2             | ['1','2']     |
| 3    | 3             | ['1','2','3'] |

Final Output:

```
1 2 3 
```

---

## ⚠️ Common Mistakes

### ❌ Forgetting to move pointer

```python
# Infinite loop!
while curr:
    result.append(str(curr.val))
```

---

### ❌ Not converting to string

```python
# Causes error
result.append(curr.val)
```

---

### ❌ Wrong function call

```python
make_list[1,2,3]   # ❌
make_list([1,2,3]) # ✅
```

---

### ❌ Printing inside loop

```python
# Prints partial results
while curr:
    print(curr.val)
```

---

## ⏱️ Complexity

| Type  | Value |
| ----- | ----- |
| Time  | O(N)  |
| Space | O(N)  |

---

## 🛠️ Helper Function (Optional)

```python
def make_list(values):
    if not values:
        return None

    head = Node(values[0])
    curr = head

    for v in values[1:]:
        curr.next = Node(v)
        curr = curr.next

    return head
```

---

## 🧪 Sample Usage

```python
head = make_list([1, 2, 3])

sol = Solution()
sol.printNode(head)
```

---

## 🎯 Summary

* Start from head
* Traverse using `.next`
* Collect values
* Print using `" ".join()`
* Add trailing space

---

## 🚀 What to Learn Next

* Reverse a linked list
* Find middle node
* Detect cycle
* Merge two lists

