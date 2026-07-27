# Prime AI/ML Batch — Python from Basics to Advanced

My Python learning repository, structured from fundamentals through to the AI/ML libraries.

Each folder contains an **`AI_Practice_Problems.md`** file with AI-flavoured problems that
use only the concepts taught up to that point — so nothing is ever blocked by something
not yet learned.

---

## Structure

| # | Folder | Topics | Practice Problems |
|---|---|---|---|
| 01 | [Python Fundamentals(Part 1)](01.%20Python%20Fundamentals%28Part%201%29/) | variables, operators, type conversion, input/output | [12 problems](01.%20Python%20Fundamentals%28Part%201%29/AI_Practice_Problems.md) |
| 02 | [Python Fundamentals(Part 2)](02.%20Python%20Fundamentals%28Part%202%29/) | conditionals, match-case, loops, break/continue, functions, lambda | [14 problems](02.%20Python%20Fundamentals%28Part%202%29/AI_Practice_Problems.md) |
| 03 | [Python_Fundamentals(Part-3)](03.%20Python_Fundamentals%28Part-3%29/) | strings, slicing, lists, tuples, dictionaries, sets | [15 problems](03.%20Python_Fundamentals%28Part-3%29/AI_Practice_Problems.md) |
| 04 | [Python Fundamental(Part-4)](04.%20Python%20Fundamental%28Part-4%29/) | OOP — classes, constructors, encapsulation, inheritance | [12 problems](04.%20Python%20Fundamental%28Part-4%29/AI_Practice_Problems.md) |
| 05 | [Python Fundamental(Part-5)](05.%20Python%20Fundamental%28Part-5%29/) | file handling, exceptions, modules, comprehensions, NumPy, pandas | [20 problems](05.%20Python%20Fundamental%28Part-5%29/AI_Practice_Problems.md) |

**73 practice problems total.**

---

## How to use the practice files

1. Open the folder you are currently studying
2. Open `AI_Practice_Problems.md`
3. Pick a problem and create a file for it — e.g. `P03_neuron.py`
4. Solve it **without** looking at hints first; the hints are there for when you are stuck
5. Tick off the checklist at the bottom of the file before moving to the next folder

Difficulty is marked ⭐ (easy) to ⭐⭐⭐⭐ (challenging).

---

## The thread running through all five parts

The same AI concepts reappear at every level, each time with better tools:

| Concept | Part 1 | Part 2 | Part 3 | Part 4 | Part 5 |
|---|---|---|---|---|---|
| **A neuron** | one line of arithmetic | a function with an activation | — | a `Layer` class | `np.dot()` on a whole layer |
| **Accuracy** | one calculation | a reusable function | a confusion matrix | a model `.evaluate()` method | a pandas column |
| **Tokenizing** | — | — | lists, sets and dicts | a `Tokenizer` class | — |
| **A dataset** | two numbers | a hard-coded list | a list of dictionaries | a `Dataset` class | a pandas DataFrame |

Watching the same idea get cleaner as the tools improve is the fastest way to understand
why each new concept exists.

---

## Setup

```bash
python3 --version          # 3.10 or newer (match-case needs 3.10+)
pip install numpy pandas   # needed for Part 5 only
```

---

## Roadmap after Part 5

1. **scikit-learn** — `train_test_split`, regression, classification, `fit`/`predict`/`score`
2. **Matplotlib & Seaborn** — visualising data and model results
3. **Model evaluation** — cross-validation, precision/recall/F1, ROC curves
4. **Deep learning** — PyTorch or TensorFlow
5. **LLMs** — the Claude API, prompting, RAG, agents
