from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4
from datetime import datetime

class ItemBase(BaseModel):
    name: str = Field(..., description="Name of the item")
    category: str = Field(..., description="Category the item")
    price: float = Field(..., gt=0, description="Price of the item (>0)")
    quantity: int = Field(..., ge=0, description="Available stock")
    description: Optional[str] = Field(None, description="description ")
    in_stock: bool = Field(True, description="Wheather the item is in stock")
    
class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    quantity: Optional[int] = Field(None, ge=0)
    description: Optional[str] = None
    in_stock: Optional[bool] = None

class ItemInDB(ItemBase):
    id: str = Field(default_factory=lambda: str(uuid4()))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Config:
        populate_by_name = True

class Item(ItemInDB):
    pass