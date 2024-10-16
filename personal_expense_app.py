# import streamlit as st
# import datetime
# from datetime import date

# st.header("PERSONAL EXPENSE TRACKER")

# st.subheader("Track your expenses easily !!")

# st.date_input("Date: ", datetime.date(2019, 7, 6))

# Desc = st.text_input("Description: ", "This is a tracker to track our own personal expenses.")

# Amt = st.number_input("Enter the expense !")

# Category = st.selectbox("choose a category : " ,("Travel", "Food", "Rent", "Misc"))

# st.button("Submit")

# st.subheader("Expenses List")

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.markdown("Date")
# with col2:
#     st.markdown("Description")
# with col3:
#     st.markdown("Amount")


# import streamlit as st
# from datetime import datetime

# # Initialize an empty list to store expenses
# if 'expenses' not in st.session_state:
#     st.session_state.expenses = []

# st.header("PERSONAL EXPENSE TRACKER")
# st.subheader("Track your expenses easily!")

# # Date input with today's date as default
# date = st.date_input("Date: ", datetime.today())

# # Input fields
# description = st.text_input("Description: ", "Enter a brief description.")
# amount = st.number_input("Enter the expense!", min_value=0.0, format="%.2f")
# category = st.selectbox("Choose a category:", ("Travel", "Food", "Rent", "Misc"))

# # Submit button
# if st.button("Submit"):
#     # Create a new expense entry
#     new_expense = {"Date": date, "Description": description, "Amount": amount, "Category": category}
#     # Append the new expense to the session state
#     st.session_state.expenses.append(new_expense)
#     st.success("Expense added successfully!")

# # Display the expenses list
# st.subheader("Expenses List")


# if st.session_state.expenses:
#     # Create columns for the expense list
#     col1, col2, col3, col4 = st.columns(4)

#     with col1:
#         st.markdown("**Date**")
#         for expense in st.session_state.expenses:
#             st.markdown(str(expense["Date"]))

#     with col2:
#         st.markdown("**Description**")
#         for expense in st.session_state.expenses:
#             st.markdown(expense["Description"])

#     with col3:
#         st.markdown("**Amount**")
#         for expense in st.session_state.expenses:
#             st.markdown(f"${expense['Amount']:.2f}")

#     with col4:
#         st.markdown("**Category**")
#         for expense in st.session_state.expenses:
#             st.markdown(expense["Category"])
# else:
#     st.write("No expenses recorded yet.")




import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Ensure that 'expenses' is a DataFrame
if 'expenses' not in st.session_state or not isinstance(st.session_state.expenses, pd.DataFrame):
    st.session_state.expenses = pd.DataFrame(columns=["Date", "Description", "Amount", "Category"])

# Title and Description
st.title("Personal Expense Tracker")
st.write("Track your expenses easily and visualize your spending habits.")

# User Input Form
st.sidebar.header("Add an Expense")
with st.sidebar.form(key='expense_form'):
    date = st.date_input("Date:", datetime.today())
    description = st.text_input("Description:")
    amount = st.number_input("Enter the expense:", min_value=0, format="%d")  # No decimals allowed
    category = st.selectbox("Choose a category:", ["Food", "Transport", "Entertainment", "Utilities", "Misc"])
    submit_button = st.form_submit_button("Add Expense")

    if submit_button:
        if description:  # Check if description is provided
            # Create a new expense entry as a DataFrame
            new_expense = pd.DataFrame({
                "Date": [date],
                "Description": [description],
                "Amount": [amount],
                "Category": [category]
            })
            # Append the new expense to the session state DataFrame
            st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense], ignore_index=True)
            st.success("Expense added successfully!")
        else:
            st.warning("Please enter a description.")

# Expense List
st.subheader("Expenses List")
if not st.session_state.expenses.empty:
    for index, row in st.session_state.expenses.iterrows():
        col1, col2, col3, col4, col5 = st.columns([1, 2, 1, 1, 0.5])
        
        with col1:
            st.write(row["Date"])
        with col2:
            st.write(row["Description"])
        with col3:
            st.write(f"${int(row['Amount'])}")  # Display amount as an integer
        with col4:
            st.write(row["Category"])
        with col5:
            delete_button = st.button("Dlt", key=f"delete_{index}", help="Delete this expense")
            if delete_button:
                st.session_state.expenses = st.session_state.expenses.drop(index).reset_index(drop=True)
                # st.experimental_rerun()  # Rerun to refresh the view
else:
    st.write("No expenses recorded yet.")

# Summary Statistics
if not st.session_state.expenses.empty:
    total_expenses = st.session_state.expenses["Amount"].sum()
    average_expense = st.session_state.expenses["Amount"].mean()
    highest_expense = st.session_state.expenses["Amount"].max()

    st.subheader("Summary Statistics")
    st.write(f"Total Expenses: ${int(total_expenses)}")  # No decimals
    st.write(f"Average Expense: ${int(average_expense)}")  # No decimals
    st.write(f"Highest Expense: ${int(highest_expense)}")  # No decimals

    # Visualizations
    st.subheader("Spending by Category")
    category_summary = st.session_state.expenses.groupby("Category")["Amount"].sum()
    plt.figure(figsize=(10, 5))
    category_summary.plot(kind='bar', color='skyblue')
    plt.title('Total Spending by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    st.pyplot(plt)

    st.subheader("Expenses Over Time")
    time_summary = st.session_state.expenses.groupby("Date")["Amount"].sum()
    plt.figure(figsize=(10, 5))
    time_summary.plot(kind='line', marker='o', color='orange')
    plt.title('Expenses Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Amount')
    st.pyplot(plt)

# Add custom CSS to adjust the button width
st.markdown(
    """
    <style>
    div.stButton > button {
        width: 100%;
        height: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)






       


