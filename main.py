import os
import sys

# Add the current directory to sys.path to ensure modules can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv

from agents.fetcher_agent import FetcherAgent
from agents.constraint_agent import ConstraintAgent
from agents.comparer_agent import ComparerAgent
from agents.negotiator_agent import NegotiatorAgent
from agents.decision_agent import DecisionAgent


def main():
    # Load environment variables (API Key)
    load_dotenv()

    print("==========================================")
    print("   PROCUREMENT AI MULTI-AGENT SYSTEM      ")
    print("==========================================")

    # 1. Get User Input
    try:
        budget = float(input("\nEnter maximum budget per unit ($): "))
        deadline = int(input("Enter delivery deadline (days): "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    # 2. Run Agents

    # Step 1: Fetcher Agent
    data_path = os.path.join(
        os.path.dirname(__file__), "data_simulator", "vendors.json"
    )
    fetcher = FetcherAgent(data_path)
    vendors = fetcher.run()

    # Step 2: Constraint Agent
    constraint = ConstraintAgent(budget, deadline)
    valid_vendors = constraint.run(vendors)

    if not valid_vendors:
        print("\nNo vendors met the criteria. Process terminated.")
        return

    # Step 3: Comparer Agent
    comparer = ComparerAgent(budget, deadline)
    ranked_vendors = comparer.run(valid_vendors)

    # Step 4: Negotiator Agent
    # We only negotiate with the top vendor
    top_vendor = ranked_vendors[0] if ranked_vendors else None
    negotiator = NegotiatorAgent()
    negotiation_advice = negotiator.run(top_vendor)

    # Step 5: Decision Agent
    decision_agent = DecisionAgent()
    final_choice = decision_agent.run(ranked_vendors, negotiation_advice)

    print("\nProcurement process completed.")


if __name__ == "__main__":
    main()
