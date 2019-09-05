import os

from src.app import app
from config.config import *
if __name__ == '__main__':
    if os.environ['ENV'] == "Development":
        app.run(host=DevelopmentConfig.HOST, port=DevelopmentConfig.port)
    elif os.environ['ENV'] == "Production":
        app.run(host=ProductionConfig.HOST, port=ProductionConfig.port)
    else:
        app.run(host=TestingConfig.HOST, port=TestingConfig.port)