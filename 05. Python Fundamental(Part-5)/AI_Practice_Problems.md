# AI Practice Problems — Part 5 (File Handling, Exceptions, Modules, Comprehensions, NumPy & Pandas)

> This folder was empty, so I filled it with the topics that come next and that you
> genuinely need before touching machine learning. If your course covers something
> different here, treat this as bonus practice.

**Topics assumed:** reading and writing files, `with open(...)`, CSV and JSON,
`try / except / finally`, raising your own errors, `import` and custom modules,
list/dict/set comprehensions, and the first two AI libraries — **NumPy** and **pandas**.

**Install what you need:**
```bash
pip install numpy pandas
```

Create one file per problem, e.g. `P01_read_dataset.py`.

---

# Section A — File Handling

## P01 — Read a Dataset File ⭐

First create `data.txt` with one number per line:

```
23.5
19.8
22.1
25.0
21.3
```

Now write a program that reads the file, converts every line to a float, and prints the
count, sum, mean, min and max.

```
Read 5 values.
Sum : 111.7
Mean: 22.34
Min : 19.8
Max : 25.0
```

**Always use `with open("data.txt") as f:`** — it closes the file automatically even if
your code crashes halfway through.

---

## P02 — Write Predictions to a File ⭐⭐

Take a list of predictions and write them to `predictions.txt`, one per line, numbered.

```
1,0.87
2,0.34
3,0.91
```

Then read the file back and print only the rows where the score is above `0.5`.

---

## P03 — CSV Reader Without a Library ⭐⭐⭐

Create `students.csv`:

```
name,maths,science,english
Alice,88,92,79
Bob,45,61,55
Charlie,95,89,91
Diana,67,72,84
```

Read it manually (no `csv` module yet):
1. Read the first line as the **header**
2. For each remaining line, `split(",")` and build a dictionary using the header as keys
3. End up with a list of dictionaries — the same structure as Part-3 P08

```
[{'name': 'Alice', 'maths': '88', 'science': '92', 'english': '79'}, ...]
```

Then convert the score fields to `int` and print each student's average.

**This is what `pandas.read_csv()` does for you.** Writing it once by hand means you will
actually understand what pandas hands back.

---

## P04 — Log File Analyzer ⭐⭐⭐

Create `training.log`:

```
2026-01-10 10:00:01 INFO Epoch 1 loss=0.891 acc=0.42
2026-01-10 10:02:15 INFO Epoch 2 loss=0.654 acc=0.61
2026-01-10 10:04:33 WARNING GPU memory at 91%
2026-01-10 10:04:40 INFO Epoch 3 loss=0.412 acc=0.78
2026-01-10 10:06:58 ERROR CUDA out of memory
2026-01-10 10:07:10 INFO Epoch 4 loss=0.298 acc=0.85
```

Write a program that:
1. Counts how many INFO / WARNING / ERROR lines there are
2. Extracts every `loss=` value into a list and confirms the loss is decreasing
3. Prints the final accuracy
4. Prints every ERROR line

```
INFO: 4 | WARNING: 1 | ERROR: 1
Losses: [0.891, 0.654, 0.412, 0.298]
Loss decreasing: True
Final accuracy: 0.85
Errors found:
  2026-01-10 10:06:58 ERROR CUDA out of memory
```

Reading training logs is a daily task in real ML work.

---

## P05 — JSON Config Loader ⭐⭐

Create `config.json`:

```json
{
  "model_name": "resnet50",
  "learning_rate": 0.001,
  "epochs": 100,
  "batch_size": 32,
  "use_gpu": true,
  "layers": [128, 64, 32]
}
```

Use `import json` to load it and print each setting. Then change `epochs` to `150` in your
program and save it back to `config_updated.json`.

**Hint:** `json.load(f)` reads, `json.dump(data, f, indent=2)` writes.

---

# Section B — Exception Handling

## P06 — Safe Division and Safe Input ⭐

Write `safe_accuracy(correct, total)` that returns `0.0` instead of crashing when `total`
is `0`. Use `try / except ZeroDivisionError`.

Then write a loop that keeps asking the user for a number until they type a valid one,
catching `ValueError` when they type text.

```
Enter a number: hello
That is not a number. Try again.
Enter a number: 42
Got it: 42
```

---

## P07 — The Missing File ⭐⭐

Try to open `nonexistent_data.csv`. Catch `FileNotFoundError` and print a helpful message
instead of a stack trace. Use `finally` to print `Done` either way.

```
try:
    ...
except FileNotFoundError:
    print("Dataset not found. Check the path.")
except PermissionError:
    print("No permission to read that file.")
finally:
    print("Done")
```

**Rule:** catch the *specific* exception you expect. A bare `except:` hides real bugs and
will waste hours of your life.

---

## P08 — Custom Exceptions for a Model ⭐⭐⭐

Define your own exception classes (they just inherit from `Exception`):

