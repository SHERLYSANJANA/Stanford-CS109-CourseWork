# CS109 Coursework: Probability, Statistics & Machine Learning

A collection of Python projects covering core concepts in probability, statistics, and machine learning — implemented from scratch using NumPy, without relying on high-level ML libraries like scikit-learn.

This repo brings together coursework completed across multiple problem sets, spanning statistical inference, resampling methods, and classic supervised learning classifiers.

## Repository Structure

```
.
├── classifiers/          # Naive Bayes & Logistic Regression classifiers
│   ├── naive_bayes.py
│   ├── logistic_regression.py
│   ├── questions.py
│   ├── test_classifiers.py
│   ├── test_questions.py
│   └── README.md
│
└── statistics/           # Expectation, variance, and hypothesis testing
    ├── cs109_pset5_email.py
    ├── cs109_pset5_hci.py
    ├── cs109_pset5_coursera.py
    └── README.md
```

## Projects

### 📊 [Statistical Inference & Resampling](./statistics/README.md)
Exercises in expectation, variance, bootstrap resampling, and permutation-based hypothesis testing — applied to keystroke timing data, peer grading data, and behavioral outcome data.

**Key concepts:** expectation & variance from raw data, bootstrap estimation of sampling variance, non-parametric permutation testing, p-value estimation.

### 🤖 [ML Classifiers from Scratch](./classifiers/README.md)
A Naive Bayes classifier and a Logistic Regression classifier, built from the ground up, applied to movie preference data, genetic ancestry data, and heart disease diagnostic data.

**Key concepts:** MLE vs. MAP estimation with Laplace smoothing, gradient ascent optimization, precision/recall evaluation, log-likelihood computation.

## Requirements

- Python ≥ 3.6
- NumPy

```bash
pip install numpy
```

Each project folder has its own README with specific run instructions.

## About This Repository

This work was completed as part of a university course covering probability, statistics, and introductory machine learning. The core algorithmic logic in each file (the parts implementing `fit()`, `predict()`, resampling loops, etc.) reflects my own work; the surrounding scaffolding — function signatures, docstrings, and test harnesses — was provided as starter code by course staff and is credited in each subproject's README.

This repo is shared publicly as a portfolio of coursework and personal learning. If you're a student currently taking a similar course, please use this as a reference for understanding concepts rather than as a source to copy from — plagiarizing coursework can have serious consequences, and the whole point of working through problems like these is what you learn by doing them yourself.

## Acknowledgments

See individual project READMEs for full acknowledgments of course staff and material authors.
