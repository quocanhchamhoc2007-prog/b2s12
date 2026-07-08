from fastapi import FastAPI ,Depends ,status ,HTTPException
from sqlalchemy.orm import Session 
from database import get_db
from sqlalchemy import Text
from serviec import get_all_class_svr ,get_class_by_id ,update_class,delete_class
from schema import createclass ,uppdate_class
app = FastAPI()

@app.get('/test')
def get_test(db:Session = Depends(get_db)) :
    try :
        db.execute('select 1')
        return {'message' : 'succese'}
    except :
        return {"message" : 'lỗi'}

@app.get('/classroom')
def get_all_class(db:Session = Depends(get_db)) :
    list_class = get_all_class_svr(db)
    return {
        "message" : 'lỗi',
        "data" : list_class
    }
# lấy thông tin theo id 

@app.get('/classroom/{id}')
def get_class_bt_id (db : Session = Depends(get_db)) :
    classroom = get_class_by_id(db, id) 
    return {
        "message" : 'seccese',
        "data" : classroom
    }

#  thêm sinh viên 
@app.post("/classroom")
def create_class(new_class:createclass ,db:Session = Depends(get_db)) :
    classroom = create_class(db,new_class)
    return {
        "message" : 'seccese',
        "data" : classroom
    }
    

#  sửa
@app.put('/classroom/{id}')
def update_class(update_clas : uppdate_class , db:Session = Depends(get_db)) :
    class_romm = update_class(id ,db,update_clas)
    return {
        "message" : 'seccese',
        "data" : class_romm
    }

# xoá 
@app.delete("/classroom/{id}")
def delete(db:Session =Depends(get_db)):
    class_room = delete_class(db ,id)
    return {
        'message' :'succes',
        'data' : class_room
    }

