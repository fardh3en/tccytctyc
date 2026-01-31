import json
import os


def load_vendors(filepath):
    """
    Loads vendor data from a JSON file.

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        list: List of vendor dictionaries.
    """
    try:
        with open(filepath, "r") as f:
            vendors = json.load(f)
        return vendors
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {filepath}")
        return []


def calculate_score(vendor, budget, deadline):
    """
    Calculates the total score for a vendor based on price, delivery, and reliability.

    Score Formula:
    price_score = (budget - price_per_unit) / budget
    delivery_score = (deadline - delivery_days) / deadline
    total_score = price_score + delivery_score + reliability_score

    Args:
        vendor (dict): Vendor data.
        budget (float): User's budget per unit.
        deadline (int): User's delivery deadline in days.

    Returns:
        float: Total calculated score.
    """
    # Price Score: Higher is better (lower price relative to budget)
    # If price > budget, this will be negative, which is fine as it penalizes over-budget
    price_score = (budget - vendor["price_per_unit"]) / budget

    # Delivery Score: Higher is better (faster delivery relative to deadline)
    delivery_score = (deadline - vendor["delivery_days"]) / deadline

    # Reliability is already 0-1
    reliability_score = vendor["reliability_score"]

    total = price_score + delivery_score + reliability_score
    return round(total, 4)
