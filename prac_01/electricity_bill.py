"""Electricity bill estimator 2.0 """

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff_used = int(input("Which tariff? 11 or 31: "))
while tariff_used != 11 and 31 != tariff_used:
    tariff_used = int(input("Which tariff? 11 or 31: "))

if tariff_used == 11:
    cents_per_kwh = TARIFF_11
else:
    cents_per_kwh = TARIFF_31

# cents_per_kwh = float(input("Enter cents per kWh: "))
daily_use_kwh = float(input("Enter daily use in kWh: "))
days_billed = int(input("Enter number of billing days: "))

estimated_cost = cents_per_kwh * daily_use_kwh * days_billed

print(f"Estimated bill: ${estimated_cost:.2f}")