- `NotTrainedError` — raised when `predict()` is called before `fit()`
- `InvalidDataError` — raised when the training data is empty or `X` and `y` have
  different lengths

Rebuild the `Model` class from Part 4 to `raise` these instead of printing errors.

```
m = Model("Test")
m.predict([1,2,3])
->  NotTrainedError: Call fit() before predict()

m.fit([1,2,3], [1,2])
->  InvalidDataError: X has 3 samples but y has 2
```

**Why raise instead of print?** A printed error can be ignored and the program continues
with garbage. A raised error stops everything until someone handles it properly.

---

## P09 — Robust Data Loader ⭐⭐⭐

Put it all together. Write `load_dataset(path)` that:
- catches `FileNotFoundError` and returns an empty list
- skips any line that will not convert to a number, but counts and reports how many it skipped
- raises `InvalidDataError` if the file is empty or every line was bad

Test it against a messy file:

```
23.5
abc
19.8

22.1
N/A
25.0
```
```
Loaded 4 values, skipped 3 bad lines.
```

---

# Section C — Modules & Comprehensions

## P10 — Build Your Own Module ⭐⭐

Create `ml_utils.py` containing the functions you have written across all five folders:

```python
def accuracy(correct, total): ...
def normalize(value, min_val, max_val): ...
def mean(values): ...
def std(values): ...
def mse(actual, predicted): ...
def relu(x): ...
def sigmoid(x): ...
```

Then in a separate file `test_utils.py`, do `import ml_utils` and use every function.

Add this at the bottom of `ml_utils.py`:
```python
if __name__ == "__main__":
    print("Running self-tests...")
    # call each function with known values
```

**What that line does:** the block runs when you execute `ml_utils.py` directly, but NOT
when another file imports it. Every serious Python file uses this.

---

## P11 — Comprehensions: Rewrite Your Old Loops ⭐⭐

Take five loops you wrote in earlier folders and compress each into one line.

```python
# Before
squares = []
for x in range(10):
    squares.append(x ** 2)

# After
squares = [x ** 2 for x in range(10)]
```

Rewrite these as comprehensions:
1. Squares of numbers 1–20 that are even → **list** comprehension with a condition
2. `{word: len(word) for word in tokens}` → **dict** comprehension
3. Unique first letters of a word list → **set** comprehension
4. Normalize a list of scores to 0–1 in one line
5. ReLU applied to a whole list in one line

**Caution:** comprehensions are for *simple* transformations. If you need an `if/else`
plus three operations, a normal loop is more readable. Clever is not the goal.

---

# Section D — NumPy

## P12 — First NumPy Array ⭐⭐

```python
import numpy as np
```

1. Create an array from `[1, 2, 3, 4, 5]` and print its `shape`, `dtype`, `ndim`, `size`
2. Create a 3x4 array of zeros, one of ones, and one of random numbers
3. Create `np.arange(0, 20, 2)` and `np.linspace(0, 1, 11)`
4. Reshape a 12-element array into `(3, 4)` and then `(2, 6)`

```
Shape: (5,)  dtype: int64  ndim: 1  size: 5
```

---

## P13 — Vectorization: NumPy vs Loops ⭐⭐⭐

Do the same job twice and compare.

```python
import numpy as np
import time

data = list(range(1_000_000))

# Way 1 — plain Python loop
start = time.time()
result1 = [x * 2 for x in data]
print("Loop  :", time.time() - start)

# Way 2 — NumPy
arr = np.array(data)
start = time.time()
result2 = arr * 2
print("NumPy :", time.time() - start)
```

NumPy will be roughly 10–50x faster. **This is the entire reason AI uses NumPy.** No loop,
no `append` — one operation applies to the whole array at once. That is *vectorization*,
and it is the mental shift you need for everything that follows.

---

## P14 — NumPy Statistics and Slicing ⭐⭐

Given a 5x3 array of student marks (5 students, 3 subjects):

```python
marks = np.array([
    [88, 92, 79],
    [45, 61, 55],
    [95, 89, 91],
    [67, 72, 84],
    [30, 41, 38],
])
```

Print:
1. Each student's total (`axis=1`) and each subject's average (`axis=0`)
2. The highest mark overall and its position (`argmax`)
3. Every mark above 80 using **boolean indexing**: `marks[marks > 80]`
4. All marks for subject 2 only: `marks[:, 1]`
5. The first three students only: `marks[:3]`
6. Normalize the whole array to 0–1 in one line

**`axis` is the thing everyone gets wrong:** `axis=0` collapses rows (gives per-column
results), `axis=1` collapses columns (gives per-row results). Print both until it sticks.

---

## P15 — A Neuron Layer with NumPy ⭐⭐⭐

Rebuild the single neuron from Part-1 P03, but now for a whole layer at once using
matrix multiplication.

