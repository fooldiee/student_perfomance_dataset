import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/ultimate_student_productivity_dataset_5000.csv")

# 1. Гистограммы
plt.figure()
plt.hist(df["exam_score"], bins=20)
plt.title("Распределение exam_score")
plt.show()

plt.figure()
plt.hist(df["burnout_level"], bins=20)
plt.title("Распределение burnout_level")
plt.show()

# 2. Столбчатая
counts = df["academic_level"].value_counts()
plt.figure()
plt.bar(counts.index, counts.values)
plt.title("Academic Level")
plt.show()

# 3. Круговая
plt.figure()
plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%')
plt.title("Academic Level %")
plt.show()

# 4. Линейный
plt.figure()
plt.plot(df["exam_score"].values[:100])
plt.title("Динамика exam_score")
plt.show()

# 5. Сравнительная
means = df[["exam_score", "burnout_level"]].mean()
plt.figure()
plt.bar(means.index, means.values)
plt.title("Средние значения")
plt.show()