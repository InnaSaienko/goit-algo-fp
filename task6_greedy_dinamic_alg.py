from typing import Dict, List, Tuple

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items: Dict, budget: int) -> Tuple[List[str], int]:
    """Greedy calories per cost"""

    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True,
    )

    total_calories = 0
    chosen = []

    for name, data in sorted_items:
        if budget >= data["cost"]:
            budget -= data["cost"]
            total_calories += data["calories"]
            chosen.append(name)

    chosen.sort()
    return chosen, total_calories


def dynamic_programming(items: Dict, budget: int) -> Tuple[List[str], int]:
    """Dynamic programming solution"""

    items_names = list(items.keys())
    quantity_items = len(items_names)

    table = [[0] * (budget + 1) for _ in range(quantity_items + 1)] # create empty table

    for i in range(1, quantity_items + 1): # fill table with max calories
        cost = items[items_names[i - 1]]["cost"]
        calories = items[items_names[i - 1]]["calories"]

        for b in range(budget + 1):
            if cost <= b:
                table[i][b] = max(
                    table[i - 1][b],
                    table[i - 1][b - cost] + calories,
                )
            else:
                table[i][b] = table[i - 1][b]

    # restore chosen items
    result = []
    b = budget
    for i in range(quantity_items, 0, -1): # find in table which item give best max calories
        if table[i][b] != table[i - 1][b]:
            result.append(items_names[i - 1])
            b -= items[items_names[i - 1]]["cost"]

    result = sorted(result)
    return result, table[quantity_items][budget]


if __name__ == "__main__":
    budget = 137

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("Greedy:", greedy_result)
    print("Dynamic:", dp_result)
