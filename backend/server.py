from fastapi import FastAPI, HTTPException
from datetime import date
import db_connection
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date

#for Add/update
@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expense(expense_date: date):
    expenses = db_connection.fetch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense from database")

    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses:List[Expense]):
    db_connection.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_connection.insert_expense(expense_date, expense.amount, expense.category, expense.notes)

    return {"Expense Successfully Added"}


#for Analytics by category
@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data = db_connection.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from database")

    total = sum([row['total'] for row in data])

    breakdown={}
    for row in data:
        percentage = (row['total'] / total) * 100 if total != 0 else 0
        breakdown[row['category']] = {
            "total": row['total'],
            "percentage": percentage
        }

    return breakdown


#for Analytics by Months
@app.get("/monthly-expenses")
def get_monthly_expenses():
    month_data = db_connection.fetch_monthly_expenses()
    if month_data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve months by expense from database")

    return month_data