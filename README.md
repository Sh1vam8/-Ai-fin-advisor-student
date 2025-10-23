# AI Financial Advisor for Students**

## **1. Project Title**

**AI Financial Advisor for Students with Zero Capital** 💰

A web app that helps students plan budgets, track expenses, forecast savings, and get personalized micro-financial advice using AI and rule-based engines.

---

## **2. Project Overview**

Many students struggle with managing money due to irregular income, limited capital, and lack of financial literacy.
This project provides a **simple, interactive, and educational tool** to:

* Track monthly income and expenses
* Plan and forecast savings
* Suggest actionable micro-challenges
* Provide AI-powered low-risk investment guidance
* Generate dashboards and projections for better visualization

---

## **3. Core Objectives**

* Teach students to **start small with savings and investments**
* Provide **personalized action plans and habit tracking**
* Create **visual dashboards for income, expenses, and savings**
* Build a **portfolio project** to showcase skills in Python, data analysis, and Streamlit

---

## **4. Features**

### ✅ Home Page

* Introduction to the AI Financial Advisor
* Overview of app functionality

### ✅ Financial Planner

* Input income and fixed expenses (Rent, Food, Transport, Misc)
* Target savings and profile info (age, name)
* Save monthly data in session or CSV

### ✅ Financial Dashboard

* Interactive charts: Income vs Expenses, Monthly Savings
* Summary table with averages
* 6-month savings projections

### ✅ AI Investment Tips

* Risk-based personalized suggestions
* Educational guidance for low-barrier investments

### ✅ About Project

* Tech stack and project purpose

---

## **5. Tech Stack**

* **Frontend / UI:** Streamlit
* **Backend / Analytics:** Python, Pandas, NumPy
* **Visualization:** Plotly
* **Storage:** Session State + CSV (local), optional SQLite
* **Optional ML:** Rule-based engine for suggestion ranking
* **Deployment:** Streamlit Cloud

---

## **6. Installation & Setup**

1. Clone the repository:

```bash
git clone https://github.com/your-username/ai-fin-advisor-student.git
cd ai-fin-advisor-student
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app locally:

```bash
streamlit run streamlit_app.py
```

4. Open the link in your browser (Streamlit provides the local URL).

---

## **7. Folder Structure**

```
/ai-fin-advisor
  /app
    streamlit_app.py       # Main Streamlit app
    /modules               # Optional for modular code (profile, budget, savings)
      profile.py
      budget.py
      savings_engine.py
      forecast.py
  /data
    planner_data.csv       # Saved planner entries
  /docs
    README.md
    architecture.md        # Optional architecture diagram
  /notebooks
    eda.ipynb              # Exploratory data analysis (if any)
  requirements.txt
  .github/workflows/deploy.yml  # Optional CI/CD
```

---

## **8. How to Use**

1. Go to **Financial Planner** page → enter profile, income, and expenses → save monthly data.
2. Go to **Financial Dashboard** → visualize income, expenses, savings, and 6-month projection.
3. Go to **AI Investment Tips** → select risk and get personalized suggestions.

---

## **9. Future Enhancements**

* Micro-savings engine with daily/weekly micro-challenges
* Integration with SQLite or Firebase for persistent storage
* Personalized ML recommendations based on student spending habits
* PDF/Exportable reports
* Gamification (badges, streaks, progress tracking)

---

## **10. Disclaimer**

⚠️ **Educational purposes only** – This app does **not provide financial advice**. Users are responsible for their financial decisions.

---

If you want, I can also **create a polished `architecture.md`** for the `/docs` folder showing **app flow, module structure, and data flow**, which will make your repo look highly professional for portfolio or MiM/MBA applications.

Do you want me to do that next?

