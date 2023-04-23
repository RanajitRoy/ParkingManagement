from _dbaccess import _DBAccessObj
from fastapi import FastAPI, UploadFile

app = FastAPI()
_dbao = _DBAccessObj(host="172.28.80.1")


@app.get("/is_reg/{name}/{plate_no}")
async def reg_users(name: str, plate_no : str) -> bool:
    return _dbao.is_registered(name, plate_no)

@app.get("/user/img/")
async def create_upload_file(file: UploadFile) -> bool:
    return False

@app.post("/user/{name}/{plate_no}")
async def reg_users(name: str, plate_no : str) -> bool:
    return _dbao.register_user(name, plate_no)

@app.delete("/user/{name}/{plate_no}")
async def reg_users(name: str, plate_no : str) -> int:
    return _dbao.unregister_user(name, plate_no)