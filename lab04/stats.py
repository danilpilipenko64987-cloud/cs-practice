def parse_record(line: str) -> dict:
    """Разбирает строку формата город;температура;дата."""
    parts = line.strip().split(";")

    if len(parts) != 3:
        raise ValueError("Запись должна содержать три поля")

    city = parts[0].strip()
    temperature_text = parts[1].strip().replace(",", ".")
    date = parts[2].strip()

    if not city or not date:
        raise ValueError("Город и дата не должны быть пустыми")

    try:
        temperature = float(temperature_text)
    except ValueError:
        raise ValueError("Температура должна быть числом")

    return {
        "city": city,
        "temperature": temperature,
        "date": date,
    }


def read_valid(lines: list[str]) -> list[dict]:
    """Возвращает корректные записи, пропуская пустые и ошибочные строки."""
    records = []

    for line in lines:
        if not line.strip():
            continue

        try:
            records.append(parse_record(line))
        except ValueError:
            continue

    return records


def average_by_city(records: list[dict]) -> dict:
    """Вычисляет среднюю температуру для каждого города."""
    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        temperature = record["temperature"]

        totals[city] = totals.get(city, 0) + temperature
        counts[city] = counts.get(city, 0) + 1

    return {
        city: round(totals[city] / counts[city], 1)
        for city in totals
    }


def warmest_city(records: list[dict]) -> str:
    """Возвращает город с самой высокой средней температурой."""
    averages = average_by_city(records)

    if not averages:
        return ""

    return sorted(averages, key=lambda city: (-averages[city], city))[0]