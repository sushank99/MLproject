# Student Performance Outcome Prediction

## Overview

This project predicts student performance based on various features such as gender, race, parental education level, and test scores. It uses machine learning models to analyze the input data and predict the student's performance in mathematics.

## Project Structure

1. **Data Ingestion (`data_ingestion.py`)**: Handles data reading, splitting, and saving.
2. **Data Transformation (`data_transformation.py`)**: Preprocesses data for model training.
3. **Model Training (`model_trainer.py`)**: Trains and evaluates different machine learning models.
4. **Prediction Pipeline (`predict_pipeline.py`)**: Provides an interface for making predictions with trained models.
5. **Utilities (`utils.py`)**: Contains helper functions for saving/loading models and evaluating performance.
6. **Web Application (`app.py`)**: A Flask-based web application for interacting with the prediction model.
7. **Requirements File (`requirements.txt`)**: Lists the Python packages required for the project.

## Setup

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/sushank99/Student-Performace-Outcome-Prediction.git
   cd student-performance-prediction
