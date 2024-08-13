import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import traceback

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message
        self.error_detail = error_detail

    def error_message_details(self):
        _, _, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        error_message = f"Error occurred in file [{file_name}] at line [{exc_tb.tb_lineno}] with message [{self.error_message}]"
        return error_message

    
