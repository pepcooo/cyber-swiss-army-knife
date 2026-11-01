import socket
import ssl

class WebRequestService:
    def __init__(self):
        self.__request = "GET / HTTP/1.1\r\nHost: Bazinga.com\r\nConnection: close\r\n\r\n"
        self.__port = 80
        self.__use_ssl = False


    def _extract_host(self) -> str:
        for line in self.__request.splitlines():
            if line.lower().startswith("host:"):
                return line.split(":")[1].strip()

        raise ValueError("Host header not found in the request.")


    def send_request(self) -> str:
        host = self._extract_host()
        port = self.__port

        raw_sock = socket.create_connection((host, port), timeout=10)
        if self.__use_ssl:
            context = ssl.create_default_context()
            sock = context.wrap_socket(raw_sock, server_hostname=host)
        else:
            sock = raw_sock

        with sock:
            sock.sendall(self.__request.encode("utf-8"))

            response_chunks = []
            while True:
                data = sock.recv(4096)
                if not data:
                    break
                response_chunks.append(data)

        raw_response = b"".join(response_chunks).decode("utf-8", errors="replace")
        return raw_response


    def set_port(self, port) -> None:
        if not port.isdigit():
            raise ValueError("Port is not a number.")
        elif int(port) < 0 or int(port) > 65535:
            raise ValueError("Port number must be between 0 and 65535.")

        self.__port = int(port)


    def set_request(self, new_request) -> None:
        new_request = new_request.replace("\\r\\n", "\r\n")
        self.__request = new_request


    def toggle_ssl(self) -> None:
        self.__use_ssl = not self.__use_ssl


    def get_request(self) -> str:
        return self.__request


    def get_port(self) -> int:
        return self.__port


    def get_ssl(self) -> bool:
        return self.__use_ssl


class WebRequestCLI:
    def __init__(self, service):
        self.__service = service


    def run(self) -> None:
        print("You have chosen the web-request module.")
        while True:
            print("Current state of the request:\n")
            print(self.__service.get_request())
            print("\nPlease choose one of the following options:")
            print("\t1 - modify the request")
            print(f"\t2 - specify port ({self.__service.get_port()})")
            print(f"\t3 - use ssl ({self.__service.get_ssl()})")
            print("\t4 - send the custom request")
            print("\t5 - go back to menu")

            chosen_option = input().strip()

            if chosen_option not in ("1", "2", "3", "4", "5"):
                print("ERROR: Unrecognized option")
                return

            try:
                if chosen_option == "1":
                    new_req = input("Please enter the request, with lines being separated by \\r\\n.\n")
                    self.__service.set_request(new_req)

                elif chosen_option == "2":
                    port = input("Please enter the port number:\n").strip()
                    self.__service.set_port(port)

                elif chosen_option == "3":
                    self.__service.toggle_ssl()

                elif chosen_option == "4":
                    response = self.__service.send_request()
                    print("Server response:\n")
                    print(response)

                else:
                    break

            except Exception as e:
                print(f"ERROR: {e}")