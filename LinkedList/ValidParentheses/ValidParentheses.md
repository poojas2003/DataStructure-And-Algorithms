# ✅ Valid Parentheses (Stack Approach)

## 📌 Problem Statement

Given a string `s` containing just the characters:

```
( ) { } [ ]
```

determine if the input string is **valid**.

### A string is valid if:

* Open brackets are closed by the same type of brackets
* Open brackets are closed in the correct order

---

## 🧠 Approach (Using Stack)

We use a **stack** to keep track of opening brackets.

### Steps:

1. Traverse each character in the string
2. If it's an **opening bracket** → push it into the stack
3. If it's a **closing bracket**:

   * Check if stack is not empty
   * Check if top of stack matches the correct opening bracket
   * If yes → pop from stack
   * Else → return `False`
4. At the end:

   * If stack is empty → valid
   * Else → invalid

---

## 💻 Python Code

```python
def validParentheis(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if stack and stack[-1] == pairs[ch]:
                stack.pop()
            else:
                return False

    return not stack


print(validParentheis("({})"))  # Output: True
```

---

## 🔍 Example

### Input:

```
s = "({})"
```

### Execution:

| Step | Character | Stack Before | Action | Stack After |
| ---- | --------- | ------------ | ------ | ----------- |
| 1    | (         | []           | Push   | ['(']       |
| 2    | {         | ['(']        | Push   | ['(', '{']  |
| 3    | }         | ['(', '{']   | Pop    | ['(']       |
| 4    | )         | ['(']        | Pop    | []          |

### Output:

```
True
```

---

## ⏱️ Time Complexity

* **O(n)** → We traverse the string once

## 📦 Space Complexity

* **O(n)** → In worst case, all characters are pushed to stack

---

## 🚀 Key Concepts

* Stack (LIFO)
* HashMap (Dictionary)
* String traversal

---

## ⚠️ Common Mistake

❌ Using:

```python
if ch == "({[":
```

✅ Correct:

```python
if ch in "({[":
```

---

## 🎯 Summary

* Use stack to track opening brackets
* Match closing with top of stack
* Final stack should be empty for valid string

---

## 🔥 Practice More

* Remove outer parentheses
* Longest valid parentheses
* Next greater element (stack based)

---

