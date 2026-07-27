# AI Practice Problems — Part 1 (Variables, Operators, Type Conversion, Input)

**Rule:** Solve these using ONLY what you learned in this folder — variables, arithmetic
operators, comparison operators, `int()` / `float()` / `str()`, `input()` and `print()`.
No `if`, no loops, no functions yet. That is on purpose.

Create one file per problem, e.g. `P01_model_accuracy.py`.

---

## P01 — Model Accuracy Calculator ⭐

Every AI model is judged by its **accuracy**: how many predictions it got right out of the total.

Ask the user for the number of **correct predictions** and the number of **total predictions**.
Print the accuracy as a percentage.

```
Enter correct predictions: 87
Enter total predictions: 100
Accuracy: 87.0 %
```

**Hint:** `accuracy = (correct / total) * 100`. Remember `input()` gives you a *string* —
convert it before doing maths.

---

## P02 — Error Rate ⭐

Same input as P01, but print BOTH the accuracy and the **error rate** (the percentage the model got wrong).

```
Enter correct predictions: 87
Enter total predictions: 100
Accuracy   : 87.0 %
Error rate : 13.0 %
```

**Hint:** `error_rate = 100 - accuracy`.

---

## P03 — A Single Neuron ⭐⭐

A neuron in a neural network does exactly this maths:

```
output = (x1 * w1) + (x2 * w2) + bias
```

Ask the user for two inputs `x1`, `x2`, two weights `w1`, `w2`, and a `bias`.
Print the neuron's output.

```
Enter x1: 2
Enter x2: 3
Enter w1: 0.5
Enter w2: -1.5
Enter bias: 1
Neuron output: -2.5
```

This one formula is the heart of every neural network. Get comfortable with it.

---

## P04 — Min-Max Normalization ⭐⭐

Before feeding data to a model we **scale** it to the range 0 to 1. The formula is:

```
scaled = (value - min) / (max - min)
```

Ask for a `value`, a `min` and a `max`. Print the scaled value.

```
Enter the value: 75
Enter the minimum: 50
Enter the maximum: 100
Scaled value: 0.5
```

**Real use:** a student's marks (0–100) and their age (0–80) live on totally different
scales. Normalizing puts them on the same footing so the model treats them fairly.

---

## P05 — Token Cost Estimator ⭐⭐

AI APIs charge per **token** (roughly ¾ of a word). Suppose a model costs
**₹0.002 per input token** and **₹0.006 per output token**.

Ask for the number of input tokens and output tokens. Print the total cost.

```
Enter input tokens: 1500
Enter output tokens: 400
Total cost: Rs 5.4
```

---

## P06 — Dataset Split Calculator ⭐⭐

A dataset is always split into **training** and **testing** parts. A common split is 80 / 20.

Ask for the total number of rows in the dataset. Print how many rows go to training
and how many go to testing. Both must be whole numbers.

```
Enter total rows: 1000
Training rows: 800
Testing rows : 200
```

**Hint:** use `int()` to chop off the decimal, then subtract to get the rest.
Do NOT calculate the test rows separately — if you do, `1001` rows will lose a row.

---

## P07 — Celsius to Fahrenheit Sensor Reading ⭐

An IoT temperature sensor feeding an AI model reports in Celsius, but the model was
trained on Fahrenheit. Convert it.

```
Enter temperature in Celsius: 37
Temperature in Fahrenheit: 98.6
```

**Formula:** `F = (C * 9/5) + 32`

---

## P08 — Image Size in Memory ⭐⭐

A colour image has `width x height` pixels, and each pixel needs **3 bytes** (Red, Green, Blue).

Ask for the width and height. Print the memory the image needs in **bytes**, in **KB**, and in **MB**.

```
Enter image width: 1920
Enter image height: 1080
Bytes: 6220800
KB   : 6075.0
MB   : 5.9326171875
```

**Hint:** 1 KB = 1024 bytes, 1 MB = 1024 KB.

---

## P09 — Is the Prediction Confident? ⭐⭐

A model outputs a **confidence score** between 0 and 1. We usually trust it only if the
score is above `0.75`.

Ask for the confidence score. Using a **comparison operator only** (no `if` — you have not
learned it yet), print `True` or `False`.

```
Enter confidence score: 0.91
Is confident: True
```

**Hint:** `print("Is confident:", score > 0.75)` — a comparison *is* a value.

---

## P10 — Training Time Estimator ⭐⭐⭐

A model takes a fixed number of **seconds per epoch** to train.
Ask for the number of epochs and the seconds per epoch, then print the total time
broken into **hours, minutes and seconds**.

```
Enter number of epochs: 50
Enter seconds per epoch: 95
Total training time: 1 h 19 m 10 s
```

**Hint:** you need `//` (floor division) and `%` (modulo). Total seconds = `50 * 95 = 4750`.
Hours = `4750 // 3600`. The leftover is `4750 % 3600`, and you repeat the trick on that.

---

## P11 — Averaging Three Models (Ensemble) ⭐⭐

In an **ensemble**, several models each make a prediction and we average them for a better answer.

Ask for the predicted house price from three different models and print the ensemble
prediction (their average).

```
Enter prediction from Model A: 4500000
Enter prediction from Model B: 4720000
Enter prediction from Model C: 4380000
Ensemble prediction: 4533333.333333333
```

---

## P12 — Squared Error ⭐⭐⭐

**Loss** measures how wrong a model is. The simplest loss is **squared error**:

```
loss = (actual - predicted) ** 2
```

Ask for the actual value and the predicted value. Print the plain error, the absolute
error, and the squared error.

```
Enter actual value: 100
Enter predicted value: 118
Error          : -18.0
Absolute error : 18.0
Squared error  : 324.0
```

**Hint:** `abs()` gives the absolute value. Why square it? Squaring makes every error
positive AND punishes big mistakes much harder than small ones.

---

### Checklist before you move on

- [ ] I know `input()` always returns a **string**
- [ ] I can convert with `int()`, `float()`, `str()`
- [ ] I know the difference between `/`, `//` and `%`
- [ ] I know `**` is power, not `^`
- [ ] A comparison like `x > 5` produces a `True` / `False` value I can print
