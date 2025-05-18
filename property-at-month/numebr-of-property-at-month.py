
import pandas as pd
import matplotlib.pyplot as plt

# تحميل الملف
df = pd.read_excel("DocRealestateSale.xlsx", engine='openpyxl')
df.columns = df.columns.str.strip()


# تحويل التاريخ
df["تاريخ الصفقة ميلادي"] = pd.to_datetime(df["تاريخ الصفقة ميلادي"], errors='coerce')
df["الشهر"] = df["تاريخ الصفقة ميلادي"].dt.month

# تجميع عدد الصفقات حسب الشهر
monthly_counts = df["الشهر"].value_counts().sort_index()

# أسماء الشهور بالعربي
arabic_months = [
    "يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو",
    "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"
]


# ✅ حفظ الجدول في ملف نصي
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("🔹 عدد الصفقات لكل شهر ميلادي:\n\n")
    f.write(f"{'الشهر':<15}{'عدد الصفقات':>15}\n")
    f.write("-" * 30 + "\n")
    for month_number, count in monthly_counts.items():
        f.write(f"{arabic_months[month_number - 1]:<15}{count:>15}\n")

               

# ✅ رسم بياني
plt.figure(figsize=(10, 6))
plt.plot(monthly_counts.index, monthly_counts.values, marker='o', linestyle='-', color='teal')
plt.xticks(monthly_counts.index, [arabic_months[i-1] for i in monthly_counts.index], rotation=45)
plt.title("عدد الصفقات في كل شهر ميلادي")
plt.xlabel("الشهر")
plt.ylabel("عدد الصفقات")
plt.grid(True)
plt.tight_layout()
plt.savefig("عدد_الصفقات_لكل_شهر.png")  # حفظ الرسم كصورة
plt.show()
