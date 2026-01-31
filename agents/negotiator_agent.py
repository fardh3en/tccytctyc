import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


class NegotiatorAgent:
    def __init__(self):
        # Initialize OpenAI Chat Model
        # Using a temperature of 0.7 for some creativity in negotiation tactics
        # Note: Requires OPENAI_API_KEY in environment variables
        try:
            self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        except Exception as e:
            print("Warning: Could not initialize LLM. Negotiation will be skipped.")
            self.llm = None

    def run(self, top_vendor):
        """
        Generates a negotiation strategy for the top vendor.
        """
        print("\n--- Negotiator Agent Started ---")

        if not top_vendor:
            print("No vendor to negotiate with.")
            return "No negotiation needed."

        if not self.llm:
            return "LLM not available. Skipping negotiation suggestion."

        print(f"Drafting negotiation strategy for {top_vendor['name']}...")

        # Prepare the prompt
        system_prompt = "You are a procurement negotiator. Suggest possible improvements to this supplier offer."
        user_prompt = (
            f"Supplier: {top_vendor['name']}\n"
            f"Offer: ${top_vendor['price_per_unit']} per unit, delivered in {top_vendor['delivery_days']} days.\n"
            f"Reliability: {top_vendor['reliability_score']}\n"
            "What can we ask for to improve this deal?"
        )

        try:
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=user_prompt),
            ]
            response = self.llm(messages)
            suggestion = response.content
            print("Negotiation suggestion generated.")
            return suggestion
        except Exception as e:
            print(f"Error during LLM call: {e}")
            return "Error generating negotiation advice."
