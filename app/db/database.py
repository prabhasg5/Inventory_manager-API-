from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator
from couchbase.options import ClusterOptions
from app.config import (
    COUCHBASE_HOST, 
    COUCHBASE_USERNAME, 
    COUCHBASE_PASSWORD,
    COUCHBASE_BUCKET,
    COUCHBASE_COLLECTION
)
import logging
import json
from datetime import datetime

logger = logging.getLogger(__name__)

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

class Database:
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
            
        try:
            auth = PasswordAuthenticator(
                COUCHBASE_USERNAME,
                COUCHBASE_PASSWORD
            )
       
            self.cluster = Cluster(COUCHBASE_HOST, ClusterOptions(auth))
            self.bucket = self.cluster.bucket(COUCHBASE_BUCKET)
            self.collection = self.bucket.collection(COUCHBASE_COLLECTION)
            
            try:
                query = f"SELECT COUNT(*) FROM system:indexes WHERE keyspace_id = '{COUCHBASE_BUCKET}' AND is_primary = true"
                result = self.cluster.query(query)
                count = next(result).get('$1', 0)
                if count == 0:
                    self.cluster.query(f"CREATE PRIMARY INDEX ON {COUCHBASE_BUCKET}").execute()
                    logger.info(f"Created primary index on {COUCHBASE_BUCKET}")
            except Exception as e:
                logger.warning(f"Error handling primary index: {str(e)}")
            
            logger.info(f"Connected to Couchbase at {COUCHBASE_HOST}")
            self._initialized = True
            
        except Exception as e:
            logger.error(f"Failed to initialize Couchbase connection: {str(e)}")
            raise
    def _prepare_data_for_storage(self, data):
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, datetime):
                    data[key] = value.isoformat()
                elif isinstance(value, (dict, list)):
                    data[key] = self._prepare_data_for_storage(value)
        elif isinstance(data, list):
            return [self._prepare_data_for_storage(item) for item in data]
        return data
    
    async def get_item(self, item_id: str):
        try:
            result = self.collection.get(item_id)
            return result.content_as[dict]
        except Exception as e:
            logger.error(f"Error retrieving item {item_id}: {str(e)}")
            return None
    
    async def get_all_items(self):
        try:
            query = f"SELECT * FROM `{COUCHBASE_BUCKET}`.`_default`.`{COUCHBASE_COLLECTION}` WHERE type = 'inventory_item'"
            result = self.cluster.query(query)
            return [row[COUCHBASE_COLLECTION] for row in result] 
        except Exception as e:
            logger.error(f"Error retrieving all items: {str(e)}")
            return []
    
    async def create_item(self, item_id: str, item_data: dict):
        try:
            item_data["type"] = "inventory_item"
            processed_data = self._prepare_data_for_storage(item_data)
            
            self.collection.upsert(item_id, processed_data)
            return item_data
        except Exception as e:
            logger.error(f"Error creating item: {str(e)}")
            return None
    
    async def update_item(self, item_id: str, item_data: dict):
        try:
            existing = await self.get_item(item_id)
            if not existing:
                return None
            processed_data = self._prepare_data_for_storage(item_data)
            
            self.collection.replace(item_id, processed_data)
            return item_data
        except Exception as e:
            logger.error(f"Error updating item {item_id}: {str(e)}")
            return None
    
    async def delete_item(self, item_id: str):
        try:
            existing = await self.get_item(item_id)
            if not existing:
                return False

            self.collection.remove(item_id)
            return True
        except Exception as e:
            logger.error(f"Error deleting item {item_id}: {str(e)}")
            return False

db = Database()