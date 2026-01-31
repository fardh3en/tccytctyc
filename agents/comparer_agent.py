from utils import calculate_score


class ComparerAgent:
    def __init__(self, budget, deadline):
        self.budget = budget
        self.deadline = deadline

    def run(self, vendors):
        """
        Scores each vendor and ranks them.
        """
        print("\n--- Comparer Agent Started ---")
        scored_vendors = []

        for vendor in vendors:
            score = calculate_score(vendor, self.budget, self.deadline)
            vendor_with_score = vendor.copy()
            vendor_with_score["score"] = score
            scored_vendors.append(vendor_with_score)
            print(f" - Scored {vendor['name']}: {score}")

        # Sort by score in descending order
        ranked_vendors = sorted(scored_vendors, key=lambda x: x["score"], reverse=True)

        print(
            "Ranking complete. Top candidate: "
            + (ranked_vendors[0]["name"] if ranked_vendors else "None")
        )
        return ranked_vendors
