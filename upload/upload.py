from fastapi import FastAPI, File, UploadFile

app = FastAPI()

"""

uvicorn upload:app --reload
"""


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):

    data = await file.read()
    print(data)

    return {"filename": file.filename}
