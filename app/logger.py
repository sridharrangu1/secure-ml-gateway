# app/logger.py
import logging

logging.basicConfig(
    filename="access.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def log_access(user, role, endpoint, status):
    logging.info(f"{user} | {role} | {endpoint} | {status}")
