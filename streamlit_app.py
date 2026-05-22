import streamlit as st
import pandas as pd

# Set page configuration for a professional wide layout
st.set_page_config(page_title="Financial Report Engine", layout="wide")

st.title("📊 Financial Performance & Position Report Generator")
st.subheader("Professional Chartered Accountant Offline Suite")

# Step 1: Local File Input
uploaded_file = st.file_uploader("Upload Raw Financial CSV or Excel File", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read the data safely offline
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
        
    st.success("File successfully loaded into memory!")

    # --- SIMPLIFIED ACCOUNTING ENGINE ENGINE (Example Variables) ---
    # In production, pull these directly by filtering your dataframe rows:
    # q1_actual = df.loc[df['Line Item'] == 'Investment Income', 'Q1_Actual'].values[0]
    
    q1_rev, q2_rev, q2_budget = 1003365.00, 851804.43, 1453555.30
    q1_cash, q2_cash = 419796.00, 2441258.61
    q2_pat = -83159.61
    
    # Step 2: Create UI Tabs
    tab1, tab2, tab3 = st.tabs(["📋 Executive Management Report", "💸 Cashflow Statement", "🗃️ Raw Data Viewer"])
    
    with tab1:
        st.header("Management Financial Performance & Position Report")
        
        # Display Core KPI Blocks
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Q2 Revenue", value=f"GH¢ {q2_rev:,.2f}", delta=f"{(q2_rev-q1_rev)/q1_rev*100:.1f}% QoQ")
        col2.metric(label="Q2 Net Profit/Loss", value=f"GH¢ {q2_pat:,.2f}", delta="Unfavorable vs Q1")
        col3.metric(label="Cash Runway (Q2)", value=f"GH¢ {q2_cash:,.2f}", delta="Strategic Security")
        
        # Inject the text analysis dynamically
        st.markdown(f"""
        ### **1. Executive Summary**
        This report evaluates performance for **Q2 2025**. Total Revenue arrived at **GH¢ {q2_rev:,.2f}**, 
        representing a contraction against Q1 but handled through extreme cost containment techniques.
        
        ### **2. Technical Audit Notes**
        * **Income Surplus Mismatch:** The balance sheet reveals an un-reconciled variance matching Q1 PAT. Ensure correction journals are passed.
        """)
        
    with tab2:
        st.header("Statement of Cash Flows (IAS 7 Indirect Method)")
        # Draw a dynamic cashflow table
        cf_data = {
            "Line Item / Description": ["Net Profit/Loss After Tax", "Depreciation Add-back", "Operating Cash Flow", "Investing Activities (Net)", "Closing Cash Balance"],
            "Amount (GH¢)": [q2_pat, 225397.13, 151412.55, 1839291.36, q2_cash]
        }
        st.table(pd.DataFrame(cf_data))
        
    with tab3:
        st.header("Raw Imported Ledger Sheet")
        st.dataframe(df) # Allows sorting and local filtering

else:
    st.info("Please select and upload a local financial document to populate the reporting dashboard.")