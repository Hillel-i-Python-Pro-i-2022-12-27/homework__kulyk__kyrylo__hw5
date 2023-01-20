from application.body_application.create_files_txt import to_create_file_txt
from application.body_application.read_files import to_read_file_txt
from application.body_application.write_files import to_write_file_txt
from application.logging.init_logging import init_logging
from application.requests_example.requests_data import to_requests_data
from application.requests_example.response_processing import to_processing_response


def main() -> None:
    print("Hello world!")
    to_create_file_txt(name_file="fake_text")
    to_read_file_txt(name_file="fake_text")
    to_write_file_txt(name_file="users", amount_users=5)
    to_requests_data(url="http://api.open-notify.org/astros.json")
    to_processing_response("output")


if __name__ == "__main__":
    init_logging()
    main()
