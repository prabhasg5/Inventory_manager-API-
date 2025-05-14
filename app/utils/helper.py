# Helper utility functions for the application

import uuid
from datetime import datetime
from typing import Dict, Any


def generate_uuid() -> str:
    return str(uuid.uuid4())


def current_timestamp() -> datetime:
    return datetime.now()


def filter_none_values(data: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in data.items() if v is not None}


def is_in_stock(quantity: int) -> bool:
    return quantity > 0