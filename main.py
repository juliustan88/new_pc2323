import fastapi
import uvicorn
from uvicorn import run

print("hello, fast api")

api = fastapi.FastAPI()


@api.get("/")  # decorator
def endpoint():  # endpoint function
    return {
        "msg": "hello world here",
        "list of port": [8000, 9000, 6789],
    }


run(api, port=9000)
