import fastapi
from fastapi import routing
from starlette.requests import Request
from starlette.responses import Response
import starlette





def home(request: Request):
    result = Response(content="<html> <head> </head><body>FUCK YOU</body><\html>")





def main(*args, **kwargs):
    app = fastapi.FastAPI()

    app.route("/", home)

    

    









if __name__ == "__main__":
    main()
