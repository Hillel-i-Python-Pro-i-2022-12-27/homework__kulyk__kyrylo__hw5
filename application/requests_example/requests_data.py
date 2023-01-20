import json

import requests

from application.config.paths import FILES_OUTPUT_PATH
from application.logging.loggers import get_core_logger


def to_requests_data() -> None:
    logger = get_core_logger()
    url = "http://api.open-notify.org/astros.json"

    path = FILES_OUTPUT_PATH.joinpath("output.json")

    with requests.Session() as session:
        response = session.get(url)
        logger.info(f"{response}")
        response_json = response.json()
        logger.info(f"{response_json=}")

        path.write_text(json.dumps(response_json, indent=2))
