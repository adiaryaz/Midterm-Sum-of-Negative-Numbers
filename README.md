# Sum of Negative Numbers

Mid Exam for Basic Programming - A program to calculate the sum of all negative numbers from a user-defined series of inputs.

## 📝 Description

This program first prompts the user for a number, `n`, which specifies how many integers will be entered subsequently. It then reads `n` numbers one by one. The program identifies all the strictly negative numbers (less than zero) from the list and calculates their total sum.

-----

## 🎯 Problem Statement

### Input:

  * The first input is a single positive integer (`n`).
  * The next `n` inputs are the integers to be evaluated.

### Output:

  * The total sum of all negative numbers entered.
  * "NotProceed" if the first input `n` is not a positive integer or not an integer at all.

### Rules:

1.  The first input **n** (the count of numbers to follow) must be a **positive integer**.
2.  If `n` is zero, negative, or a non-integer (like a float), the program should output the message **"NotProceed"**.
3.  The program will then read `n` integers, which can be positive, negative, or zero.
4.  The program must only sum the numbers that are strictly less than 0.
5.  The final output should be the sum of only these negative numbers.

-----

## 💡 Examples

### Example 1 (n = 3)

**Input:**

```
3
-1
-2
3
```

**Output:**

```
-3
```

**Explanation:** Out of the numbers `-1`, `-2`, `3`, the negative ones are `-1` and `-2`. The sum is **-3**.

### Example 2 (n = 1)

**Input:**

```
1
3
```

**Output:**

```
0
```

**Explanation:** There are no negative numbers in the input list. The sum is **0**.

### Example 3 (n = -5)

**Input:**

```
-5
```

**Output:**

```
NotProceed
```

**Explanation:** The first input `n` is negative, which is not a valid count.

### Example 4 (n = 1.5)

**Input:**

```
1.5
```

**Output:**

```
NotProceed
```

**Explanation:** The first input `n` is not an integer.

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiaryaz/sum-of-negatives.git
    cd sum-of-negatives
    ```

2.  **Run the program** (assuming the file is `PEMDAS-L9.py`):

    ```bash
    python PEMDAS-L9.py
    ```

    Enter the count `n` first, then enter `n` integers to see the result.

-----
