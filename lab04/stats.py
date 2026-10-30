def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError('Неверное количество полей')

    city, temp_str, date = parts[0].strip(), parts[1].strip(), parts[2].strip()

    date = date.strip(')"\'')

    if not city or not date:
        raise ValueError('Пустое название города или дата')

    try:
        temp = float(temp_str.replace(',', '.'))
    except ValueError:
        raise  ValueError('Некорректный формат температуры')

    return {'city': city, 'temperature': temp, 'date': date}

def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            pass
    return valid_records

def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}
    for r in records:
        city = r['city']
        temp = r['temperature']
        totals[city] = totals.get(city, 0.0) + temp
        counts[city] = counts.get(city, 0) + 1

    averages = {}
    for city in totals:
        averages[city] = round(totals[city] / counts[city], 1)
    return averages

def warmest_city(records: list[dict]) -> str:
    if not records:
        return ""
    avgs = average_by_city(records)
    best_city = min(avgs.keys(), key=lambda x: (-avgs[x], x))
    return best_city