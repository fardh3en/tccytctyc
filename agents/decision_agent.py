class DecisionAgent:
    def run(self, ranked_vendors, negotiation_advice):
        """
        Makes the final selection and outputs the result.
        """
        print("\n--- Decision Agent Started ---")

        if not ranked_vendors:
            print("No valid vendors available. Decision: NONE.")
            return None

        top_vendor = ranked_vendors[0]

        print("\n==============================")
        print("       FINAL DECISION         ")
        print("==============================")
        print(f"Selected Vendor: {top_vendor['name']}")
        print(f"Final Score: {top_vendor['score']}")
        print(f"Price: ${top_vendor['price_per_unit']}")
        print(f"Delivery: {top_vendor['delivery_days']} days")
        print(f"Reliability: {top_vendor['reliability_score']}")
        print("\n>>> Negotiation Tip:")
        print(negotiation_advice)
        print("==============================")

        return top_vendor
