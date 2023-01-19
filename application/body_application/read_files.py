from application.config.paths import FILES_INPUT_PATH
from application.logging.loggers import get_core_logger


def to_read_file_txt() -> None:
    logger = get_core_logger()
    path_to_file = FILES_INPUT_PATH.joinpath("any_file.txt")
    logger.info(f"Path to file: file://{path_to_file}")
    file_contents = path_to_file.read_text()
    print(file_contents)


if __name__ == "__main__":
    to_read_file_txt()
