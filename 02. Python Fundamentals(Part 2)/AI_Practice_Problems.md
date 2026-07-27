# AI Practice Problems — Part 2 (Conditionals, Loops, Functions, Lambda)

**Rule:** Use only what you learned up to this folder — `if / elif / else`, nesting,
`match-case`, `while`, `for`, `range()`, `break`, `continue`, `def` functions, and `lambda`.
Lists and dictionaries come in Part 3, so avoid them here (a couple of problems below let
you use a simple list purely to loop over — that is fine).

Create one file per problem, e.g. `P01_confidence_gate.py`.

---

## P01 — Confidence Gate ⭐

A model returns a confidence score between `0.0` and `1.0`. Decide what to do with it:

| Score | Action |
|---|---|
| `>= 0.90` | `Auto-approve` |
| `0.70` to `0.89` | `Send to human review` |
| `0.40` to `0.69` | `Low confidence - ask user to rephrase` |
| below `0.40` | `Reject` |

```
Enter confidence score: 0.83
Action: Send to human review
```

Also handle bad input: if the score is below 0 or above 1, print `Invalid score`.

---

## P02 — Classify the AI Task ⭐

Use **`match-case`** for this one. The user types a task name and you print which family
of AI it belongs to.

| Input | Output |
|---|---|
| `classification`, `regression` | `Supervised Learning` |
| `clustering`, `pca` | `Unsupervised Learning` |
| `q-learning`, `policy-gradient` | `Reinforcement Learning` |
| anything else | `Unknown task` |

```
Enter the task: clustering
Category: Unsupervised Learning
```

**Hint:** `match-case` lets you combine patterns with `|` — `case "clustering" | "pca":`

---

## P03 — Training Loop with Early Stopping ⭐⭐

This is how real training actually works. Start with `loss = 1.0`. On every epoch the loss
drops by 10% (`loss = loss * 0.9`). Print the loss at each epoch.

Stop training when **either**:
- you reach 100 epochs, **or**
- the loss falls below `0.01` — then print `Early stopping triggered` and `break`.

```
Epoch 1  | Loss: 0.9
Epoch 2  | Loss: 0.81
...
Epoch 44 | Loss: 0.00975
Early stopping triggered at epoch 44
```

**Hint:** `print(f"Epoch {i} | Loss: {loss:.5f}")` gives you clean output.

---

## P04 — Skip the Corrupted Rows ⭐⭐

You are cleaning a dataset. Loop through row numbers `1` to `30`. Some rows are corrupted —
say every row divisible by 7. **Skip** those with `continue` and count how many good rows
you processed.

```
Skipping corrupted row 7
Skipping corrupted row 14
Skipping corrupted row 21
Skipping corrupted row 28
Clean rows processed: 26
```

---

## P05 — Accuracy Function ⭐

Write a **function** `accuracy(correct, total)` that returns the accuracy as a percentage.
Call it three times with different numbers and print each result.

```
accuracy(87, 100)  ->  87.0
accuracy(45, 60)   ->  75.0
accuracy(9, 10)    ->  90.0
```

Then add a **guard**: if `total` is `0`, return `0` instead of crashing with a divide-by-zero.

---

## P06 — Activation Functions ⭐⭐

Activation functions are what let a neural network learn non-straight-line patterns.
Write three functions:

- `relu(x)` — returns `x` if `x > 0`, otherwise `0`
- `step(x)` — returns `1` if `x >= 0`, otherwise `0`
- `leaky_relu(x)` — returns `x` if `x > 0`, otherwise `0.01 * x`

Test each with the values `-5`, `0`, `3.7`.

```
relu(-5) = 0        step(-5) = 0        leaky_relu(-5) = -0.05
relu(0)  = 0        step(0)  = 1        leaky_relu(0)  = 0.0
relu(3.7)= 3.7      step(3.7)= 1        leaky_relu(3.7)= 3.7
```

**Bonus:** rewrite `relu` as a one-line **lambda**.

---

## P07 — Sigmoid without a Library ⭐⭐⭐

The **sigmoid** squashes any number into the range 0 to 1, which is how a model turns a raw
score into a probability.

```
sigmoid(x) = 1 / (1 + e^(-x))
```

You have not learned `import` yet, so approximate `e` as `2.718281828`.
Write `sigmoid(x)` and test it with `-10`, `-1`, `0`, `1`, `10`.

```
sigmoid(-10) = 0.0000454
sigmoid(0)   = 0.5
sigmoid(10)  = 0.9999546
```

