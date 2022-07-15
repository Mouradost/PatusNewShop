# ! Expense by category
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from DB.DBHandler import DBHelper

db = DBHelper()


df = pd.read_sql_query(
    """
SELECT ExpenseCategory.name, sum(price * quantity) AS 'total' FROM Expense JOIN ExpenseCategory ON Expense.category=ExpenseCategory._id WHERE date BETWEEN '2022-05-04' AND '2022-05-06' GROUP BY category;
""",
    db.conn,
)
sns.barplot(x="name", y="total", data=df)
plt.show()
print(df.head())

"""
SELECT ExpenseCategory.name, sum(price * quantity) AS 'total' FROM Expense JOIN ExpenseCategory ON Expense.category=ExpenseCategory._id WHERE date BETWEEN '2022-05-04' AND '2022-05-06' GROUP BY category;
"""

# ! All Expenses
"""
SELECT sum(price * quantity) FROM Expense WHERE date BETWEEN '2022-05-04' AND '2022-05-06';
"""

# ! All Sells
"""
SELECT sum(total) FROM Sells WHERE date BETWEEN '2022-05-04' AND '2022-05-06';
"""

# ! All Payement
"""
SELECT sum(amount) FROM Payment WHERE date BETWEEN '2022-05-04' AND '2022-05-06';
"""
