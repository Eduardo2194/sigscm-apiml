from datetime import datetime
from fastapi import APIRouter,UploadFile
from controller.testingController import testCSV
from typing import List

router = APIRouter()


@router.post("/test", tags=["test"])
async def test(start:str,end:str):
#async def test(file: UploadFile,start:str,end:str):
    date_format = "%Y-%m-%d"
    a = datetime.strptime(start, date_format)
    b = datetime.strptime(end, date_format)
    delta = b - a
    if(delta.days == 7):
        result = await testCSV(start,end)
    else:
        result = 'La diferencia debe ser de 7 dias | Ej: 2022-09-20 - 2022-09-27'    
    return result