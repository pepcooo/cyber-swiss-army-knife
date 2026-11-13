from datetime import datetime
from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP, ARP, Raw, Padding
from scapy.config import conf


class SniffingService:
    def __init__(self):
        self.__packet_count = 0


    def _format_packet(self, packet, file):
        layers = [layer.__name__ for layer in packet.layers() if layer not in (Raw, Padding)]
        proto_name = layers[-1].upper() if layers else "OTHER"

        protocol = f"[{proto_name}] "
        f_packet = protocol + packet.summary()

        print(f_packet)
        print(f_packet, flush=True, file=file)


    def sniff_packets(self):
        conf.noenum.add(TCP.sport, TCP.dport, UDP.sport, UDP.dport)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"report_{timestamp}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                sniff(prn=lambda packet: self._format_packet(packet, f),
                    count=self.__packet_count,
                    store=False)


        except KeyboardInterrupt:
            pass

        print(f"\nFile saved as {filename}\n")

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
                continue

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