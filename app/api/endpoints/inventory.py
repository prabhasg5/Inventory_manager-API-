from fastapi import APIRouter, HTTPException, status
from app.models.inventory import ItemCreate, Item, ItemUpdate
from app.db.database import db
from typing import List
from datetime import datetime

router = APIRouter()

@router.get("/", response_model=List[Item])
async def get_all_items():
    
    items = await db.get_all_items()
    return items

@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: str):
    
    item = await db.get_item(item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )
    return item

@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    
    new_item = Item(
        **item.model_dump(),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    result = await db.create_item(new_item.id, new_item.model_dump())
    
    if not result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create item"
        )
    
    return new_item

@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: str, item_update: ItemUpdate):

    existing_item = await db.get_item(item_id)
    if not existing_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )
    update_data = item_update.model_dump(exclude_unset=True)
    if not update_data:
        return Item(**existing_item)
    updated_item = {**existing_item, **update_data, "updated_at": datetime.now()}
    result = await db.update_item(item_id, updated_item)
    
    if not result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update item"
        )
    
    return Item(**updated_item)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: str):
    success = await db.delete_item(item_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )
    
    return None  