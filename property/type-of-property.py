import pandas as pd
import matplotlib.pyplot as plt
import sys

# تعريب مخرجات التيرمنال (خاص بالماك)
sys.stdout.reconfigure(encoding='utf-8')

# ✅ تحميل ملف الإكسل
df = pd.read_excel("DocRealestateSale.xlsx", engine='openpyxl')
df.columns = df.columns.str.strip()

# نفتح ملف لحفظ المخرجات
with open("property.txt", "w", encoding="utf-8") as f:
    
  
    # ✅ عدد الصفقات حسب التصنيف والنوع
    grouped = df.groupby(["تصنيف العقار", "نوع العقار"]).size().sort_values(ascending=False)
    labels = [f"{index[0]} - {index[1]}" for index in grouped.index]
    
    f.write("\n🔹 عدد الصفقات حسب التصنيف والنوع:\n\n")
    for label, count in zip(labels, grouped.values):
        f.write(f"{label}: {count} صفقة\n")

        # ✅ رسم Pie Chart للصفقات حسب النوع والتصنيف
plt.clf()
plt.figure(figsize=(10, 10))
plt.pie(grouped.values, labels=labels, autopct="%1.1f%%", startangle=140)
plt.title("توزيع الصفقات حسب تصنيف العقار ونوع العقار")
plt.axis("equal")
plt.tight_layout()
plt.savefig("توزيع_الصفقات_تصنيف_ونوع.png")  # حفظ الرسم
