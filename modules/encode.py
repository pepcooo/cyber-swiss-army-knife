import urllib.parse
import base64


class EncodeService:
    def __init__(self):
        self.__standard_encodings = {
            "utf-8"         :   "utf-8",
            "utf-16"        :   "utf-16",
            "utf-32"        :   "utf-32",
            "latin-1"       :   "iso8859",
            "latin-2"       :   "iso8859-2",
            "windows-1252" :    "cp1252",
            "windows-1250" :    "cp1250"
        }

        self.__custom_encodings = {
            "base64" : "base64",
            "url" : "url",
        }

    def get_supported_encodings(self):
        return list(self.__standard_encodings.keys()) + list (self.__custom_encodings.keys())

    def encode(self, text, encoding):
        if encoding in self.__standard_encodings:
            scheme = self.__standard_encodings[encoding]
            return text.encode(scheme).hex()

        else:
            if encoding == "base64":
                return base64.b64encode(text.encode()).decode()

            elif encoding == "url":
                return urllib.parse.quote(text.encode())

        raise ValueError(f"Unrecognized encoding: {encoding}")


    def decode(self, text, encoding):
        if encoding in self.__standard_encodings:
            scheme = self.__standard_encodings[encoding]
            return bytes.fromhex(text).decode(scheme)

        else:
            if encoding == "base64":
                return base64.b64decode(text.encode()).decode()

            elif encoding == "url":
                return urllib.parse.unquote(text.encode())

        raise ValueError(f"Unrecognized encoding: {encoding}")

class EncodeCLI:
    def __init__(self, service : EncodeService):
        self.__service = service

    def run(self) -> None:
        print("You have chosen the encode module.")
        print("Please specify what you wish to do by entering the appropriate number.")
        print("\t1 - encode text")
        print("\t2 - decode text")

        option = input().strip()
        if option not in ("1", "2"):
            print("ERROR: Unrecognized option.")
            return

        text = input("Please enter the text:\n").strip()

        print(f"Available encodings:\n{self.__service.get_supported_encodings()}")
        encoding = input("Please specify the encoding:\n").strip()

        try:
            if option == "1":
                result = self.__service.encode(text, encoding)
            else:
                result = self.__service.decode(text, encoding)

            print(f"Result:\n{result}")

        except Exception as e:
            print(f"ERROR: {e}")