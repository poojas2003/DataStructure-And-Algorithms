# 📘 Even Index Prefix Sum (Python)

## 📌 Problem Statement

Given an array `A`, compute the **prefix sum considering only even indices (0-based indexing)**.

At each index:

* If the index is **even** → add the element to sum
* If the index is **odd** → carry forward previous sum

---

## 🧠 Concept

Prefix sum means:

> Each position stores the sum of elements up to that index.

In this problem:

* We only include elements at **even indices (0, 2, 4, …)**

---

## 🧪 Example

### Input:

```python
A = [1, 2, 3, 4, 5]
```

### Explanation:

| Index | Value | Action     | Prefix Sum |
| ----- | ----- | ---------- | ---------- |
| 0     | 1     | Even → Add | 1          |
| 1     | 2     | Odd → Copy | 1          |
| 2     | 3     | Even → Add | 1 + 3 = 4  |
| 3     | 4     | Odd → Copy | 4          |
| 4     | 5     | Even → Add | 4 + 5 = 9  |

### Output:

```python
[1, 1, 4, 4, 9]
```

---

## 💻 Python Code

```python
def even_index_prefix_sum(A):
    n = len(A)
    even_prefix = [0] * n

    # First element
    even_prefix[0] = A[0]

    # Build prefix array
    for i in range(1, n):
        if i % 2 == 0:
            even_prefix[i] = even_prefix[i-1] + A[i]
        else:
            even_prefix[i] = even_prefix[i-1]

    return even_prefix


# Example usage
A = [1, 2, 3, 4, 5]
print(even_index_prefix_sum(A))
```

---

## ⚡ Time & Space Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

---

## 🎯 Key Idea

* Even index → **Add current element**
* Odd index → **Copy previous sum**

---

## 🚀 Applications

* Range queries
* Optimization problems
* Interview questions (important for companies like Amazon, Flipkart)

---

## 🧪 Practice

Try with:

```python
A = [2, 4, 6, 8, 10]
```

Expected Output:

```
[2, 2, 8, 8, 18]
```

---

## 🔥 Next Step

Learn:

* Odd Index Prefix Sum
* Combined Even + Odd Prefix
* Special Index Problem 

---
