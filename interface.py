from modules.hash import Hash
from modules.encode import Encode


class Interface:
    __modules = {
        "hash": Hash,
        "encode": Encode
    }
    def __init__(self):
        print("hello")

    def run(self):
        while True:
            print("Please choose the desired module:")
            print("\tencode")
            print("\tweb-request")
            print("\thash")
            print("\tquit")
            chosen_option = input().strip().lower()
            match chosen_option:
                case "encode":
                    Encode()
                case "web-request":
                    pass
                case "hash":
                    Hash()
                    break
                case "quit":
                    break

        print("Bye")