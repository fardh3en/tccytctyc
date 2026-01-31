from utils import load_vendors


class FetcherAgent:
    def __init__(self, data_path):
        self.data_path = data_path

    def run(self):
        """
        Loads vendor data from the JSON file.
        """
        print("\n--- Fetcher Agent Started ---")
        print(f"Loading vendors from {self.data_path}...")
        vendors = load_vendors(self.data_path)
        print(f"Successfully loaded {len(vendors)} vendors.")
        for v in vendors:
            print(
                f" - Found: {v['name']} (${v['price_per_unit']}/unit, {v['delivery_days']} days)"
            )
        return vendors
