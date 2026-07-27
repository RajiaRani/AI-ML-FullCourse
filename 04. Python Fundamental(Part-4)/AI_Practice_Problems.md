# AI Practice Problems — Part 4 (OOP: Classes, Constructors, Encapsulation, Inheritance)

**Rule:** Use classes, `__init__`, instance methods, class methods (`@classmethod`),
static methods (`@staticmethod`), encapsulation (`_protected`, `__private`), and
inheritance — single, multi-level and multiple. Plus everything from Parts 1–3.

**Why OOP matters for AI:** every library you are about to learn is object oriented.
`model = LinearRegression()` then `model.fit(X, y)` then `model.predict(X)` — that is a
class, a constructor and two instance methods. Learn the pattern here and scikit-learn
will feel obvious.

Create one file per problem, e.g. `P01_dataset_class.py`.

---

## P01 — The Dataset Class ⭐⭐

Build a `Dataset` class that wraps a list of numbers.

**Constructor:** takes a `name` and a list of `values`.

**Instance methods:**
- `size()` — how many values
- `mean()` — the average
- `minimum()` / `maximum()`
- `describe()` — prints a summary
- `__str__` — so `print(dataset)` shows something readable

```
d = Dataset("Temperatures", [23.5, 19.8, 22.1, 25.0, 21.3])
print(d)
d.describe()
```
```
Dataset(Temperatures, 5 values)
Name  : Temperatures
Count : 5
Mean  : 22.34
Min   : 19.8
Max   : 25.0
```

---

## P02 — Class Variable: Counting Instances ⭐⭐

Add a **class variable** `total_datasets` to `Dataset` that counts how many `Dataset`
objects have ever been created. Add a `@classmethod` called `how_many()` that prints it.

```
d1 = Dataset("A", [1,2,3])
d2 = Dataset("B", [4,5,6])
d3 = Dataset("C", [7,8,9])
Dataset.how_many()      ->  3 datasets created
```

**The key idea:** `self.name` belongs to ONE object. `Dataset.total_datasets` is shared by
ALL objects. Your `Message` class in `11. Mini_Chat_System.py` already uses this pattern
with `message_counter` — same concept.

---

## P03 — Static Methods: A Maths Toolbox ⭐⭐

Add `@staticmethod`s to `Dataset` that do not need any object at all:

- `normalize(value, min_val, max_val)` — min-max scaling
- `squared_error(actual, predicted)`
- `is_valid_probability(p)` — `True` if `0 <= p <= 1`

```
Dataset.normalize(75, 50, 100)        ->  0.5
Dataset.squared_error(100, 118)       ->  324
Dataset.is_valid_probability(1.4)     ->  False
```

**When to use which:**
| | Needs the object's data? | Needs the class? |
|---|---|---|
| instance method (`self`) | yes | — |
| class method (`cls`) | no | yes |
| static method | no | no |

---

## P04 — Base Model Class ⭐⭐⭐

Create a `Model` base class — the blueprint every ML model follows.

**Constructor:** `name`, and set `self.is_trained = False`

**Methods:**
- `fit(X, y)` — sets `is_trained = True` and prints `Training {name}...`
- `predict(X)` — if not trained, print `Error: model is not trained yet` and return `None`.
  Otherwise return a list of predictions.
- `evaluate(X, y)` — predict, then return the MSE against `y`

```
m = Model("Baseline")
m.predict([1, 2, 3])     ->  Error: model is not trained yet
m.fit([1,2,3], [2,4,6])  ->  Training Baseline...
m.predict([1, 2, 3])     ->  [some predictions]
```

The `is_trained` guard is real — scikit-learn raises `NotFittedError` for exactly this.

---

## P05 — Inheritance: Three Model Types ⭐⭐⭐

Now inherit from `Model` and give each child its own `predict()`:

- `MeanModel` — always predicts the mean of the training `y`. (Sounds silly, but this is
  the **baseline** every real model must beat.)
- `LinearModel` — stores a `slope` and `intercept`, predicts `slope * x + intercept`
- `ThresholdModel` — a classifier: predicts `1` if `x > threshold` else `0`

```
mean_m = MeanModel("Mean Baseline")
mean_m.fit([1,2,3,4], [10, 20, 30, 40])
mean_m.predict([5, 6])          ->  [25.0, 25.0]

lin = LinearModel("Linear", slope=2, intercept=1)
lin.fit([1,2,3], [3,5,7])
lin.predict([4, 5])             ->  [9, 11]

clf = ThresholdModel("Classifier", threshold=0.5)
clf.fit([], [])
clf.predict([0.2, 0.9, 0.5])    ->  [0, 1, 0]
```

Then put all three in a list and loop over them calling `.predict()`. Each one behaves
differently even though the call is identical. **That is polymorphism.**

---

## P06 — Encapsulation: Protecting the Weights ⭐⭐⭐

A model's learned weights must never be changed from outside — otherwise the model silently
breaks. Rebuild `LinearModel` with:

- `self.__slope` and `self.__intercept` as **private** attributes
- `get_weights()` to read them
- `set_weights(slope, intercept)` to change them, but **only** if the model is not trained
  yet. Otherwise print `Cannot change weights of a trained model`.

```
m = LinearModel("Protected")
m.__slope                       ->  AttributeError
m.get_weights()                 ->  (2, 1)
m.set_weights(5, 0)             ->  Weights updated
m.fit([1,2],[3,5])
m.set_weights(9, 9)             ->  Cannot change weights of a trained model
```

**The lesson:** private attributes let you enforce rules. Without them, anyone can put your
object into an invalid state.

---

## P07 — Multi-Level Inheritance: The Neural Network Family ⭐⭐⭐

Build a three-level chain:

```
Layer  ->  DenseLayer  ->  OutputLayer
```

