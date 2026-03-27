# 📌 Next Smaller Element (NSE)

## 🧠 Problem Statement

Given an array of integers, find the **next smaller element** for each element in the array.

👉 The next smaller element of an element `x` is the **first smaller element to its right**.
👉 If no such element exists, return `-1` for that position.

---

## 📥 Example

**Input:**

```
[4, 5, 2, 10, 8]
```

**Output:**

```
[2, 2, -1, 8, -1]
```

---

## 📝 Explanation

| Element | Right Side Elements | Next Smaller |
| ------- | ------------------- | ------------ |
| 4       | [5, 2, 10, 8]       | 2            |
| 5       | [2, 10, 8]          | 2            |
| 2       | [10, 8]             | -1           |
| 10      | [8]                 | 8            |
| 8       | []                  | -1           |

---

## 🚀 Approach (Monotonic Stack)

We use a **stack** to efficiently find the next smaller element in **O(n)** time.

### 🔑 Key Idea

* Traverse the array from **right to left**
* Maintain a stack that keeps **smaller elements**
* Remove elements that are **greater than or equal** to current element

---

## ⚙️ Algorithm

1. Initialize:

   * `result` array with `-1`
   * empty `stack`
2. Traverse from **right → left**
3. For each element:

   * Pop elements from stack while they are **≥ current element**
   * If stack is not empty → top is the answer
   * Push current element into stack
4. Return `result`

---

## 💻 Python Code

```python
def nextSmaller(arr):
    n = len(arr)
    result = [-1] * n
    stack = []
    
    for i in range(n-1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        
        if stack:
            result[i] = stack[-1]
        
        stack.append(arr[i])
    
    return result

# Example usage
print(nextSmaller([4, 5, 2, 10, 8]))
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

---

## 🔥 Key Points

* Use **monotonic stack**
* Traverse **right to left**
* Remove **greater elements**
* Stack stores **useful candidates only**

---

## 🧩 Related Problems

* Next Greater Element
* Previous Smaller Element
* Largest Rectangle in Histogram
* Stock Span Problem

---

## 📌 Summary

👉 Next Smaller Element helps in optimizing problems involving **nearest smaller values**.
👉 Using a stack reduces time complexity from **O(n²) → O(n)**.

---
