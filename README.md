# Telecom_sony

Portfolio Data Science

## Install the requirement packages using pip

> pip install -r requirements.txt

# The Goal

To expose how the conventional, manual preprocessing workflow inflates your metrics and why pipelines are not optional if you care about real performance on unseen data.

The Jupyter Notebook perform the conventional way and the modular programming implements the pipeline that encode, scales, train.

## 1. The Conventional Way (Manual Preprocessing)

### What People Usually Do

1. Take the full training dataset
2. Apply preprocessing once:

   - Scaling
   - Encoding
   - SMOTE or other resampling

3. Feed the transformed data into:
   - Cross-validation
   - Hyperparameter search
   - Final model training

On the surface, this looks clean and efficient.

### The Actual Problem: Data Leakage

This approach breaks the core assumption of cross-validation.

The validation folds has already seen the data, because you have alredy have preprocess the dataset upfront:

- Scalers compute statistics using future validation data
- Encoders learn category distributions from all folds
- SMOTE creates synthetic samples influenced by data that should be held out

Your model is indirectly trained on information it was never supposed to see. **That’s leakage.**

## 2. The Pipeline Method (Correct Way)

In this method, you package the transformations and the model into a single Pipeline. You pass raw data into the Pipeline.

### What Happens During Cross-Validation

For every fold:

- The training split is isolated
- Preprocessing is fit only on that split
- The validation split stays untouched
- The model is evaluated honestly

Every fold stands on its own—no shared statistics, no synthetic samples leaking across folds, and zero opportunity for the model to cheat.
