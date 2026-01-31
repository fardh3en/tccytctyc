class ConstraintAgent:
    def __init__(self, budget, deadline):
        self.budget = budget
        self.deadline = deadline

    def run(self, vendors):
        """
        Filters vendors that do not meet the budget or deadline constraints.
        """
        print("\n--- Constraint Agent Started ---")
        print(
            f"Filtering with Budget: ${self.budget} and Deadline: {self.deadline} days..."
        )

        valid_vendors = []
        for vendor in vendors:
            if (
                vendor["price_per_unit"] <= self.budget
                and vendor["delivery_days"] <= self.deadline
            ):
                valid_vendors.append(vendor)
            else:
                reasons = []
                if vendor["price_per_unit"] > self.budget:
                    reasons.append(
                        f"Price ${vendor['price_per_unit']} > Budget ${self.budget}"
                    )
                if vendor["delivery_days"] > self.deadline:
                    reasons.append(
                        f"Delivery {vendor['delivery_days']} days > Deadline {self.deadline}"
                    )
                print(f" - Dropped {vendor['name']}: {', '.join(reasons)}")

        print(f"Valid vendors remaining: {len(valid_vendors)}")
        return valid_vendors
