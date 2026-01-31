import streamlit as st
import os
import sys
from dotenv import load_dotenv

# Ensure we can import modules from the current directory
sys.path.append(os.path.dirname(__file__))

from agents.fetcher_agent import FetcherAgent
from agents.constraint_agent import ConstraintAgent
from agents.comparer_agent import ComparerAgent
from agents.negotiator_agent import NegotiatorAgent
from agents.decision_agent import DecisionAgent

# Load environment variables
load_dotenv()

# Streamlit Cloud Deployment: Load secrets if .env is missing
if hasattr(st, "secrets") and "OPENAI_API_KEY" in st.secrets:
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Procurement AI", layout="wide")

st.title("🤖 Procurement AI Multi-Agent System")
st.markdown("Automated vendor selection and negotiation assistant.")

# --- Sidebar Inputs ---
st.sidebar.header("Procurement Constraints")
budget = st.sidebar.number_input(
    "Max Budget per Unit (₹)", min_value=0.0, value=100.0, step=5.0
)
deadline = st.sidebar.number_input(
    "Delivery Deadline (Days)", min_value=0, value=10, step=1
)

if st.sidebar.button("Run Procurement Process", type="primary"):
    data_path = os.path.join(
        os.path.dirname(__file__), "data_simulator", "vendors.json"
    )

    # --- Step 1: Fetch Vendors ---
    st.header("1. Vendor Data Fetching")
    fetcher = FetcherAgent(data_path)
    vendors = fetcher.run()

    if vendors:
        st.write(f"Loaded {len(vendors)} vendors from database.")
        st.table(vendors)  # Display raw data
    else:
        st.error("No vendors found.")
        st.stop()

    # --- Step 2: Apply Constraints ---
    st.header("2. Constraint Filtering")
    constraint = ConstraintAgent(budget, deadline)
    valid_vendors = constraint.run(vendors)

    if valid_vendors:
        st.success(
            f"✅ {len(valid_vendors)} vendors meet the criteria (Budget <= ₹{budget}, Deadline <= {deadline} days)."
        )
        st.table(valid_vendors)
    else:
        st.error(
            f"❌ No vendors meet constraints: Budget ₹{budget}, Deadline {deadline} days."
        )
        st.stop()

    # --- Step 3: Score & Rank ---
    st.header("3. AI Scoring & Ranking")
    comparer = ComparerAgent(budget, deadline)
    ranked_vendors = comparer.run(valid_vendors)

    # Display ranked vendors with highlighting
    st.write("Vendors ranked by composite score (Price + Delivery + Reliability):")
    st.dataframe(ranked_vendors, use_container_width=True)

    top_vendor = ranked_vendors[0]

    # --- Step 4: AI Negotiation ---
    st.header("4. AI Negotiation Strategy")
    with st.spinner("Consulting Negotiator Agent (LLM)..."):
        negotiator = NegotiatorAgent()
        negotiation_advice = negotiator.run(top_vendor)

    st.info(f"💡 **Negotiation Tip for {top_vendor['name']}:**\n\n{negotiation_advice}")

    # --- Step 5: Final Decision ---
    st.header("5. Final Decision")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.metric(label="🏆 Winning Suplier", value=top_vendor["name"])
        st.metric(label="Final Score", value=f"{top_vendor['score']:.4f}")

    with col2:
        st.subheader("Deal Details")
        st.write(f"**Price:** ₹{top_vendor['price_per_unit']}")
        st.write(f"**Delivery:** {top_vendor['delivery_days']} days")
        st.write(f"**Reliability:** {top_vendor['reliability_score'] * 100}%")

    decision_agent = DecisionAgent()
    # We call run just to trigger any internal logic if added later, though we presented the data above.
    decision_agent.run(ranked_vendors, negotiation_advice)
