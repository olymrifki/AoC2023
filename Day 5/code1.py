# ```
# Given:
#     1. list of type of initial source category
#         "seeds: 79 14 55 13"
#     2. many list of convertion from source to destination
#         "seed-to-soil map:
#         50 98 2
#         52 50 48

#         soil-to-fertilizer map:
#         0 15 37
#         37 52 2
#         39 0 15"

#         Conversion:
#         This list consists of *destination start*, *source start*, and *map range*
#         If source number is in range, the converted destination number is a 1 to 1 map inside of the range
#         otherwise, the sourec number is the same as destination number

# Find the smallest value of the final destination number
# ```

# ```
# To do:
# 1. Convert initial source line to number
line = "seeds: 79 14 55 13\n"


def get_source_number(line: str) -> list[int]:
    line = line.strip()
    line = line.split(" ")[1:]
    return [int(number) for number in line]


assert get_source_number(line) == [79, 14, 55, 13]

# 2. Convert map line to number
#     2.1 Convert multiple map line to list of map
#         detect starting non number line and blank stopping line
#     2.2 For each map:
#         Conversion will be
#         destination = (source-source_start) > map_range? source
#                     : destination_start + (source-source_start)
#         for all maps
converters = []


class Converter:
    def __init__(self) -> None:
        self.maps = []
        self.name = ""
        # consists of list of:
        # *destination start*, *source start*, and *map range*

    def convert(self, source_number: list[int]) -> list[int]:
        result = source_number.copy()
        for map in self.maps:
            for source_index, source in enumerate(source_number):
                if source is not None and (0 <= (source - map[1]) < map[2]):
                    result[source_index] = map[0] + (source - map[1])
                    source_number[source_index] = None
        return result

    def add_map_from_line(self, line: str) -> None:
        line = line.strip()
        line = line.split(" ")
        self.maps.append([int(number) for number in line])


converter = Converter()
converter.add_map_from_line("52 50 48 \n")
assert converter.maps == [[52, 50, 48]]
converter = None


def is_contain_number(line: str) -> bool:
    for char in line:
        if char in "0123456789":
            return True
    return False


with open("./Day 5/data.txt") as file:
    lines = file.readlines()
    first_line = lines[0]
    source = get_source_number(first_line)

    for line in lines[1:]:
        line = line.strip()
        if not line:
            if converter is not None:
                converters.append(converter)
            converter = Converter()
        elif is_contain_number(line):
            converter.add_map_from_line(line)
        else:
            converter.name = line
            print("Adding " + line)
            print(converters)
    converters.append(converter)

# 3. Connvert and find smallest destination
print("\n\nconverting")
for converter in converters:
    print("converting")
    print(source)
    print("with " + converter.name)
    source = converter.convert(source)
print(source)
print(min(source))

# ```
