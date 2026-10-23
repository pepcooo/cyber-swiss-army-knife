import hashlib

class Hash:
    def __init__(self):
        self.__hashing_algorithms = hashlib.algorithms_available
        print("You have chosen the hash module.")
        self.run()

    def run(self):
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
