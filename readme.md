# Student Performance Outcome Prediction

## Overview

The **Student Performance Outcome Prediction** project aims to predict students' mathematics scores based on various features including gender, ethnicity, parental education level, lunch status, and test preparation course completion. Utilizing machine learning algorithms, this project provides insights into student performance and helps in identifying factors that influence academic success.


![image](https://github.com/user-attachments/assets/2cdce8b4-8a09-463e-a667-15d44f13a6c1)

![image](https://github.com/user-attachments/assets/825aeccf-3e3f-4818-933b-d4a94112e6e9)


## Project Structure

- **`data_ingestion.py`**: Manages the ingestion of raw data, including splitting and saving datasets.
- **`data_transformation.py`**: Preprocesses data by handling missing values and scaling features.
- **`model_trainer.py`**: Trains multiple machine learning models, evaluates their performance, and selects the best model.
- **`predict_pipeline.py`**: Provides a prediction interface using the trained model and preprocessing object.
- **`utils.py`**: Contains utility functions for model management and evaluation.
- **`app.py`**: Implements a Flask web application for user interaction and prediction.
- **`setup.py`**: Sets up the project environment and dependencies.
- **`exception.py`**: Defines custom exceptions for error handling.
- **`logger.py`**: Configures logging to track events and errors during execution.

## Features

- **Data Ingestion**: Reads, splits, and stores raw data for further processing.
- **Data Transformation**: Prepares data by handling missing values and normalizing features.
- **Model Training**: Trains and evaluates various machine learning models to identify the best performer.
- **Prediction Pipeline**: Allows users to input data and receive predictions on student performance.
- **Web Application**: Provides a user-friendly interface for making predictions and viewing results.

## Installation

### Prerequisites

- Python 3.9
- Pandas
- Flask
- Pip (Python package installer)

### Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/sushank99/Student-Performace-Outcome-Prediction.git
   cd student-performance-prediction
### **Run Applicaton File**
- To start the web application, use:

   ```bash
   python app.py     
### How to Use the Web Application
- Navigate to http://localhost:5001 in your web browser.
- Fill in the form with the required student details.
- Submit the form to receive the predicted mathematics score.