- `Layer` — has `name` and `num_neurons`, plus `info()`
- `DenseLayer(Layer)` — adds an `activation` ("relu" / "sigmoid") and a `forward(inputs)`
  method that applies the activation
- `OutputLayer(DenseLayer)` — adds `num_classes` and a `softmax_ready()` check

Use `super().__init__(...)` at every level. Then build a small network as a list of layers
and loop through printing each one's `info()`.

```
Layer 1: DenseLayer 'hidden1' | 128 neurons | relu
Layer 2: DenseLayer 'hidden2' | 64 neurons  | relu
Layer 3: OutputLayer 'output' | 10 neurons  | sigmoid | 10 classes
```

---

## P08 — Multiple Inheritance: A Mixin ⭐⭐⭐

Create two small standalone classes:

- `LoggerMixin` — has `log(message)` that prints `[LOG] {message}` and keeps a list of
  every message logged
- `TimerMixin` — has `start_timer()` and `stop_timer()` that track how many steps passed

Now create `TrainableModel(Model, LoggerMixin, TimerMixin)` that inherits from all three,
and make `fit()` log its progress.

```
m = TrainableModel("SmartModel")
m.fit([1,2,3], [2,4,6])
```
```
[LOG] Starting training for SmartModel
[LOG] Epoch 1 complete
[LOG] Epoch 2 complete
[LOG] Epoch 3 complete
[LOG] Training finished in 3 steps
```

Then print `TrainableModel.__mro__` to see the **Method Resolution Order** — the exact order
Python searches the parent classes. This is the thing that makes multiple inheritance
predictable instead of chaotic.

---

## P09 — Tokenizer as a Class ⭐⭐⭐

Turn your Part-3 tokenizer into a proper reusable class.

```python
class Tokenizer:
    def __init__(self, lowercase=True, remove_stopwords=False)
    def fit(self, corpus)          # builds the vocabulary
    def encode(self, text)         # text  -> list of ids
    def decode(self, ids)          # ids   -> text
    def vocab_size(self)
```

Keep the vocabulary **private** (`self.__vocab`) so nobody can corrupt it, and expose it
through a `get_vocab()` method.

```
t = Tokenizer(lowercase=True)
t.fit(["AI is great", "AI is the future"])
t.vocab_size()              ->  6
t.encode("AI is great")     ->  [0, 3, 2]
t.decode([0, 3, 2])         ->  "ai is great"
```

Handle the unknown-word case: if a word is not in the vocabulary, encode it as `-1` and
decode `-1` back to `<UNK>`. Every real tokenizer has an `<UNK>` token for exactly this.

---

## P10 — Chatbot with Inheritance ⭐⭐⭐

Fix and extend your `11. Mini_Chat_System.py` idea into a proper hierarchy.

- `Bot` (base) — has a `name` and a `respond(message)` that returns `"I don't understand"`
- `EchoBot(Bot)` — repeats the message back
- `RuleBot(Bot)` — has a dictionary of keyword → reply, and matches on keywords
- `SmartBot(RuleBot)` — falls back to the parent's reply via `super().respond()` when no
  keyword matches, and keeps a conversation history

```
bot = SmartBot("Aria")
bot.respond("hello")           ->  "Hi there! How can I help?"
bot.respond("what is python")  ->  "Python is a programming language."
bot.respond("blah blah")       ->  "I don't understand"
bot.show_history()             ->  prints all 3 exchanges
```

---

## P11 — Bank Account: Encapsulation Done Right ⭐⭐

The classic problem, because it teaches encapsulation better than anything else.

`BankAccount` with a **private** `__balance`:
- `deposit(amount)` — reject amounts `<= 0`
- `withdraw(amount)` — reject if more than the balance
- `get_balance()` — read-only access
- `transaction_history()` — list of every operation

Then `SavingsAccount(BankAccount)` adds `add_interest(rate)`, and
`CurrentAccount(BankAccount)` allows an overdraft up to a limit.

**The point:** `__balance` can only change through methods that validate first. Make it
public and one typo puts the account into an impossible state.

---

## P12 — Experiment Tracker ⭐⭐⭐

Every AI project needs one of these. Build `Experiment`:

- Constructor: `model_name`, `learning_rate`, `epochs`
- Class variable `all_experiments` — a list holding every experiment created
- `log_result(accuracy, loss)` — record one run
- `@classmethod best_experiment()` — returns the experiment with the highest accuracy
- `@classmethod compare_all()` — prints a table of every experiment
- `__str__` for readable output

```
e1 = Experiment("ResNet",  0.01,  50)
e2 = Experiment("VGG",     0.001, 100)
e3 = Experiment("MobileNet", 0.01, 30)
e1.log_result(0.91, 0.23)
e2.log_result(0.88, 0.31)
e3.log_result(0.94, 0.19)

Experiment.compare_all()
Experiment.best_experiment()   ->  MobileNet (accuracy 0.94)
```

This is a simplified version of MLflow and Weights & Biases — tools you will use for real.

---

### Checklist before you move on

- [ ] `self` is the object itself and must be the first parameter of every instance method
- [ ] `__init__` runs automatically when I create an object
- [ ] Class variables are shared by all objects; instance variables are not
- [ ] `@classmethod` gets `cls`, `@staticmethod` gets neither `self` nor `cls`
- [ ] `__str__` controls what `print(obj)` shows
- [ ] `super().__init__()` calls the parent constructor and I know why it is needed
- [ ] `__private` names are hidden from outside; `_protected` is a convention only
- [ ] I understand polymorphism: same method name, different behaviour per class

> **Note:** your file `11. Mini_Chat_System.py` currently has broken indentation in the
> `User` class (the methods are nested inside `__init__`). Fixing that file is a good
> warm-up before starting P10.
