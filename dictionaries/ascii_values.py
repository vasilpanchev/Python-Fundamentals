class LettersASCII:
    def __init__(self):
        self.ascii_dict = {}

    def convert_to_ascii(self, text: str) -> dict:
        self.ascii_dict = {letter: ord(letter) for letter in text.split(', ') if letter not in self.ascii_dict}
        return self.ascii_dict


def main():
    letters_ascii = LettersASCII()
    text = input()
    print(letters_ascii.convert_to_ascii(text))


if __name__ == "__main__":
    main()
