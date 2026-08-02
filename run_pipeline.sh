#!/bin/bash

echo "======================================"
echo "Customer Churn LTV Pipeline"
echo "======================================"

echo ""
echo "Step 1: Formatting Code..."
black .

echo ""
echo "Step 2: Running Linter..."
flake8 .

echo ""
echo "Step 3: Training Baseline Model..."
python src/ml/train_baseline.py

echo ""
echo "Step 4: Training Ensemble Model..."
python src/ml/train_ensemble.py

echo ""
echo "Step 5: Exporting Models..."
python src/ml/export_models.py

echo ""
echo "Step 6: Running Unit Tests..."
pytest

echo ""
echo "Step 7: Generating Coverage Report..."
pytest --cov=app --cov-report=html

echo ""
echo "======================================"
echo "Pipeline Completed Successfully!"
echo "======================================"