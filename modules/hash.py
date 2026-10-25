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
        print("Please enter the hash you wish to crack followed by the name of hashing algorithm and a path to the wordlist file.")
        user_input = input().strip()

        if not user_input:
            print("ERROR: Empty string.")
            return 1

        hash_to_crack = user_input.split(" ")[0]
        hashing_algorithm = user_input.split(" ")[1]
        wordlist_path = user_input.split(" ")[2]

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