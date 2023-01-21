import json

from application.config.paths import FILES_OUTPUT_PATH


def to_processing_response(name_file: str = None) -> None:
    path_to_file = FILES_OUTPUT_PATH.joinpath(f"{name_file}.json")
    with open(path_to_file) as file:
        response_dict = json.load(file)
    number_of_astronauts = response_dict.get("number", {})
    print(f"The number of people in space at this moment: {number_of_astronauts}-astronauts")


if __name__ == "__main__":
    to_processing_response()
