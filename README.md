# Fraud Detection Pipeline

This project implements a full fraud-detection workflow built around the NeurIPS Fraud Detection dataset. The notebook covers end-to-end preprocessing, dimensionality reduction, resampling, model training, and evaluation.

## Overview
The workflow cleans and standardizes the raw dataset, applies PCA for dimensionality reduction, and uses NearMiss undersampling to address the strong class imbalance. Multiple models were tested, with LightGBM performing the strongest after hyperparameter tuning.

## Model Performance
The tuned LightGBM model achieved a ROC–AUC of approximately 0.87 on held-out validation data. The notebook includes cross-validation scores, ROC curves, and diagnostics illustrating model behavior.

## API Integration
The entire pipeline (preprocessing → inference → evaluation tools) is packaged behind a FastAPI interface for deployment, although the API code itself is not included in this repository.

## Structure
- `notebook.ipynb` — data processing, PCA, NearMiss workflow, LightGBM training, and ROC–AUC evaluation  
- `requirements.txt` — core dependencies  
- `models/` — trained model artifacts (excluded via `.gitignore`)

## Dataset
This project uses the **NeurIPS Fraud Detection** dataset, which provides transaction-level features suitable for supervised classification benchmarks.

## Notes
Large artifacts are intentionally excluded via `.gitignore` to keep the repository lightweight.
