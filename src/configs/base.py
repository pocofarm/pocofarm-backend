from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from . import settings
from ..middlewares.base import attach_base_middleware


app = FastAPI(redoc_url=settings.redoc_url, docs_url=settings.docs_url)
app = attach_base_middleware(app)


@app.get("/", response_class=PlainTextResponse)
async def hello_pocofarm() -> str:
    """
    Hello PocoFarm
    """
    return """
                              ▄▄▄▄▄                  _________________
                              ▀▀▀██████▄▄▄          /  PocoFarm      \\
                            ▄▄▄▄▄  █████████▄       |  Gotta go fast! |
                            ▀▀▀▀█████▌ ▀▐▄ ▀▐█      | ________________/
                          ▀▀█████▄▄ ▀██████▄██      |/ 
                          ▀▄▄▄▄▄  ▀▀█▄▀█════█▀         
                              ▀▀▀▄  ▀▀███ ▀      ▄▄   
                            ▄███▀▀██▄████████▄ ▄▀▀▀██▌ 
                          ██▀▄▄▄██▀▄███▀ ▀▀████     ▀█▄
                      ▄▀▀▀▄██▄▀▀▌████▒▒▒▒▒▒███    ▌▄▄▀
                      ▌    ▐▀████▐███▒▒▒▒▒▐██▌        
                      ▀▄  ▄▀   ▀▀████▒▒▒▒▄██▀         
                        ▀▀      ▀▀█████████▀          
                              ▄▄██▀██████▀█           
                            ▄██▀     ▀▀▀  █           
                            ▄█             ▐▌          
                        ▄▄▄▄█▌              ▀█▄▄▄▄▀▀▄  
                       ▌     ▐                ▀▀▄▄▄▀   
                        ▀▀▄▄▀                          
        """
