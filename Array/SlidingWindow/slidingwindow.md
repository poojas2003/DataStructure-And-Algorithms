# 🧠 Maximum Subarray Sum of Size K — Sliding Window Technique

> 📌 Array Optimization Problem | ⚡ Sliding Window | 🧩 Efficient Window Updates

This note explains how to find the **maximum sum of a contiguous subarray of size `K`** using two approaches.

The problem demonstrates how the **Sliding Window technique** optimizes calculations and avoids repeated work.

This is a very common **Data Structures & Algorithms interview question** used to test understanding of:

* Sliding Window Optimization
* Efficient array traversal
* Time complexity improvement

---

# 📌 Problem Statement

Given an integer array `A` and an integer `K`, find the **maximum sum of any contiguous subarray of size `K`**.

---

# 🗂 Example

```
A = [1,2,3,4,5,6,-1]
K = 4
```

Possible subarrays:

| Subarray   | Sum    |
| ---------- | ------ |
| [1,2,3,4]  | 10     |
| [2,3,4,5]  | 14     |
| [3,4,5,6]  | **18** |
| [4,5,6,-1] | 14     |

✅ **Maximum Sum = 18**

---

# ⚡ Approach 1 — Brute Force

### Idea

Calculate the sum of every possible subarray of size `K`.

For each window:

```
Compute sum of K elements
Move window one step forward
Repeat
```

---

# ⚙️ Algorithm Steps

1️⃣ Start window from index `0`

2️⃣ Calculate sum from

```
start → end
```

3️⃣ Update maximum sum

4️⃣ Move window forward

```
start += 1
end += 1
```

---

# 💻 Python Implementation

```python
A=[1,2,3,4,5,6,-1]
K=4
n=len(A)

start=0
end=K-1
result=float('-inf')

while(end<n):

    subArraySum=0

    for i in range(start,end+1):
        subArraySum+=A[i]

    result=max(result,subArraySum)

    start+=1
    end+=1

print(result)
```

---

# ⏱ Complexity Analysis

| Metric           | Value        |
| ---------------- | ------------ |
| Time Complexity  | **O(N × K)** |
| Space Complexity | **O(1)**     |

Reason: For every window we recompute the sum of `K` elements.

---

# ⚡ Approach 2 — Sliding Window (Optimized)

### Key Insight

When the window moves forward by one step:

```
One element leaves the window
One element enters the window
```

Instead of recalculating the sum, update it using:

```
window_sum = window_sum + new_element - removed_element
```

---

# ⚙️ Window Update Formula

```
window_sum = window_sum + A[i] - A[i-K]
```

| Term     | Meaning                     |
| -------- | --------------------------- |
| `A[i]`   | New element entering window |
| `A[i-K]` | Element leaving window      |

---

# 💻 Python Implementation

```python
A=[1,2,3,4,5,6,-1]
K=4
n=len(A)

window_sum=sum(A[0:K])
max_sum=window_sum

for i in range(K,n):

    window_sum = window_sum + A[i] - A[i-K]

    max_sum=max(max_sum,window_sum)

print(max_sum)
```

---

# 📊 Sliding Window Iteration

| Step    | Window     | Calculation   | Sum    |
| ------- | ---------- | ------------- | ------ |
| Initial | [1,2,3,4]  | 1+2+3+4       | 10     |
| Move 1  | [2,3,4,5]  | 10 + 5 − 1    | 14     |
| Move 2  | [3,4,5,6]  | 14 + 6 − 2    | **18** |
| Move 3  | [4,5,6,-1] | 18 + (-1) − 3 | 14     |

Maximum sum = **18**

---

# ⚖️ Approach Comparison

| Feature             | Brute Force  | Sliding Window      |
| ------------------- | ------------ | ------------------- |
| Technique           | Nested Loop  | Window Optimization |
| Time Complexity     | **O(N × K)** | **O(N)**            |
| Space Complexity    | **O(1)**     | **O(1)**            |
| Efficiency          | Slower       | Faster              |
| Interview Preferred | ❌            | ✅                   |

---

# 🧩 Concepts Learned

✔ Sliding Window Technique
✔ Efficient Window Updates
✔ Time Complexity Optimization
✔ Contiguous Subarray Handling

---

# 🎯 Key Takeaway

Instead of recalculating the entire subarray sum repeatedly:

> **Update only the changed elements in the window.**

Sliding Window reduces the complexity from

```
O(N × K)
```

to

```
O(N)
```

making it much more efficient for large arrays.
