from base import app
from base.utiles.logger import get_logger

logger = get_logger()

if __name__ == '__main__':
    logger.info('Server Start ===========')
    app.run(port=8000, debug=True)
