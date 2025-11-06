import os
import sys
from user_dashboard.config import Config
from user_dashboard.routes import app

if __name__ == '__main__':
    config = Config(os.environ.get('ENV', 'dev'))
    app.config.from_object(config)
    app.run(debug=config.DEBUG, port=config.PORT)