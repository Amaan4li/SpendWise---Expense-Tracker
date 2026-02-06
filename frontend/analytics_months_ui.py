import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"


def analytics_months_tab():
        response = requests.get(f"{API_URL}/monthly-expenses")
        monthly_data = response.json()

        df = pd.DataFrame(monthly_data)
        df.rename(columns={
            "expense_month" : "Months Number",
            "month_name" : "Months Name",
            "total" : "Total Expenses",
        }, inplace=True)
        df_sorted = df.sort_values("Months Number", ascending=False)
        df_sorted.set_index(["Months Number"], inplace=True)

        st.bar_chart(data = df_sorted.set_index("Months Name")["Total Expenses"], width='stretch')

        df_sorted["Total Expenses"] = df_sorted["Total Expenses"].map("{:,.2f}".format)

        st.subheader("📅 Monthly Expense Trends")
        st.table(df_sorted.sort_index())

