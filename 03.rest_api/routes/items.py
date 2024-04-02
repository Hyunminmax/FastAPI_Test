from fastapi import APIRouter, Depends, HTTPException
import crud_orm
from sqlalchemy.orm import Session

import schemas
from dependencies import get_db

router = APIRouter(prefix='/api/v1/items')


# api/v1/item
@router.post('/')
def create_item(create_item: schemas.ItemCreate, owner_id: int, db: Session = Depends(get_db)):
    item = crud_orm.create_item(db, create_item, owner_id)
    return item


@router.get('/{item_id}')
def get_item(item_id: int, db: Session = Depends(get_db)):
    return crud_orm.get_item(db, item_id)


@router.get('/')
def get_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_orm.get_items(db, skip, limit)


@router.put('/{item_id}')
def update_item(item_id: int, item_update: schemas.ItemUpdate, db: Session = Depends(get_db)):
    return crud_orm.update_item(db, item_id, item_update)


@router.delete('/{item_id}')
def delete_item(item_id: int, db: Session = Depends(get_db)):
    is_success = crud_orm.delete_item(db, item_id)
    if not is_success:
        raise HTTPException(404, 'Fail to delete item')
    return {'msg': 'Item delete success'}
