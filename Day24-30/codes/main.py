from fastapi import FastAPI,Depends
from database import Product
import database_model
from database_config import session, engine
from sqlalchemy.orm import Session



app = FastAPI()

database_model.Base.metadata.create_all(bind=engine)

products = [
    Product(id = 1,name = "phone",description = "Sumsang", price = 15000, quantity = 200),
    Product(id = 2,name = "phone",description = "iphone", price = 16000, quantity = 300)
    ]

#intialize data base
def init_db():
    db = session()
    count = db.query(database_model.Product).count()
    if count == 0:
        try:
            for i in products:
                db.add(database_model.Product(**i.model_dump()))
        finally:
             db.commit()
init_db()
    

#create dependency
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

#get all data from data base
@app.get("/product")
def get_db_product(db:Session = Depends(get_db)):
    db_product = db.query(database_model.Product).all()
    return db_product

#get filtered data from data base
@app.get("/product/{id}")
def get_db_product(id:int, db:Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        return db_product
    return{"message":"item not found"}
    


    