**Notice:** the output never leaves 0–1, and `sigmoid(0)` is exactly `0.5`. That is why it
is perfect for yes/no predictions.

---

## P08 — Gradient Descent by Hand ⭐⭐⭐

This is THE algorithm that trains every AI model. We want to find the `x` that makes
`f(x) = x²` smallest (obviously `x = 0`, but let the computer discover it).

- Start at `x = 10`
- Learning rate = `0.1`
- The slope (gradient) of `x²` is `2 * x`
- On each of 50 steps: `x = x - (learning_rate * 2 * x)`
- Print `x` every 10 steps

```
Step 0  | x = 10.0
Step 10 | x = 1.073741824
Step 20 | x = 0.115292150
Step 30 | x = 0.012379400
Step 40 | x = 0.001329227
Step 50 | x = 0.000142724
Converged near x = 0
```

Then experiment: set the learning rate to `1.5` and watch `x` **explode** instead of
converging. That is exactly what "the learning rate is too high" means in practice.

---

## P09 — Mean Squared Error over Many Samples ⭐⭐

Given these paired actual and predicted values (you may hard-code them as two simple lists
and loop with `range(len(...))`):

```
actual    = [3.0, -0.5, 2.0, 7.0, 4.2]
predicted = [2.5,  0.0, 2.1, 7.8, 3.9]
```

Write a function `mse(actual, predicted)` that returns the **Mean Squared Error**:
average of `(actual - predicted) ** 2` over all pairs.

```
MSE: 0.238
```

Also write `mae(actual, predicted)` — the same thing but with `abs()` instead of squaring.

---

## P10 — Guess the Number (Binary Search Agent) ⭐⭐⭐

A tiny AI agent that finds a hidden number by halving the search space every time.

You think of a number between 1 and 100. The program guesses the middle of its current range,
you type `h` (too high), `l` (too low), or `c` (correct). It narrows down and guesses again.
Count the guesses.

```
Is it 50? (h/l/c): l
Is it 75? (h/l/c): h
Is it 62? (h/l/c): c
Found it in 3 guesses!
```

**Why this matters:** halving each time means 100 numbers takes at most 7 guesses, and
a million numbers takes only 20. This is the intuition behind decision trees.

---

## P11 — Fibonacci: Loop vs Recursion ⭐⭐⭐

Write `fib_loop(n)` using a `for` loop, and `fib_recursive(n)` that calls itself.
Print the first 15 Fibonacci numbers from each and confirm they match.

Then try `fib_recursive(35)` and notice how **slow** it is compared to `fib_loop(35)`.

**Why this matters:** the recursive version re-computes the same values thousands of times.
Storing results instead of recomputing is called **memoization**, and it is the same idea
behind caching in AI systems.

---

## P12 — Epoch Scheduler with Nested Loops ⭐⭐

Simulate training: 3 epochs, each with 4 batches. Print a line for every batch.

```
Epoch 1 | Batch 1
Epoch 1 | Batch 2
Epoch 1 | Batch 3
Epoch 1 | Batch 4
--- Epoch 1 complete ---
Epoch 2 | Batch 1
...
```

Then add a twist: if a batch number is `3` in epoch `2`, print `Batch failed, skipping` and
`continue` to the next batch.

---

## P13 — Learning Rate Decay ⭐⭐

Real training reduces the learning rate over time so the model can settle precisely.
Start at `lr = 0.1`. Every 5 epochs, halve it. Run 30 epochs and print the learning rate
each epoch.

```
Epoch 1  | LR: 0.1
...
Epoch 6  | LR: 0.05
...
Epoch 11 | LR: 0.025
```

**Hint:** `if epoch % 5 == 0:` is where the halving happens.

---

## P14 — Lambda Practice: Score Transformers ⭐⭐

Write these as **one-line lambdas**:

- `to_percent` — turns `0.87` into `87.0`
- `is_pass` — returns `True` if a score is `>= 0.5`
- `double` — doubles a number
- `clamp` — takes a score and forces it into the 0–1 range

Call each one and print the results.

```
to_percent(0.87) -> 87.0
is_pass(0.42)    -> False
double(21)       -> 42
clamp(1.7)       -> 1
```

---

### Checklist before you move on

- [ ] I can chain `if / elif / else` and I know only ONE branch runs
- [ ] I know when to use `while` (unknown count) vs `for` (known count)
- [ ] `break` exits the loop; `continue` skips to the next round
- [ ] I can write a function with parameters and a `return`
- [ ] I understand a function that returns nothing gives back `None`
- [ ] I can write a `lambda` for a one-line function
