import os
import sys
import numpy as np
import pandas as pd
from exception import CustomException
from logger import logging
import dill
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
