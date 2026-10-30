import hashlib


class HashCLI:
    def __init__(self, hashing_service):
        self.__hashing_service = hashing_service

    def run(self) -> None:
        print("You have chosen hash module.")
        print("Please choose one of the following options:")
        print("\t1 - create a hash")
        print("\t2 - crack a hash using a wordlist")

        option = input().strip()
        if option not in ("1", "2"):
            print("ERROR: Unrecognized option.")
            return

        text = input("Please enter the text:\n").strip()

        print(f"Supported hashing algorithms:\n{self.__hashing_service.get_supported_hashing_algorithms()}")
        algorithm = input("Please choose the hashing algorithm:\n").strip()

        if option == "1":
            try:
                result = self.__hashing_service.create_hash(text, algorithm)
                print(f"\nGenerated hash:\n{result}\n")

            except ValueError as e:
                print(f"ERROR: {e}")

            except Exception as e:
                print(f"UNEXPECTED ERROR: {e}")

        elif option == "2":
            wordlist_path = input("Please provide the path to the wordlist.\n").strip()
            try:
                word, tries = self.__hashing_service.crack_hash(text, algorithm, wordlist_path)

                if word is not None:
                    print(f"\nMatch found: {word}")
                    print(f"Hash cracked after {tries} tries.\n")

                else:
                    print("Text not found in the wordlist.")

            except FileNotFoundError:
                print(f"ERROR: File {wordlist_path} not found.")

            except PermissionError:
                print(f"ERROR: Permission denied: {wordlist_path}.")

            except ValueError as e:
                print(f"ERROR: {e}")

class HashService:
    def __init__(self):
        self.__hashing_algorithms = hashlib.algorithms_available


    def get_supported_hashing_algorithms(self):
        return self.__hashing_algorithms

    def create_hash(self, text, algorithm):
        if algorithm in self.__hashing_algorithms:
            hasher = hashlib.new(algorithm)
            hasher.update(text.encode("utf-8"))
            return hasher.hexdigest()

        raise ValueError(f"Unrecognized hashing algorithm: {algorithm}")

    def crack_hash(self, hashed_text, algorithm, wordlist):
        if algorithm not in self.__hashing_algorithms:
            raise ValueError(f"Unrecognized hashing algorithm: {algorithm}")

        with open(f"{wordlist}", "r", errors="ignore", encoding="utf-8") as f:
            base_hasher = hashlib.new(algorithm)
            for num, line in enumerate(f, start=1):
                hasher = base_hasher.copy()
                hasher.update(line.strip().encode("utf-8"))

                checksum = hasher.hexdigest()
                if checksum == hashed_text:
                    return line.strip(), num

        return None, None