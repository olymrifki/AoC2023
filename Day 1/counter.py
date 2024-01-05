def get_number(line: str) -> int:
    numbers = [number for number in line if number in "0123456789"]
    # print(numbers)
    return int(numbers[0] + numbers[-1])


with open("./Day 1/example.txt") as file:
    # print(file.readline)
    print(sum(get_number(line) for line in file.readlines()))
