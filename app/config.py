import os
from dotenv import load_dotenv
load_dotenv()
COUCHBASE_HOST = os.getenv("COUCHBASE_HOST", "localhost")
COUCHBASE_USERNAME = os.getenv("COUCHBASE_USERNAME", "Administrator")
COUCHBASE_PASSWORD = os.getenv("COUCHBASE_PASSWORD", "password")
COUCHBASE_BUCKET = os.getenv("COUCHBASE_BUCKET", "inventory")
COUCHBASE_COLLECTION = os.getenv("COUCHBASE_COLLECTION", "items")
API_V1_STR = "/api/v1"
PROJECT_NAME = "Inventory Manager API"