import urllib.parse
import base64

class Encode:
    __encodings = [
        "base64",
        "url",
        "utf-8",
        "utf-16",
        "utf-32"
    ]
    def __init__(self):
        self.__options = {
            1: self.encode,
            2: self.decode
        }
        print("You have chosen the encode module.")
        self.run()


    def run(self):
        print("Please specify what you wish to do by entering the appropriate number.")
        print("\t1 - encode text")
        print("\t2 - decode text")

        option = input().strip()
        print(self.__options[int(option)]())

    def encode(self):
        print("Please enter the text to encode.")
        text = input().strip()

        print("Please specify the encoding.")
        print("Available encodings:")
        print(self.__encodings)
        encoding = input().strip()

        if encoding not in self.__encodings:
            print("ERROR: Unrecognized encoding.")
            return 1

        result = ""
        match encoding:
            case "base64":
                result = base64.b64encode(text.encode()).decode()

            case "url":
                result = urllib.parse.quote(text.encode())

            case "utf-8":
                result = text.encode("utf-8").hex()

            case "utf-16":
                result = text.encode("utf-16").hex()

            case "utf-32":
                result = text.encode("utf-32").hex()

        return result


    def decode(self):
        print("Please enter the text to decode.")
        text = input().strip()

        print("Please specify the encoding.")
        print("Available encodings:")
        print(self.__encodings)
        encoding = input().strip()

        if encoding not in self.__encodings:
            print("ERROR: Unrecognized encoding.")
            return 1

        result = ""
        match encoding:
            case "base64":
                result = base64.b64decode(text.encode()).decode()

            case "url":
                result = urllib.parse.unquote(text.encode())

            case "utf-8":
                result = bytes.fromhex(text).decode("utf-8")

            case "utf-16":
                result = bytes.fromhex(text).decode("utf-16")

            case "utf-32":
                result = bytes.fromhex(text).decode("utf-32")

        return result