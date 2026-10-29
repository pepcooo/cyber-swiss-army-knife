import urllib.parse
import base64

class Encode:
    __encodings = [
        "base64",
        "url",
        "utf-8",
        "utf-16",
        "utf-32",
        "latin-1",
        "latin-2",
        "windows-1252",
        "windows-1250"
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

            case "latin-1":
                result = text.encode("latin-1").hex()

            case "latin-2":
                result = text.encode("iso8859-2").hex()

            case "windows-1252":
                result = text.encode("cp1252").hex()

            case "windows-1250":
                result = text.encode("cp1250").hex()

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

            case "latin-1":
                result = bytes.fromhex(text).decode("latin-1")

            case "latin-2":
                result = bytes.fromhex(text).decode("iso8859-2")

            case "windows-1252":
                result = bytes.fromhex(text).decode("cp1252")

            case "windows-1250":
                result = bytes.fromhex(text).decode("cp1250")

        return result