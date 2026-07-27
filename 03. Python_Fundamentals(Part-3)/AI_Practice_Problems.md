# AI Practice Problems — Part 3 (Strings, Lists, Tuples, Dictionaries, Sets)

**Rule:** Use only what you learned up to this folder — strings and slicing, f-strings,
lists and list methods, tuples, dictionaries and their methods, sets and set operations,
plus everything from Parts 1 and 2.

This is the most important folder for AI. **Almost all real data preprocessing is
dictionary and list work.** Take your time here.

Create one file per problem, e.g. `P01_tokenizer.py`.

---

## P01 — Build a Tokenizer ⭐⭐

Every language model starts by breaking text into **tokens**. Write a simple word tokenizer.

Given a sentence, produce a list of lowercase words with punctuation stripped.

```
Input : "AI is Amazing, and AI is the FUTURE!"
Tokens: ['ai', 'is', 'amazing', 'and', 'ai', 'is', 'the', 'future']
```

**Hints:** `.lower()`, `.replace()` to remove `,` `.` `!` `?`, then `.split()`.

---

## P02 — Vocabulary Builder ⭐⭐

Take the tokens from P01 and build the model's **vocabulary** — every unique word, sorted.

```
Vocabulary: ['ai', 'amazing', 'and', 'future', 'is', 'the']
Vocab size: 6
```

**Hint:** a `set` removes duplicates automatically, then `sorted()` puts it in order.

---

## P03 — Word to Index Mapping ⭐⭐

Models cannot read words, only numbers. Convert your vocabulary into a dictionary that maps
each word to a number, then **encode** the original sentence.

```
Word to index: {'ai': 0, 'amazing': 1, 'and': 2, 'future': 3, 'is': 4, 'the': 5}
Encoded      : [0, 4, 1, 2, 0, 4, 5, 3]
```

**Bonus:** build the reverse dictionary (`index -> word`) and **decode** the numbers back
into the sentence. You just built the input and output layer of a language model.

---

## P04 — Word Frequency Counter ⭐⭐

Count how many times each word appears in a paragraph, then print the **top 5 most common**.

```
Input: "the cat sat on the mat the cat was happy"

the   : 3
cat   : 2
sat   : 1
on    : 1
mat   : 1
```

**Hints:** loop through the tokens and use `dict.get(word, 0) + 1` to build the counts.
For sorting, `sorted(counts.items(), key=lambda item: item[1], reverse=True)`.

---

## P05 — Stopword Removal ⭐⭐

Common words like `the`, `is`, `a`, `and` carry no meaning, so we throw them away before
training. Given a stopword **set** and a token list, produce the filtered tokens.

```
stopwords = {"the", "is", "a", "an", "and", "of", "to", "in", "on", "was"}

Before: ['the', 'cat', 'sat', 'on', 'the', 'mat', 'and', 'was', 'happy']
After : ['cat', 'sat', 'mat', 'happy']
Removed 5 stopwords.
```

**Why a set and not a list?** Checking `word in my_set` is instant no matter how big the set
gets, while `word in my_list` has to scan every item. With 10,000 stopwords that difference
is enormous. This is a real performance decision you will make again and again.

---

## P06 — Bag of Words Vector ⭐⭐⭐

Turn a sentence into a **numeric vector** the model can actually consume.

Given a fixed vocabulary, produce a list where each position holds the count of that
vocabulary word in the sentence.

```
vocabulary = ['ai', 'is', 'good', 'bad', 'model']
sentence   = "ai is good ai is good model"

Vector: [2, 2, 2, 0, 1]
```

Do this for three different sentences and print all three vectors. Congratulations — you
just built a **feature matrix**.

---

## P07 — Confusion Matrix ⭐⭐⭐

The single most important table in classification. Given the true labels and predicted
labels for a spam filter, count the four outcomes.

