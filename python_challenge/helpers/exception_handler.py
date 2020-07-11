import logging

from sqlalchemy.exc import CompileError, IntegrityError
from werkzeug.exceptions import HTTPException, BadRequest

logger = logging.getLogger(__name__)


def handle_error(error: Exception):
    if isinstance(error, HTTPException):
        raise error
    if isinstance(error, (CompileError, IntegrityError)):
        raise BadRequest()
    logger.exception('Unexpected error')
