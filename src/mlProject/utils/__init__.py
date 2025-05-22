import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
log_filepath = os.path.join(log_dir,"running_logs.log")
 
logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers= [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
     
)

logger = logging.getLogger("mlProjectLogger")
