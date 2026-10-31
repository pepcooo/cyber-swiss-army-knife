from modules.hash import HashService, HashCLI
from modules.encode import EncodeService, EncodeCLI
from modules.web_request import WebRequestCLI, WebRequestService


class Interface:
    __modules = {
        "hash": HashCLI,
        "encode": EncodeCLI,
        "web-request": WebRequestCLI
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
                    service = EncodeService()
                    cli = EncodeCLI(service)
                    cli.run()

                case "web-request":
                    service = WebRequestService()
                    cli = WebRequestCLI(service)
                    cli.run()

                case "hash":
                    service = HashService()
                    cli = HashCLI(service)
                    cli.run()

                case "quit":
                    break

        print("Bye")