#!/usr/bin/env python3

class Tasks:
    def __init__(self, filepath):
        with open(filepath, "r") as f:
            raw = f.readline()

        binary = bin(int(raw, 16))[2:]
        self.data = binary.zfill(len(raw) * 4)
        self.__tasks()

    def __tasks(self) -> int:
        packets = self.__parse(self.data)
        self.task1 = self.__version_sum([packets])
        self.task2 = self.__calc_value(packets)

    def __parse(self, bitstr: str) -> list:
        version = int(bitstr[:3], 2) # version bits
        type_nr = int(bitstr[3:6], 2) # type bits
        pos = 6 # at 7th bit now

        if type_nr == 4:
            content = "" # going to be a binary number

            while True:
                first = bitstr[pos]
                content += bitstr[pos+1:pos+5] # ignore first bit of group
                pos += 5 # adjust position

                if first == "0": break

            content = int(content, 2)
        else:
            if bitstr[6] == "0": # fixed number of bits
                total_length = int(bitstr[7:22], 2)
                content = [] # going to be subpackages
                pos += 16

                while sum(packet[3] for packet in content) < total_length:
                    packet = self.__parse(bitstr[pos:])
                    content.append(packet)
                    pos += packet[3]
            else: # fixed number of subpackages
                total_count = int(bitstr[7:18], 2)
                content = [] # going to be subpackages
                pos += 12

                while len(content) < total_count:
                    packet = self.__parse(bitstr[pos:])
                    content.append(packet)
                    pos += packet[3]

        return (version, type_nr, content, pos)

    def __version_sum(self, packets: list) -> int:
        vsum = 0

        for packet in packets:
            vsum += packet[0]

            if packet[1] != 4:
                vsum += self.__version_sum(packet[2])

        return vsum

    def __calc_value(self, packet: list) -> int:
        if packet[1] == 4:
            return packet[2]
        else:
            values = [self.__calc_value(subpacket) for subpacket in packet[2]]

            if packet[1] == 0: return sum(values)
            elif packet[1] == 1:
                result = 1

                for value in values:
                    result *= value
            
                return result
            elif packet[1] == 2: return min(values)
            elif packet[1] == 3: return max(values)
            elif packet[1] == 5: return int(values[0] > values[1])
            elif packet[1] == 6: return int(values[0] < values[1])
            elif packet[1] == 7: return int(values[0] == values[1])

    def __repr__(self) -> str:
        return f"1.) {self.task1:<16}\t2.) {self.task2:<16}"


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2: print(Tasks(argv[1]))
    else: print(Tasks("input"))