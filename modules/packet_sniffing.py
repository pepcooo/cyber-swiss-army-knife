from scapy.all import sniff


class SniffingService:
    def __init__(self):
        self.__packet_count = 0


    def sniff_packets(self):
        try:
            sniff(prn=lambda packet: print(packet.summary()), count=self.__packet_count, store=False)

        except KeyboardInterrupt:
            return

    def set_count(self, count):
        if not count.isdigit():
            raise ValueError("Specified count is not a number.")

        self.__packet_count = int(count)


    def get_count(self):
        return self.__packet_count if self.__packet_count else "NO LIMIT"


class SniffingCLI:
    def __init__(self, service : SniffingService):
        self.__service = service


    def run(self):
        print("You have chosen the packet sniffing module.")
        while True:
            print("Please choose one of the following options:")
            print("\t1 - sniff packets")
            print(f"\t2 - set the amount of packets to sniff (currently: {self.__service.get_count()})")
            print("\t3 - quit")

            option = input().strip()

            if option not in ("1", "2", "3"):
                print("ERROR: Please choose a viable option.")
                return

            try:
                if option == "1":
                    print("Beginning packet sniffing. To stop, enter CTRL+C. ")
                    self.__service.sniff_packets()

                elif option == "2":
                    count = input("Please enter the number of packets to sniff (0 for no limit).\n").strip()
                    self.__service.set_count(count)

                else:
                    break

            except Exception as e:
                print(f"ERROR: {e}")