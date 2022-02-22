import collections
import matplotlib.pyplot as plt
from . import Expense

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

# Use collection Counter to count how many purchases were in each category
spending_counter = collections.Counter(spending_categories)
print(spending_counter)
top5 = spending_counter.most_common(5)
print("Number of categories = " + str(spending_counter.__len__()))
#print(top5)

# zip puts 2 lists into a dict, *zip does the reverse
categories, count = zip(*top5)

#construct graph
fig,ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show()
