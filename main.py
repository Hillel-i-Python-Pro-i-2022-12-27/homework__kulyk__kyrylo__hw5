from application.body_application.read_files import to_read_file_txt
from application.body_application.write_files import to_write_file_txt
from application.logging.init_logging import init_logging


def main() -> None:
    print("Hello world!")
    to_write_file_txt()
    to_read_file_txt()


if __name__ == "__main__":
    init_logging()
    main()
