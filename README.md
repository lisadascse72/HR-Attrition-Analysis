# HR Attrition Analysis Dashboard

This project analyzes employee attrition patterns using IBM's HR Analytics dataset.  
It includes a Power BI dashboard for business users and a Python script for basic data analysis.

---

## 📊 Dashboard Highlights
- Attrition rate and count KPIs
- Breakdown by Department, Age Group, and Job Role
- Tenure vs. Attrition trend (Years at Company vs. Attrition)
- Clean, minimal layout with slicers for easy filtering

---

## 📁 Files Included
- `HR_Attrition_Analysis.pbix` – Power BI interactive dashboard
- `Cleaned_Employee_Attrition.xlsx` – Cleaned dataset used in the dashboard
- `analysis.py` – Python script for quick attrition rate and department-wise analysis

---

## 🧰 Tools & Technologies
- **Power BI** – For data visualization and dashboarding
- **Excel** – For initial data cleaning
- **Python (pandas)** – For basic EDA and CLI summary
- **Dataset Source** – [IBM HR Analytics on Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

---

## 📈 Key Insights
- 🔸 Highest attrition is among younger employees (age 20–30)
- 🔸 Sales and Research departments see the most exits
- 🔸 Most attrition happens within the first 1–2 years at the company

---

## ⚙️ Run the Python Script (Optional)
To get quick stats in terminal:

```bash

git clone https://github.com/lisadascse72/HR-Attrition-Analysis.git
cd HR-Attrition-Analysis
python analysis.py
