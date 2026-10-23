class Interface:
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
                    break

                case "decode":
                    break

                case "web-request":
                    break

                case "hash":
                    break

                case "quit":
                    break

        print("Bye")