from modules.hash import Hash

class Interface:
    __modules = {
        "hash": Hash
    }
    def __init__(self):
        print("hello")

    def run(self):
        while True:
            print("Please choose the desired module:")
            print("\tencode")
            print("\tdecode")
            print("\tweb-request")
            print("\thash")
            print("\tquit")
            chosen_option = input()
            match chosen_option:
                case "encode":
                    pass
                case "decode":
                    pass
                case "web-request":
                    pass
                case "hash":
                    Hash()

                case "quit":
                    break

        print("Bye")