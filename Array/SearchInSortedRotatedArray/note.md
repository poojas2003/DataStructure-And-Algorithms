# 🧠 Search in Rotated Sorted Array 

> 📌 Binary Search Variant | ⚡ O(log N) | 🧩 Pattern-Based Problem

This problem is a classic variation of **Binary Search**, where the array is **sorted but rotated** at some pivot.

It is one of the most important problems for **coding interviews**.

---

# 📌 Problem Statement

Given an array that is:

✔ Originally sorted in ascending order
✔ Rotated at an unknown pivot

Find the index of a given target element.

If not found, return:

```text
-1
```

---

# 🗂 Example

```text
arr    = [4,5,6,7,0,1,2]
target = 0
```

Output:

```text
4
```

---

# 🔍 Understanding Rotation

Original sorted array:

```text
[0,1,2,4,5,6,7]
```

After rotation:

```text
[4,5,6,7 | 0,1,2]
```

👉 The array is split into **two sorted parts**

---

# ⚡ Key Insight

> 🚀 **At least one half of the array is always sorted**

This is the **core idea** used to modify binary search.

---

# 🧩 Algorithm Strategy

At every step:

1. Find `mid`
2. Check if target is found
3. Identify sorted half:

   * Left sorted OR
   * Right sorted
4. Check if target lies in sorted half
5. Move accordingly

---

# ⚙️ Step-by-Step Algorithm

### 1️⃣ Initialize

```text
low = 0
high = n - 1
```

---

### 2️⃣ Loop

```text
while low <= high
```

---

### 3️⃣ Find mid

```text
mid = low + (high - low) / 2
```

---

### 4️⃣ Check target

```text
if arr[mid] == target → return mid
```

---

### 5️⃣ Check sorted half

---

## ✅ Case 1: Left Half Sorted

```text
if arr[low] <= arr[mid]
```

Check if target lies here:

```text
if target >= arr[low] AND target < arr[mid]
    high = mid - 1
else
    low = mid + 1
```

---

## ✅ Case 2: Right Half Sorted

```text
else
```

Check if target lies here:

```text
if target > arr[mid] AND target <= arr[high]
    low = mid + 1
else
    high = mid - 1
```

---

# 🧠 Dry Run (Important)

### Input

```text
arr = [4,5,6,7,0,1,2]
target = 0
```

---

### Iteration 1

```text
low = 0, high = 6
mid = 3 → arr[mid] = 7
```

Left sorted → `[4,5,6,7]`
Target NOT here → move right

```text
low = 4
```

---

### Iteration 2

```text
low = 4, high = 6
mid = 5 → arr[mid] = 1
```

Left sorted → `[0,1]`
Target is here → move left

```text
high = 4
```

---

### Iteration 3

```text
low = 4, high = 4
mid = 4 → arr[mid] = 0 ✅
```

---

### Output

```text
4
```

---

# 💻 Java Code

```java
import java.util.*;

class Main {

    public static int search(int[] arr, int target) {

        int low = 0;
        int high = arr.length - 1;

        while (low <= high) {

            int mid = low + (high - low) / 2;

            if (arr[mid] == target) {
                return mid;
            }

            // Left half sorted
            if (arr[low] <= arr[mid]) {

                if (target >= arr[low] && target < arr[mid]) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }

            }
            // Right half sorted
            else {

                if (target > arr[mid] && target <= arr[high]) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }

        return -1;
    }
}
```

---

# 📊 Complexity

### Time Complexity

```text
O(log N)
```

---

### Space Complexity

```text
O(1)
```

---



# 🧩 Edge Cases

✔ Array not rotated → normal binary search
✔ Single element array
✔ Target at first/last index
✔ Target not present
✔ All elements same (advanced case)

---

# 🎯 Pattern Recognition

Whenever you see:

✔ "Sorted + Rotated Array"
✔ "Search efficiently"

👉 Think:

```text
Binary Search + Sorted Half Check
```

---

# 🧠 Memory Trick

> 🔥 **“Find sorted half → check target → eliminate half”**

---

# 🚀 Related Problems (Must Practice)

1. Find Minimum in Rotated Sorted Array
2. Search in Nearly Sorted Array
3. Peak Element
4. Binary Search on Answer

---

# ⭐ Final Takeaway

This problem teaches:

✔ How to **modify binary search**
✔ How to **think logically under constraints**
✔ How to reduce complexity from **O(N) → O(log N)**



