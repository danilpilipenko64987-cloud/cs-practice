import unittest

from stats import (
    parse_record,
    read_valid,
    average_by_city,
    warmest_city,
)


class TestStats(unittest.TestCase):
    def test_parse_record(self):
        record = parse_record("Азов;24.5;2026-07-01")
        self.assertEqual(record["city"], "Азов")
        self.assertEqual(record["temperature"], 24.5)
        self.assertEqual(record["date"], "2026-07-01")

    def test_parse_record_with_spaces_and_comma(self):
        record = parse_record(" Азов ; -3,5 ; 2026-01-09")
        self.assertEqual(record["temperature"], -3.5)

    def test_parse_invalid_record(self):
        with self.assertRaises(ValueError):
            parse_record("неправильная запись")

    def test_read_valid_skips_bad_and_blank_lines(self):
        records = read_valid([
            "",
            "Азов;24.5;2026-07-01",
            "ошибка",
            "Таганрог;30;2026-07-01",
        ])
        self.assertEqual(len(records), 2)

    def test_average_by_city(self):
        records = [
            {"city": "Азов", "temperature": 24.5},
            {"city": "Азов", "temperature": 25.5},
            {"city": "Таганрог", "temperature": 30.0},
        ]
        self.assertEqual(
            average_by_city(records),
            {"Азов": 25.0, "Таганрог": 30.0},
        )

    def test_warmest_city_tie(self):
        records = [
            {"city": "Таганрог", "temperature": 30.0},
            {"city": "Азов", "temperature": 30.0},
        ]
        self.assertEqual(warmest_city(records), "Азов")


if __name__ == "__main__":
    unittest.main()