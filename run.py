from my_app import app
from config import DevelopmentConfig
app.config.from_object("config.DevelopmentConfig")
if __name__ == "__main__":
    app.run(port = DevelopmentConfig.PORT)