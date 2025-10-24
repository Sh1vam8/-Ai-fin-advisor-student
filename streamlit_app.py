from ast import Load
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Financial Advisor", page_icon="💰", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("💸 Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home",
        "📊 Financial Planner",
        "📈 Financial Dashboard",
        "🧠 AI Investment Tips",
        "ℹ️ About Project",
    ],
)

# --- HOME PAGE ---
if page == "🏠 Home":
    st.title("AI Financial Advisor for Students 💰")
    st.subheader("Smart Money Guidance for Students with Zero Capital")
    st.markdown("""
    This AI-powered financial advisor helps students:
    - Understand their spending habits 💵  
    - Plan small savings and investments 📈  
    - Learn financial literacy concepts 💡  
    - Receive AI insights on future goals 🎯
    """)
    st.image("https://cdn-icons-png.flaticon.com/512/4221/4221445.png", width=200)
    st.success("Let's begin your journey toward smarter financial decisions!")

# --- FINANCIAL PLANNER ---
elif page == "📊 Financial Planner":
    st.header("📊 Student Budget & Savings Planner")

    # --- User Profile ---
    with st.expander("👤 Your Profile"):
        name = st.text_input("Name (optional)")
        age = st.number_input("Age", min_value=10, max_value=100, value=20)
        target_savings = st.number_input("Target savings per month (₹)", min_value=0, value=500)

    # --- Income & Expenses ---
    income = st.number_input("Enter your monthly income (₹)", min_value=0, key="income_input")

    st.markdown("### 💰 Enter your fixed monthly expenses")
    rent = st.number_input("Rent (₹)", min_value=0, value=0)
    food = st.number_input("Food (₹)", min_value=0, value=0)
    transport = st.number_input("Transport (₹)", min_value=0, value=0)
    loan = st.number_input("Loan (₹)", min_value=0, value=0)
    misc = st.number_input("Miscellaneous (₹)", min_value=0, value=0)

    total_expenses = rent + food + transport + loan + misc
    st.info(f"💸 **Your total expenses:** ₹{total_expenses:,.0f}")

    # --- Initialize session_state DataFrame ---
    if 'planner_data' not in st.session_state:
        st.session_state.planner_data = pd.DataFrame(columns=[
            'Month', 'Income', 'Expenses', 'Savings', 'Rent', 'Food', 'Transport','Loan','Misc'
        ])

    # --- Save monthly entry ---
    if st.button("Save Month Data"):
        savings = income - total_expenses
        month_count = len(st.session_state.planner_data) + 1
        new_entry = pd.DataFrame({
            'Month':[f"Month {month_count}"],
            'Income':[income],
            'Expenses':[total_expenses],
            'Savings':[savings],
            'Rent':[rent],
            'Food':[food],
            'Transport':[transport],
            'Loan':[loan],
            'Misc':[misc]
        })
        st.session_state.planner_data = pd.concat([st.session_state.planner_data, new_entry], ignore_index=True)
        st.success(f"Data saved! Your savings for this month: ₹{savings}")

        # Optional: save to CSV for persistence
        st.session_state.planner_data.to_csv("planner_data.csv", index=False)

    # --- Show current planner data ---
    if not st.session_state.planner_data.empty:
        st.subheader("📋 Current Planner Data")
        st.dataframe(st.session_state.planner_data.style.format(
            {"Income":"₹{:.0f}", "Expenses":"₹{:.0f}", "Savings":"₹{:.0f}", 
             "Rent":"₹{:.0f}", "Food":"₹{:.0f}", "Transport":"₹{:.0f}","Loan":"₹{:.0f}" ,"Misc":"₹{:.0f}"}
        ))

        # --- 6-month projection ---
        st.subheader("📈 6-Month Savings Projection")
        last_savings = st.session_state.planner_data['Savings'].iloc[-1]
        projection = pd.DataFrame({
            "Month":[f"Month {i+1}" for i in range(6)],
            "Projected Savings":[last_savings*i for i in range(1,7)]
        })
        st.table(projection.style.format({"Projected Savings":"₹{:.0f}"}))

# --- FINANCIAL DASHBOARD ---
elif page == "📈 Financial Dashboard":
    st.header("📈 Financial Overview Dashboard")

    # --- Load dynamic data ---
    if 'planner_data' in st.session_state and not st.session_state.planner_data.empty:
        df = st.session_state.planner_data.copy()
    elif os.path.exists("planner_data.csv"):
        df = pd.read_csv("planner_data.csv")
    else:
        st.warning("No planner data available. Please enter your monthly income & expenses first.")
        st.stop()

    df['Month'] = df['Month'].astype(str)

    # --- Charts ---
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.line(df, x="Month", y=["Income","Expenses"], markers=True,
                       title="Monthly Income vs Expenses")
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        fig2 = px.bar(df, x="Month", y="Savings", color="Savings",
                      title="Monthly Savings", text_auto=True)
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("💡 Summary Table")
    st.dataframe(df.style.format({"Income":"₹{:.0f}", "Expenses":"₹{:.0f}", "Savings":"₹{:.0f}"}))
    st.success(f"Your average monthly savings: ₹{df['Savings'].mean():.0f}")

# --- AI INVESTMENT TIPS ---
elif page == "🧠 AI Investment Tips":
    st.header("🧠 AI-Powered Investment Suggestions")
    risk = st.radio("Select your risk tolerance:", ["Low","Medium","High"])
    goal = st.text_input("Your financial goal (e.g., 'Save for laptop', 'Start SIP')")

    if st.button("Generate Advice"):
        if risk=="Low":
            st.write(f"💡 For '{goal}', start with an FD or digital gold plan.")
        elif risk=="Medium":
            st.write(f"💡 For '{goal}', consider mutual funds or SIPs.")
        else:
            st.write(f"💡 For '{goal}', explore crypto or small-cap mutual funds — high risk, high reward!")

# --- ABOUT PAGE ---
elif page == "ℹ️ About Project":
    st.header("ℹ️ About This Mini Project")
    st.markdown("""
    **Project Name:** AI Financial Advisor for Students  
    **Technology Used:** Python, Streamlit, Pandas, Plotly, Scikit-learn  
    **Goal:** Build financial awareness and micro-investment strategies for students.

    Developed as part of *Mini Project – EDGE* to showcase AI-driven decision-making for personal finance.
    """)
