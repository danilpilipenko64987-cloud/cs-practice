import sys

from stats import average_by_city, read_valid, warmest_city


def main():
    lines = sys.stdin.read().splitlines()

    records = read_valid(lines)
    blank_lines = sum(1 for line in lines if not line.strip())
    invalid_count = len(lines) - len(records) - blank_lines

    averages = average_by_city(records)
    city = warmest_city(records)

    print(len(records))
    print(invalid_count)

    if city:
        print(f"{averages[city]:.1f}")
    else:
        print("0.0")


if __name__ == "__main__":
    main()