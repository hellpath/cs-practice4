import sys
from stats import average_by_city, parse_record, warmest_city

def main():
    lines = sys.stdin.read().splitlines()

    valid_records = []
    error_count = 0

    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            error_count += 1

    avgs = average_by_city(valid_records)
    warmest = warmest_city(valid_records)

    print(len(valid_records))
    print(error_count)
    if warmest in avgs:
        print(f'{avgs[warmest]:.1f}')
    else:
        print(0.0)

if __name__ == '__main__':
    main()