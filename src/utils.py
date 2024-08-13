import os
import sys
import numpy as np
import pandas as pd
from exception import CustomException
from logger import logging
import dill
from sklearn.metrics import r2_score
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

def save_object(file_path, obj):
    try:
        dir_name = os.path.dirname(file_path)

        os.makedirs(dir_name, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
def evalute_model(x_train, y_train, x_test, y_test, models):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            
            model.fit(x_train, y_train) #train the model

            y_train_pred = model.predict(x_train)

            y_test_predict = model.predict(x_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_predict)

            report[list(models.values())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e,sys)