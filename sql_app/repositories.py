
from sqlalchemy.orm import Session

from . import models, schemas


class ItemRepo:
    
 async def create(db: Session, item: schemas.ItemCreate):
        db_item = models.Item(name=item.name,price=item.price,description=item.description,store_id=item.store_id)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
 def fetch_by_id(db: Session,_id):
     return db.query(models.Item).filter(models.Item.id == _id).first()
 
 def fetch_by_name(db: Session,name):
     return db.query(models.Item).filter(models.Item.name == name).first()
 
 def fetch_all(db: Session, skip: int = 0, limit: int = 100):
     return db.query(models.Item).offset(skip).limit(limit).all()
 
 async def delete(db: Session,item_id):
     db_item= db.query(models.Item).filter_by(id=item_id).first()
     db.delete(db_item)
     db.commit()
     
     
 async def update(db: Session,item_data):
    updated_item = db.merge(item_data)
    db.commit()
    return updated_item
    
    
    
class StoreRepo:
    
    async def create(db: Session, store: schemas.StoreCreate):
            db_store = models.Store(name=store.name)
            db.add(db_store)
            db.commit()
            db.refresh(db_store)
            return db_store
        
    def fetch_by_id(db: Session,_id:int):
        return db.query(models.Store).filter(models.Store.id == _id).first()
    
    def fetch_by_name(db: Session,name:str):
        return db.query(models.Store).filter(models.Store.name == name).first()
    
    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Store).offset(skip).limit(limit).all()
    
    async def delete(db: Session,_id:int):
        db_store= db.query(models.Store).filter_by(id=_id).first()
        db.delete(db_store)
        db.commit()
        
    async def update(db: Session,store_data):
        db.merge(store_data)
        db.commit()