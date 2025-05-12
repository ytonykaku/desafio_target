import json
from typing import List


class DailyRevenue:
    def __init__(self, day: int, amount: float):
        self.day = day
        self.amount = amount

    def __repr__(self):
        return f"Day {self.day}: ${self.amount:.2f}"


class MonthlyRevenue:
    def __init__(self, data: List[dict]):
        self.days = [DailyRevenue(d["dia"], d["valor"]) for d in data]
        self.valid_days = [d for d in self.days if d.amount > 0]

    def min_revenue(self) -> float:
        return min(d.amount for d in self.valid_days)

    def max_revenue(self) -> float:
        return max(d.amount for d in self.valid_days)

    def monthly_average(self) -> float:
        total = sum(d.amount for d in self.valid_days)
        return total / len(self.valid_days)

    def days_above_average(self) -> List[DailyRevenue]:
        avg = self.monthly_average()
        return [d for d in self.valid_days if d.amount > avg]

    def report(self):
        print(f"Lowest daily revenue: ${self.min_revenue():.2f}")
        print(f"Highest daily revenue: ${self.max_revenue():.2f}")
        print(f"Monthly average (excluding zeros): ${self.monthly_average():.2f}")
        print(f"Number of days above average: {len(self.days_above_average())}")
        for day in self.days_above_average():
            print(f"  - {day}")


def load_json_data(filepath: str) -> List[dict]:
    with open(filepath, 'r') as f:
        return json.load(f)


if __name__ == "__main__":
    data = load_json_data("dados.json")
    revenue = MonthlyRevenue(data)
    revenue.report()
