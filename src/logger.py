import logging
import os
from datetime import datetime

# Create a timestamped log file name
LOG_FILE = f"{datetime.now().strftime('%y_%m_%d_%H_%M_%S')}.log"
# Define the log file path
logs_path = os.path.join(os.getcwd(), "logs")
# Create the logs directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Complete log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Test logging
if __name__ == "__main__":
    logging.info("Logging has started")
