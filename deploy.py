from mangum import Mangum

from src.configs.base import app

handler = Mangum(app, lifespan="auto")
