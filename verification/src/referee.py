import logging

from checkio_referee import RefereeBase, ENV_NAME

logger = logging.getLogger(__name__)

import settings_env
from tests import TESTS


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "striped_words"
    FUNCTION_NAMES = {
        ENV_NAME.JS_NODE: "stripedWords"
    }

    def __init__(self, *args, **kwargs):
        logger.error('First error')
        logger.error('Second error', extra={
            'stack': True,
        })
        super(Referee, self).__init__(*args, **kwargs)
