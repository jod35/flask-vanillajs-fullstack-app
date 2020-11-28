from main import create_app
from main.config import Config

if __name__ == "__main__":
    app=create_app(Config)
    app.run()
    