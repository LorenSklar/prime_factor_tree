import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Default limits for integer validation
LOWER_LIMIT = int(os.getenv('LOWER_LIMIT', -1000))
UPPER_LIMIT = int(os.getenv('UPPER_LIMIT', 1000)) 