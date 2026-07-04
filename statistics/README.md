# Probability & Statistics: Expectation, Variance, and Hypothesis Testing

A set of small statistical analysis exercises implemented in Python and NumPy, covering expectation/variance estimation, bootstrap resampling, and permutation-based hypothesis testing — applied to real-world-style datasets (keystroke timing data, peer grading data, and learning outcomes data).

This project was completed as coursework covering foundational probability and statistics concepts.

## What's Inside

### `cs109_pset5_email.py` — Keystroke Dynamics & Authorship Identification
Uses expectation and variance to identify which of two candidate typists most likely produced a given piece of text, based on keystroke timing patterns.
- **`get_expectation(filepath)`** — Computes E[X], the expected value of a keystroke timing random variable, from a timing dataset.
- **`get_squared_expectation(filepath)`** — Computes E[X²], used alongside `get_expectation` to derive variance (Var(X) = E[X²] − E[X]²) and standard deviation.
- **`optional_function()`** — Uses a z-score comparison against two candidate typists' timing distributions to predict who wrote a given sample of text.

### `cs109_pset5_hci.py` — Bootstrap Estimation of Sampling Variance
Explores how much a summary statistic (mean vs. median) varies from one small random sample to another, using bootstrap resampling.
- **`get_sample_mean(filepath)`** — Computes the mean of a grades dataset.
- **`get_mean_var(filepath, seed)`** — Estimates the variance of the sample mean via 10,000 rounds of bootstrap resampling (sampling with replacement).
- **`get_median_var(filepath, seed)`** — Same idea, but estimates the variance of the sample median instead.

### `cs109_pset5_coursera.py` — Permutation Testing for Difference in Means
Tests whether an observed difference between two groups' outcomes is statistically significant, using a non-parametric permutation test.
- **`diff_sample_means(filepath)`** — Computes the absolute difference in sample means between two activity groups.
- **`estimate_p_val(filepath, seed)`** — Runs a 10,000-iteration resampling procedure to estimate a p-value for the observed difference in means, testing the null hypothesis that group membership has no effect on outcome.

## Key Concepts Demonstrated
- Expectation and variance from raw frequency data
- Bootstrap resampling to estimate the sampling distribution of a statistic
- Permutation/resampling-based hypothesis testing and p-value estimation
- Working with `np.random.choice` for reproducible random sampling

## Running the Project

Requires Python ≥ 3.6 and NumPy.

```bash
pip install numpy

python cs109_pset5_email.py
python cs109_pset5_hci.py
python cs109_pset5_coursera.py
```

Each script's `main()` runs the implemented functions against the provided datasets and prints the results.

## Notes on Structure
- Each script expects a `cs109_pset5_util.py` helper module (providing `get_filepath()`) and a `datasets/` folder containing the relevant `.csv`/`.txt` files. These support files aren't included in this repo — see the note below.
- As with my other coursework repos, the surrounding scaffolding (function signatures, docstrings, autograder-facing comments) was provided by course staff; the implementations inside each function are my own.

## Acknowledgments
Assignment assembled by:
- Lisa Yan
- Anand Shankar (CS109 TA)
