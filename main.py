# from fastapi import FastAPI, UploadFile, File
# from io import BytesIO
# from PIL import Image
# from predict import predict
#
# app = FastAPI()
#
# @app.post("/predict/image")
# def predict_img(file: UploadFile = File(...)):
#     img = Image.open(BytesIO(file.read()))
#     result = predict(img)
#
#     return result

# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run("main:app", reload=True)

# 민호님 코드
from fastapi import FastAPI, UploadFile, File
from io import BytesIO
from PIL import Image
from predict import predict
import uvicorn

app = FastAPI()

@app.post('/predict/image')
async def predict_img(file: UploadFile=File(...)):
    img = Image.open(BytesIO(await file.read()))
    result = predict(img)

    return result

if __name__ == '_main':
    uvicorn.run('main:app', reload=True)

# 재훈님 코드
# from fastapi import FastAPI, File, UploadFile
# from PIL import Image
# from io import BytesIO
# from predict import predict
# import uvicorn
#
# app = FastAPI()
#
# @app.post("/predict/image")
# async def predict_api(file: UploadFile = File(...)):
#     extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
#     if not extension:
#         return "Image must be jpg or png format!"
#     image = Image.open(BytesIO(await file.read()))
#     prediction = predict(image)
#     return prediction
#
# if __name__ == "__main__":
#     uvicorn.run('main:app', reload=True)







# 노션 코드 안됨.
# from fastapi import FastAPI, File, UploadFile
# from PIL import Image
# from io import BytesIO
# from predict import predict
#
# app = FastAPI()
#
# @app.post("/predict/image")
# async def predict_api(file: UploadFile = File(...)):
#     extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
#     if not extension:
#         return "Image must be jpg or png format!"
#     image = Image.open(BytesIO(await file.read()))
#     prediction = predict(image)
#     return prediction
#
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, reload=True)