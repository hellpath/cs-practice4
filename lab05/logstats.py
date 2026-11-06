def parse_event(line: str) -> dict:
    if not line or not line.strip():
        raise ValueError("Пустая строка")

    parts = line.split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError("Неверный формат строки")

    time, level, message = parts
    if level not in {"DEBUG", "INFO", "WARNING", "ERROR"}:
        raise ValueError("Неизвестный уровень")

    return {"time": time, "level": level, "message": message.strip()}