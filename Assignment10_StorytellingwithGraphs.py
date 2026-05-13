import matplotlib.pyplot as plt
# Sample data
subjects = ["Math", "Science", "English", "Computer", "History"]
marks = [85, 78, 90, 92, 70]

# Bar Chart
plt.bar(subjects, marks)
plt.title("Marks in Different Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Pie Chart
plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.show()

# Histogram
plt.hist(marks)
plt.title("Marks Frequency Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()