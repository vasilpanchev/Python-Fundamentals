def get_file_name(file: str) -> str:
    slash_index = file.rfind("\\")
    dot_index = file.rfind('.')
    file_name = file[slash_index + 1:dot_index]
    return file_name


def get_file_extension(file: str) -> str:
    dot_index = file.rfind('.')
    file_extension = file[dot_index + 1:]
    return file_extension


def main():
    file = input()
    print(f"File name: {get_file_name(file)}")
    print(f"File extension: {get_file_extension(file)}")


if __name__ == "__main__":
    main()
