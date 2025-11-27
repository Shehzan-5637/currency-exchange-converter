print("=== Currency Converter ===")

pkr = float(input("Enter amount in PKR: "))

usd_rate = 277.50
eur_rate = 300.10
gbp_rate = 350.25
inr_rate = 3.33
aed_rate = 75.50

print("\nConverted Amounts:")
print(f"USD: {pkr / usd_rate:.2f}")
print(f"EUR: {pkr / eur_rate:.2f}")
print(f"GBP: {pkr / gbp_rate:.2f}")
print(f"INR: {pkr / inr_rate:.2f}")
print(f"AED: {pkr / aed_rate:.2f}")
