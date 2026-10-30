def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError('Неверное количество полей')

    city, temp_str, date = parts[0].strip(), parts[1].strip(), parts[2].strip()

    if not city or not date:
        raise ValueError('Пустое название города или дата')

    try:
        temp = float(temp_str)
    except ValueError:
        raise  ValueError('Некорректный формат температуры')

    return {'city': city, 'temp': temp, 'date': date}

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