```
actual    = ['spam', 'ham', 'spam', 'spam', 'ham', 'ham', 'spam', 'ham']
predicted = ['spam', 'ham', 'ham',  'spam', 'spam','ham', 'spam', 'ham']
```

Count and print:
- **True Positive** — actual spam, predicted spam
- **True Negative** — actual ham, predicted ham
- **False Positive** — actual ham, predicted spam (a real email sent to junk — annoying)
- **False Negative** — actual spam, predicted ham (spam reaching the inbox — worse)

```
TP: 3   FP: 1
FN: 1   TN: 3

Accuracy : 0.75
Precision: 0.75
Recall   : 0.75
```

**Formulas:** `precision = TP / (TP + FP)`, `recall = TP / (TP + FN)`.
Precision answers *"when it says spam, is it right?"*. Recall answers *"did it catch all
the spam?"*. A model can score high on one and terribly on the other.

---

## P08 — Student Performance Dataset ⭐⭐

Given a list of dictionaries (this is exactly how JSON data arrives from an API):

```python
students = [
    {"name": "Alice",   "maths": 88, "science": 92, "english": 79},
    {"name": "Bob",     "maths": 45, "science": 61, "english": 55},
    {"name": "Charlie", "maths": 95, "science": 89, "english": 91},
    {"name": "Diana",   "maths": 67, "science": 72, "english": 84},
    {"name": "Eshan",   "maths": 30, "science": 41, "english": 38},
]
```

Print:
1. Each student's name, total and average
2. The class average for each subject
3. The topper of each subject
4. Every student whose average is below 50 (`At risk`)

```
Alice   | Total: 259 | Average: 86.33
Bob     | Total: 161 | Average: 53.67
...
Class average - maths: 65.0, science: 71.0, english: 69.4
Topper - maths: Charlie, science: Alice, english: Charlie
At risk: Eshan
```

---

## P09 — Missing Value Handler ⭐⭐⭐

Real datasets are full of holes. Given a list of readings where missing values are `None`,
replace each `None` with the **mean of the values that are present** (this is called
*mean imputation*).

```
Before: [23.5, None, 19.8, 22.1, None, 25.0, 21.3]
Mean of known values: 22.34
After : [23.5, 22.34, 19.8, 22.1, 22.34, 25.0, 21.3]
Filled 2 missing values.
```

**Hint:** first pass to collect the non-`None` values and compute the mean, second pass to
fill. You cannot do it in one pass — you need the mean before you can fill anything.

---

## P10 — Outlier Detection ⭐⭐⭐

An outlier is a value far from the rest. Use the rule: anything more than **2 standard
deviations** from the mean is an outlier.

```
data = [12, 14, 13, 15, 12, 98, 14, 13, 11, 15, 14, 2]

Mean: 20.25
Std : 24.66
Outliers found: [98]
Clean data: [12, 14, 13, 15, 12, 14, 13, 11, 15, 14, 2]
```

**Standard deviation without a library:**
1. mean = sum / count
2. for each value compute `(value - mean) ** 2`
3. variance = average of those squares
4. std = `variance ** 0.5`

---

## P11 — Set Operations on Datasets ⭐⭐

Two teams labelled images independently:

```
team_a = {"img_01", "img_02", "img_03", "img_05", "img_08", "img_09"}
team_b = {"img_02", "img_04", "img_05", "img_07", "img_09", "img_10"}
```

Print:
- Images **both** teams labelled (intersection) — these can be checked for agreement
- Images labelled by **either** team (union) — total coverage
- Images **only** team A did (difference)
- Images exactly one team did (symmetric difference) — these have no second opinion
- The **agreement rate**: `len(intersection) / len(union)`

```
Both       : {'img_02', 'img_05', 'img_09'}
Either     : {'img_01', ..., 'img_10'}
Only A     : {'img_01', 'img_03', 'img_08'}
Only one   : {'img_01', 'img_03', 'img_04', 'img_07', 'img_08', 'img_10'}
Agreement  : 0.33
```

