import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

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
    income = st.number_input("Enter your monthly income (₹)", min_value=0)
    expenses = st.number_input("Enter your monthly expenses (₹)", min_value=0)

    if income > 0:
        savings = income - expenses
        st.info(f"Your estimated monthly savings: ₹{savings}")

        if savings < income * 0.1:
            st.warning("Try saving at least 10% of your income.")
        else:
            st.success("Good job! You're saving a healthy amount 🎉")

# --- FINANCIAL DASHBOARD ---
elif page == "📈 Financial Dashboard":
    st.header("📈 Financial Overview Dashboard")

    # Sample monthly data
    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Income": [8000, 8500, 8700, 9000, 9500, 9800],
        "Expenses": [7000, 7300, 7600, 7800, 8200, 8500],
    }
    df = pd.DataFrame(data)
    df["Savings"] = df["Income"] - df["Expenses"]

    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.line(df, x="Month", y=["Income", "Expenses"], markers=True,
                       title="Monthly Income vs Expenses")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.bar(df, x="Month", y="Savings", color="Savings",
                      title="Monthly Savings", text_auto=True)
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("💡 Summary Table")
    st.dataframe(df.style.format({"Income": "₹{:.0f}", "Expenses": "₹{:.0f}", "Savings": "₹{:.0f}"}))

    avg_saving = df["Savings"].mean()
    st.success(f"Your average monthly savings: ₹{avg_saving:.0f}")

# --- AI INVESTMENT TIPS ---
elif page == "🧠 AI Investment Tips":
    st.header("🧠 AI-Powered Investment Suggestions")
    risk = st.radio("Select your risk tolerance:", ["Low", "Medium", "High"])
    goal = st.text_input("Your financial goal (e.g., 'Save for laptop', 'Start SIP')")

    if st.button("Generate Advice"):
        if risk == "Low":
            st.write(f"💡 For '{goal}', start with an FD or digital gold plan.")
        elif risk == "Medium":
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
