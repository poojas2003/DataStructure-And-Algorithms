# 🧠 Special Index Problem — Prefix Sum Technique

> 📌 Array Optimization Problem | ⚡ Prefix Sum | 🧩 Index Parity Logic

This note explains the **Special Index Problem**, a well-known array problem that demonstrates how **prefix sums** can be used to optimize calculations and avoid repeated work.

The goal is to determine **how many indices in an array can be removed** such that the **sum of elements at even indices equals the sum of elements at odd indices** in the resulting array.

This problem is commonly used in **technical interviews** to test understanding of:

* Prefix Sum Optimization
* Array Index Parity (Even vs Odd)
* Efficient problem solving with **O(N)** time complexity

---

# 📌 Problem Statement

Given an integer array `A`, count the number of indices `i` such that **removing the element at index `i` results in an array where:**

```
Sum of elements at even indices = Sum of elements at odd indices
```

---

# 🔍 Key Insight

When an element is removed from an array:

```
All elements to the right shift one position left
```

This causes **index parity to change**.

| Original Index | After Removal |
| -------------- | ------------- |
| Even           | Odd           |
| Odd            | Even          |

Handling this shift efficiently is the **core challenge** of the problem.

---

# ⚡ Optimized Approach — Prefix Sum

Instead of recalculating sums for every removal (which would take **O(N²)** time), we use **prefix sums** to compute results in **O(N)** time.

We maintain two prefix arrays:

### `prefix_even`

Stores cumulative sums of elements located at **even indices**.

### `prefix_odd`

Stores cumulative sums of elements located at **odd indices**.

---

# 🗂 Example

```
A = [2, 1, 6, 4]

Index : 0  1  2  3
Value : 2  1  6  4
```

Even index elements → `2 + 6 = 8`
Odd index elements → `1 + 4 = 5`

---

# ⚙️ Algorithm Steps

### 1️⃣ Initialize Prefix Arrays

```
prefix_even = [0] * (n + 1)
prefix_odd  = [0] * (n + 1)
```

These arrays store cumulative sums for quick lookup.

---

### 2️⃣ Build Prefix Sums

```
for i in range(n):
    prefix_even[i+1] = prefix_even[i] + (A[i] if i % 2 == 0 else 0)
    prefix_odd[i+1]  = prefix_odd[i]  + (A[i] if i % 2 == 1 else 0)
```

Each index stores the sum of elements **up to that position**.

---

### 3️⃣ Store Total Even & Odd Sums

```
total_even = prefix_even[n]
total_odd  = prefix_odd[n]
```

These represent the sums of all even and odd indexed elements in the original array.

---

### 4️⃣ Simulate Removing Each Index

For every index `i`, split the array into two parts:

```
LEFT PART  : indices 0 → i-1
RIGHT PART : indices i+1 → n-1
```

Left side parity **remains unchanged**.

Right side parity **flips** because elements shift left.

---

### 5️⃣ Calculate New Sums

```
left_even = prefix_even[i]
left_odd  = prefix_odd[i]

right_even = total_even - prefix_even[i+1]
right_odd  = total_odd  - prefix_odd[i+1]
```

After the shift:

```
new_even = left_even + right_odd
new_odd  = left_odd  + right_even
```

---

### 6️⃣ Check Balanced Condition

```
if new_even == new_odd:
    count += 1
```

If both sums match, the index is considered a **special index**.

---

# 💻 Python Implementation

```python
def solve(A):
    n = len(A)

    prefix_even = [0] * (n + 1)
    prefix_odd  = [0] * (n + 1)

    for i in range(n):
        prefix_even[i+1] = prefix_even[i] + (A[i] if i % 2 == 0 else 0)
        prefix_odd[i+1]  = prefix_odd[i]  + (A[i] if i % 2 == 1 else 0)

    total_even = prefix_even[n]
    total_odd  = prefix_odd[n]

    count = 0

    for i in range(n):

        left_even = prefix_even[i]
        left_odd  = prefix_odd[i]

        right_even = total_even - prefix_even[i+1]
        right_odd  = total_odd  - prefix_odd[i+1]

        new_even = left_even + right_odd
        new_odd  = left_odd  + right_even

        if new_even == new_odd:
            count += 1

    return count
```

---

# 📊 Example Walkthrough

Input:

```
A = [2, 1, 6, 4]
```

Remove index `1`:

```
[2, 6, 4]
```

Even indices → `2 + 4 = 6`
Odd indices → `6`

Since both sums are equal, index `1` is a **special index**.

Final result:

```
1
```

---

# ⏱ Complexity Analysis

### Time Complexity

```
O(N)
```

* Prefix sum construction → `O(N)`
* Checking each index → `O(N)`

---

### Space Complexity

```
O(N)
```

Extra space is used for the prefix arrays.

---

# 🧩 Concepts Learned

✔ Prefix Sum Optimization
✔ Even / Odd Index Handling
✔ Efficient Array Manipulation
✔ Algorithmic Problem Solving

---

# 🎯 Takeaway

This problem highlights an important principle in algorithm design:

> **Precompute values once, reuse them many times.**

Using prefix sums reduces the complexity from **O(N²)** to **O(N)**, making the solution efficient and interview-ready.

---

⭐ *Consistent practice with problems like this builds strong problem-solving skills.*