That agreement rate is a real metric — it is called **Jaccard similarity** and it is used
everywhere from recommendation systems to plagiarism detection.

---

## P12 — Chat History Manager ⭐⭐⭐

An AI chatbot stores conversation history as a list of dictionaries:

```python
history = [
    {"role": "user",      "content": "What is machine learning?"},
    {"role": "assistant", "content": "Machine learning is a field of AI..."},
    {"role": "user",      "content": "Give me an example"},
    {"role": "assistant", "content": "Spam filters learn from labelled emails..."},
]
```

Write code that:
1. Prints the conversation nicely formatted
2. Counts how many turns each role took
3. Finds the **longest** message and who sent it
4. Estimates total tokens (rough rule: `len(text) / 4`)
5. Keeps only the **last 2 messages** (context window trimming) — use slicing

```
USER      : What is machine learning?
ASSISTANT : Machine learning is a field of AI...

Turns  - user: 2, assistant: 2
Longest message by: assistant (58 chars)
Estimated tokens: 34
Trimmed history: 2 messages kept
```

**Why trimming matters:** every model has a context limit. When a chat gets too long you
must drop old messages or the request fails. This exact code runs in every chat app.

---

## P13 — Palindrome and Anagram Detector ⭐⭐

Classic interview questions, and both are pure string and set work.

1. `is_palindrome(text)` — ignore spaces, punctuation and case.
   `"A man, a plan, a canal, Panama"` → `True`
2. `is_anagram(a, b)` — do two words use exactly the same letters?
   `"listen"`, `"silent"` → `True`

**Hint for the palindrome:** clean the string first, then compare it to `cleaned[::-1]`.

---

## P14 — N-Gram Generator ⭐⭐⭐

Before neural networks, language models predicted the next word using **n-grams** — groups
of N consecutive words.

Given `"the quick brown fox jumps"`, generate:

```
Bigrams  (n=2): [('the','quick'), ('quick','brown'), ('brown','fox'), ('fox','jumps')]
Trigrams (n=3): [('the','quick','brown'), ('quick','brown','fox'), ('brown','fox','jumps')]
```

Write it as a function `ngrams(tokens, n)` that works for any `n`.

**Hint:** `for i in range(len(tokens) - n + 1)` then slice `tokens[i : i+n]` and make it a
tuple. Why a tuple and not a list? Because tuples can be dictionary keys — and the next step
of a real n-gram model is counting how often each n-gram appears.

---

## P15 — Recommendation Engine ⭐⭐⭐

Given what each user watched, recommend movies to a target user based on the person with
the most similar taste.

```python
watched = {
    "raj":   {"Inception", "Interstellar", "The Matrix", "Arrival"},
    "priya": {"Inception", "The Matrix", "Tenet", "Dune"},
    "amit":  {"Titanic", "The Notebook", "La La Land"},
    "sara":  {"Interstellar", "Arrival", "Dune", "Inception"},
}
```

For the user `raj`:
1. Compute the Jaccard similarity against every other user
2. Find the most similar user
3. Recommend the movies that user watched but `raj` has not

```
Similarity with priya: 0.33
Similarity with amit : 0.0
Similarity with sara : 0.6

Most similar to raj: sara
Recommended for raj: {'Dune'}
```

This is **collaborative filtering** — the actual algorithm behind Netflix and Spotify
recommendations, just at a much larger scale.

---

### Checklist before you move on

- [ ] Strings are **immutable** — `.upper()` returns a new string, it does not change the original
- [ ] I can slice with `[start:stop:step]` and I know `[::-1]` reverses
- [ ] Lists are mutable, tuples are not — and only tuples can be dictionary keys
- [ ] I use `dict.get(key, default)` instead of crashing on a missing key
- [ ] I know when a **set** is the right choice (uniqueness, fast membership tests)
- [ ] I can loop over a dictionary with `.items()`, `.keys()`, `.values()`
- [ ] I can sort with a `key=lambda` function
