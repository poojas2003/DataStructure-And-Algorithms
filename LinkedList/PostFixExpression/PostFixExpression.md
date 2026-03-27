# 📌 Postfix Expression Evaluation (Stack)

## 🧠 What is Postfix Expression?

A **Postfix Expression** (Reverse Polish Notation) is a mathematical expression where:

* Operators come **after** operands

### Example:

```text
Infix   : (2 + 3) * 4
Postfix : 2 3 + 4 *
```

---

## 🎯 Problem Statement

Evaluate a given postfix expression and return the result.

---

## 🧩 Approach (Using Stack)

We use a **stack** to evaluate the expression.

### Steps:

1. Traverse each character in the expression
2. If it is a **digit** → push it into the stack
3. If it is an **operator**:

   * Pop top two elements from stack
   * Perform operation → `b operator a`
   * Push result back to stack
4. Final result will be the only element in the stack

---

## 💻 Python Code

```python
def postExpression(s):
    stack = []

    for ch in s:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            a = stack.pop()
            b = stack.pop()

            if ch == '+':
                stack.append(b + a)
            elif ch == '-':
                stack.append(b - a)
            elif ch == '*':
                stack.append(b * a)
            elif ch == '/':
                stack.append(int(b / a))

    return stack[0]


print(postExpression("23*456+-5--"))  # Output: 18
```

---

## 🔍 Example Walkthrough

### Input:

```text
23*456+-5--
```

### Execution:

| Step | Char | Stack Before | Action     | Stack After  |
| ---- | ---- | ------------ | ---------- | ------------ |
| 1    | 2    | []           | Push       | [2]          |
| 2    | 3    | [2]          | Push       | [2, 3]       |
| 3    | *    | [2, 3]       | 2*3=6      | [6]          |
| 4    | 4    | [6]          | Push       | [6, 4]       |
| 5    | 5    | [6, 4]       | Push       | [6, 4, 5]    |
| 6    | 6    | [6, 4, 5]    | Push       | [6, 4, 5, 6] |
| 7    | +    | [6,4,5,6]    | 5+6=11     | [6,4,11]     |
| 8    | -    | [6,4,11]     | 4-11=-7    | [6,-7]       |
| 9    | 5    | [6,-7]       | Push       | [6,-7,5]     |
| 10   | -    | [6,-7,5]     | -7-5=-12   | [6,-12]      |
| 11   | -    | [6,-12]      | 6-(-12)=18 | [18]         |

### Output:

```text
18
```

---

## ⏱️ Time Complexity

* **O(n)** → Single pass through expression

## 📦 Space Complexity

* **O(n)** → Stack usage

---

## ⚠️ Important Rules

### 1. Order Matters

```python
a = stack.pop()
b = stack.pop()
```

👉 Always:

```text
b operator a
```

---

### 2. Valid Postfix Condition

```text
Operands = Operators + 1
```

👉 Final stack must contain **only 1 value**

---

## ❌ Invalid Example

```text
23*456+-5-
```

👉 Leaves stack as:

```text
[6, -12]
```

❌ Invalid (more than one value)

---

## 🚀 Key Concepts

* Stack (LIFO)
* Expression evaluation
* Order of operations

---

## 🎯 Summary

✔ Push digits
✔ Pop 2 values for operator
✔ Apply `b op a`
✔ Push result
✔ Final stack should have 1 value

---

## 🔥 Practice 

* Infix → Postfix conversion ⭐
* Prefix expression evaluation
* Next Greater Element

---