```python
inputs  = np.array([1.0, 2.0, 3.0, 2.5])           # 4 features
weights = np.array([[ 0.2,  0.8, -0.5,  1.0],      # neuron 1
                    [ 0.5, -0.91, 0.26, -0.5],     # neuron 2
                    [-0.26,-0.27, 0.17, 0.87]])    # neuron 3
biases  = np.array([2.0, 3.0, 0.5])

outputs = np.dot(weights, inputs) + biases
```

Print the output, then apply ReLU with `np.maximum(0, outputs)`.

```
Raw outputs : [ 4.8    1.21   2.385]
After ReLU  : [ 4.8    1.21   2.385]
```

**You just built one layer of a neural network in three lines.** Everything else in deep
learning is this operation, repeated and stacked.

---

# Section E — pandas

## P16 — First DataFrame ⭐⭐

```python
import pandas as pd
```

Build a DataFrame from the students dictionary you have used throughout, then explore it:

```python
df.head()        # first 5 rows
df.info()        # column types and null counts
df.describe()    # count, mean, std, min, quartiles, max
df.shape         # (rows, columns)
df.columns       # column names
```

`df.describe()` is usually the very first thing anyone runs on a new dataset. Run it and
read every number.

---

## P17 — Load and Explore a Real CSV ⭐⭐

Load the `students.csv` you made in P03 — but this time with one line:

```python
df = pd.read_csv("students.csv")
```

Compare it to the 20 lines you wrote by hand. Then:
1. Add a `total` column and an `average` column
2. Sort by average, descending
3. Filter to students whose average is above 70
4. Add a `grade` column: A for 85+, B for 70+, C for 50+, else D
5. Save the result to `students_processed.csv`

**Hint:** `df["total"] = df["maths"] + df["science"] + df["english"]` — no loop needed.

---

## P18 — Handling Missing Data ⭐⭐⭐

Create a CSV with deliberate holes:

```
name,age,salary,experience
Alice,28,55000,3
Bob,,48000,2
Charlie,35,,8
Diana,42,92000,
Eshan,,61000,5
```

Then:
1. `df.isnull().sum()` — how many holes per column
2. Fill `age` with the column mean
3. Fill `experience` with `0`
4. Drop any row still missing `salary`
5. Confirm zero nulls remain

```
Missing before:
age           2
salary        1
experience    1

Missing after: 0
```

**Real datasets are 20–40% cleaning work.** This problem is not busywork — it is the job.

---

## P19 — GroupBy and Aggregation ⭐⭐⭐

Build a sales DataFrame with columns `region`, `product`, `units`, `revenue` and about
15 rows across 3 regions and 4 products. Then answer:

1. Total revenue per region — `df.groupby("region")["revenue"].sum()`
2. Average units per product
3. Which region sold the most of each product — `groupby(["region", "product"])`
4. Multiple stats at once — `.agg(["sum", "mean", "count"])`

`groupby` is the single most useful pandas operation. If you know SQL, it is `GROUP BY`.
If you do not, it is: split the data into buckets, compute something per bucket, put the
results back together.

---

## P20 — Full Mini Pipeline ⭐⭐⭐⭐

Put every part of this folder together into one program.

1. **Load** a CSV with `pandas`, wrapped in `try / except FileNotFoundError`
2. **Clean** it — fill missing values, drop duplicates, fix data types
3. **Engineer** two new features (e.g. a ratio column, a binned category column)
4. **Normalize** the numeric columns to 0–1
5. **Split** into 80% train and 20% test — `df.sample(frac=0.8, random_state=42)`
6. **Save** both parts as `train.csv` and `test.csv`
7. **Report** the shape and null count at every step

```
Loaded    : (150, 5)   nulls: 12
Cleaned   : (147, 5)   nulls: 0
Engineered: (147, 7)
Normalized: (147, 7)
Train     : (118, 7)
Test      : (29, 7)
Saved train.csv and test.csv
```

**This is a real ML preprocessing pipeline.** Every model you ever train starts with
exactly these six steps. If you can write this from memory, you are ready for
scikit-learn.

---

### Checklist before you move on to Machine Learning

- [ ] I always use `with open(...)` instead of `open()` + `close()`
- [ ] I catch **specific** exceptions, never a bare `except:`
- [ ] I can raise my own exception classes
- [ ] I know what `if __name__ == "__main__":` does
- [ ] I can write list, dict and set comprehensions — and I know when NOT to
- [ ] I understand why NumPy is faster than a Python loop
- [ ] I know the difference between `axis=0` and `axis=1`
- [ ] I can load, clean, filter and group a DataFrame
- [ ] I can handle missing values three different ways
- [ ] I can split a dataset into train and test

### What comes after this

Once P20 runs clean, the next step is **scikit-learn**: `train_test_split`,
`LinearRegression`, `LogisticRegression`, `DecisionTreeClassifier`, and the
`fit` / `predict` / `score` pattern you already built by hand in Part 4.
