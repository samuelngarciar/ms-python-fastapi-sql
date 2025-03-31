from fastapi import FastAPI
from app.api import endpoints
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s:  %(message)s')
logger = logging.getLogger(__name__)

logger.info("Start app")
app = FastAPI()
app.include_router(endpoints.router)