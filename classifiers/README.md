# ML Classifiers from Scratch: Naive Bayes & Logistic Regression

A from-scratch implementation of two classic supervised machine learning classifiers — **Naive Bayes** and **Logistic Regression** — built using only Python and NumPy (no scikit-learn). Includes an inference module that answers real-world questions (genetics, movie recommendations, and heart disease prediction) using the trained models.

This project was completed as part of a probability & statistics course covering foundational machine learning concepts.

## What's Inside

### Classifiers
- **`naive_bayes.py`** — A Naive Bayes classifier that learns label and feature frequency counts from training data, then uses (optionally Laplace-smoothed) likelihood estimates to classify new examples.
- **`logistic_regression.py`** — A Logistic Regression classifier trained via gradient ascent on the log-likelihood, using the sigmoid function to model class probabilities.

### Inference / Analysis
- **`questions.py`** — Uses the trained classifiers to answer applied questions across three datasets:
  - **Netflix dataset**: estimating the probability a user likes *Love Actually*, and identifying the movies most predictive of that preference.
  - **Ancestry dataset**: estimating the probability that a genetic marker (SNP) matches the reference genome, conditioned on ancestry.
  - **Heart dataset**: identifying the strongest predictors of heart disease, and computing precision/recall on a held-out test set.

### Testing
- **`test_classifiers.py`** — Verifies that `fit()` and `predict()` produce correct label counts, feature counts, learned weights, and prediction accuracy across all datasets.
- **`test_questions.py`** — Verifies that the applied inference questions in `questions.py` return correct results.

## How It Works

**Naive Bayes**
1. `fit()` counts how often each label occurs, and how often each (feature, value, label) combination occurs in the training data.
2. `predict()` uses these counts to compute the (log) unnormalized probability of each label for a new sample, optionally applying Laplace add-one smoothing, and predicts the higher-probability label.

**Logistic Regression**
1. `fit()` performs gradient ascent on the log-likelihood to learn a weight vector (`theta`), including a bias term.
2. `predict()` applies the sigmoid function to the linear combination of learned weights and input features, predicting label `1` when the resulting probability is ≥ 0.5.

## Running the Project

Requires Python ≥ 3.6 and NumPy.

```bash
# Install dependencies
pip install numpy

# Run all classifier tests
python test_classifiers.py

# Run all inference/question tests
python test_questions.py

# Run specific tests only
python test_classifiers.py predict_bayes_mle_simple fit_logistic_heart
```

You can also experiment directly in a Python shell:

```python
import numpy as np
from naive_bayes import NaiveBayes

n = NaiveBayes(use_mle=True)
n.fit(np.array([[0,0,0,0], [1,1,1,1], [1,0,1,0]]), np.array([1, 0, 1]))
n.predict(np.array([[0,1,0,1], [1,0,1,0]]))
# array([0, 1], dtype=uint8)
```

## Key Concepts Demonstrated
- Maximum Likelihood Estimation (MLE) vs. Maximum A Posteriori (MAP) estimation with Laplace smoothing
- Log-likelihood and numerical stability tricks for probabilistic classifiers
- Gradient ascent optimization for logistic regression
- Model evaluation: accuracy, precision, and recall
- Vectorized NumPy operations for performance

## Datasets
Three datasets were used to test and demonstrate the classifiers:
- A small toy ("simple") dataset for sanity-checking correctness
- A Netflix movie-preference dataset
- A genetic ancestry (SNP) dataset
- A heart disease diagnostic dataset

*(Note: raw dataset files are not included in this repository — see note below.)*

## Notes
- This project was originally developed as a course assignment. The classifier and question logic above reflects my own implementation, written into instructor-provided starter files.
- Because the surrounding scaffolding (docstrings, test harness, assignment instructions) was authored by course staff rather than by me, I've kept the original authorship/acknowledgment notes intact below, and left dataset files out of this repo pending confirmation that redistribution is permitted.

## Acknowledgments
Course materials, starter code, and datasets were provided by:
- Tim Gianitsos — classifiers, solution code, code questions, autograder, instructions
- Anand Shankar — comments, spec, autograder
- Alex Tsun — comments, repo maintenance
- Lisa Yan — spec, questions
- Chris Piech — questions and datasets
- Mehran Sahami — questions
