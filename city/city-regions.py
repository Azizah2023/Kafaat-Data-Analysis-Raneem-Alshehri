import pandas as pd
import matplotlib.pyplot as plt
import sys

# تعريب مخرجات التيرمنال (خاص بالماك)
sys.stdout.reconfigure(encoding='utf-8')

# ✅ تحميل ملف الإكسل
df = pd.read_excel("DocRealestateSale.xlsx", engine='openpyxl')
df.columns = df.columns.str.strip()

# نفتح ملف لحفظ المخرجات
with open("city.txt", "w", encoding="utf-8") as f:
    
    # ✅ عدد المناطق
    num_regions = df["المنطقة"].nunique()
    f.write(f"🔹 عدد المناطق: {num_regions}\n")

    # ✅ عدد المدن في كل منطقة
    cities_per_region = df.groupby("المنطقة")["المدينة"].nunique()
    f.write("\n🔸 عدد المدن في كل منطقة:\n")
    for region, count in cities_per_region.items():
        f.write(f"📍 {region}: {count} مدينة\n")

        # ✅ رسم عدد المدن في كل منطقة
plt.figure(figsize=(12, 6))
cities_per_region.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("عدد المدن في كل منطقة")
plt.xlabel("المنطقة")
plt.ylabel("عدد المدن")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("عدد_المدن_في_كل_منطقة.png")  # حفظ الرسم