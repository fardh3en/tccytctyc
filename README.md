# Procurement AI Multi-Agent System

A beginner-friendly multi-agent AI system that simulates procurement decision-making. The system selects the best supplier based on price, delivery time, reliability, budget, and deadline constraints.

## Project Structure
- `agents/`: Contains the logic for each agent.
    - `fetcher_agent.py`: Loads vendor data.
    - `constraint_agent.py`: Filters vendors based on rigid constraints.
    - `comparer_agent.py`: Scores and ranks vendors.
    - `negotiator_agent.py`: Uses an LLM to suggest negotiation strategies.
    - `decision_agent.py`: Makes the final selection.
- `data_simulator/`: Contains sample data (`vendors.json`).
- `main.py`: The entry point script that orchestrates the agents.
- `utils.py`: Utility functions.

## Setup

1.  **Install Python:** Ensure you have Python installed.
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Environment Variables:**
    - Rename the `.env` file (if you have one) or create one.
    - Add your OpenAI API key:
      ```
      OPENAI_API_KEY=your_api_key_here
      ```
    - *Note: If you don't have an API key, the Negotiator Agent will gracefully skip the LLM part.*


## How to Run

### Command Line Interface
1.  Navigate to the `procurement-ai` directory.
2.  Run the main script:
    ```bash
    python main.py
    ```
3.  Follow the prompts to enter your budget and deadline.

### Run Streamlit UI
To launch the visual dashboard:
```bash
cd procurement-ai
py -m streamlit run ui.py
```

### Streamlit UI Dashboard
1.  Ensure dependencies are installed.
2.  Navigate to the project folder:
    ```bash
    cd procurement-ai
    ```
3.  Run the UI:
    ```bash
    py -m streamlit run ui.py
    ```
4.  The dashboard will open in your browser.


## Example Output

```
Enter maximum budget per unit ($): 95
Enter delivery deadline (days): 7

--- Fetcher Agent Started ---
...
--- Constraint Agent Started ---
...
--- Comparer Agent Started ---
...
--- Negotiator Agent Started ---
...
--- Decision Agent Started ---
Selected Vendor: Alpha Supplies
...
```

## 🚀 Deployment

You can deploy this app to **Streamlit Community Cloud** directly from GitHub.

1.  Push this project to a GitHub repository.
2.  Go to [Streamlit Cloud](https://streamlit.io/cloud).
3.  Connect your GitHub account and select your repository.
4.  Set the **Main file path** to `procurement-ai/ui.py`.
    > **IMPORTANT:** If your repository has the folder `procurement-ai` at the root, you **MUST** set the path to `procurement-ai/ui.py`. If you leave it as just `ui.py`, it will fail.
5.  **Secrets Configuration**:
    - Go to App Settings -> Secrets.
    - Add your API key:
      ```toml
      OPENAI_API_KEY = "sk-..."
      ```

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/cloud)
