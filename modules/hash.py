import hashlib

class Hash:
    def __init__(self):
        self.__hashing_algorithms = hashlib.algorithms_available
        self.__options = {
            1: self.create_hash,
            2: self.crack_hash
        }
        print("You have chosen the hash module.")
        self.run()


    def run(self):
        print("Please specify what you wish to do by entering the appropriate number.")
        print("\t1 - create a hash")
        print("\t2 - try to crack a hash using a wordlist")

        option = input().strip()
        self.__options[int(option)]()


    def create_hash(self):
        print("Please provide a string of characters to hash.")
        text = input().strip()

        print("Now, please provide a hashing algorithm.")
        print("Supported hashing algorithms:")
        print(self.__hashing_algorithms)
        algorithm = input().strip()

        if algorithm not in self.__hashing_algorithms:
            print("Error: Unknown hashing algorithm.")
            return 1

        try:
            hasher = hashlib.new(algorithm)
            hasher.update(text.encode("utf-8"))
            result = hasher.hexdigest()
            print(result)

        except ValueError:
            print("Error: Invalid hashing algorithm (hashlib unrecognized).")


    def crack_hash(self):
        print("Please enter the hash you wish to crack.")
        hash_to_crack = input().strip().split(" ")[0]
        if not hash_to_crack:
            print("ERROR: Invalid hash provided.")
            return 1

        print("Please enter the hashing algorithm.")
        print("Supported hashing algorithms:")
        print(self.__hashing_algorithms)
        hashing_algorithm = input().strip().split(" ")[0]
        if not hashing_algorithm or hashing_algorithm not in self.__hashing_algorithms:
            print("ERROR: Invalid algorithm provided.")
            return 1

        print("Please enter the path to the wordlist.")
        wordlist_path = input().strip().split(" ")[0]
        if not wordlist_path:
            print("ERROR: Invalid wordlist provided.")
            return 1


        try:
            with open(wordlist_path, "r") as f:
                # base_hasher is used for efficiency, as copying (.copy()) is faster than creating new hasling elemtn each iteration
                base_hasher = hashlib.new(hashing_algorithm)
                for num, line in enumerate(f, start=1):
                    hasher = base_hasher.copy()
                    hasher.update(line.strip().encode("utf-8"))

                    checksum = hasher.hexdigest()
                    if checksum == hash_to_crack:
                        print(f"[!] Match found: {line.strip()}")
                        print(f"[!] Hash cracked after {num} tries.")
                        return 0

        except FileNotFoundError:
            print("ERROR: File not found.")
            return 1

        print("Wordlist exhausted. Couldn't crack the hash.")
        return 0