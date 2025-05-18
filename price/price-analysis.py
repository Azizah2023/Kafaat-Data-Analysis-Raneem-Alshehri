
import pandas as pd
import matplotlib.pyplot as plt
import sys

# تعريب مخرجات التيرمنال (خاص بالماك)
sys.stdout.reconfigure(encoding='utf-8')

# ✅ تحميل ملف الإكسل
df = pd.read_excel("DocRealestateSale.xlsx", engine='openpyxl')
df.columns = df.columns.str.strip()

# نفتح ملف للكتابة
with open("price.txt", "w", encoding="utf-8") as f:

  # ✅ أقل سعر
    min_price = df["السعر"].min()
    min_price_row = df[df["السعر"] == min_price].iloc[0]
    f.write(f"\n⬇️ أقل سعر: {min_price:.2f} ريال في مدينة: {min_price_row['المدينة']} ({min_price_row['المنطقة']})\n")

    # ✅ أعلى سعر
    max_price = df["السعر"].max()
    max_price_row = df[df["السعر"] == max_price].iloc[0]
    f.write(f"⬆️ أعلى سعر: {max_price:.2f} ريال في مدينة: {max_price_row['المدينة']} ({max_price_row['المنطقة']})\n")

    # ✅ متوسط السعر
    avg_price = df["السعر"].mean()
    f.write(f"📊 متوسط السعر العام: {avg_price:.2f} ريال\n")
