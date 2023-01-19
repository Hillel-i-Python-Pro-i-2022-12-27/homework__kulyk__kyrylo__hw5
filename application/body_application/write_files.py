from application.body_application.generators import generate_users
from application.config.paths import FILES_INPUT_PATH


def to_write_file_txt() -> None:
    path_to_file = FILES_INPUT_PATH.joinpath("any_file.txt")
    amount: int = 100
    with open(path_to_file, mode="w") as file:
        for user in generate_users(amount=amount):
            file.write(f"{user.name} {user.email}\n")


if __name__ == "__main__":
    to_write_file_txt()
