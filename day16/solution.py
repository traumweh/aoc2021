#!/usr/bin/env python3
import os, sys

def init() -> list:
    os.chdir(os.path.dirname(sys.argv[0])) # change working dir

    with open("input", "r") as f:
        raw = f.readline()
        binary = bin(int(raw, 16))[2:]
        return binary.zfill(len(raw) * 4)

def tasks(data: str) -> tuple:
    packets = parse(data)

    task1 = version_sum([packets])
    task2 = calc_value(packets)

    return (task1,task2)

def parse(bitstr: str) -> list:
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
                packet = parse(bitstr[pos:])
                content.append(packet)
                pos += packet[3]
        else: # fixed number of subpackages
            total_count = int(bitstr[7:18], 2)
            content = [] # going to be subpackages
            pos += 12

            while len(content) < total_count:
                packet = parse(bitstr[pos:])
                content.append(packet)
                pos += packet[3]

    return (version, type_nr, content, pos)

def version_sum(packets: list) -> int:
    vsum = 0

    for packet in packets:
        vsum += packet[0]

        if packet[1] != 4:
            vsum += version_sum(packet[2])

    return vsum

def calc_value(packet: list) -> int:
    if packet[1] == 4:
        return packet[2]
    else:
        values = [calc_value(subpacket) for subpacket in packet[2]]

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

print("1.) {}\t2.) {}".format(*tasks(init())))