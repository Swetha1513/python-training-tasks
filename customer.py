import pandas as pd

print("Customer Data Filter & Exporter\n================================\n")

# Load data
df = pd.read_csv('customers.csv')
print(f"Total customers loaded: {len(df)}\n")

# Apply filters
filtered = df.query("Purchase_Amount > 1000 and Country == 'USA'")
print("Filtered results\n-----------------\n", filtered)

# Summary
print("\nSummary Statistics:\n-----------------\n")
print(f"Total customers found: {len(filtered)}")
print(f"Average purchase amount: {filtered['Purchase_Amount'].mean():.2f}")

# Export
filtered.to_csv('filtered_customers.csv', index=False)
print("\nExporting to ‘filtered_customers.csv’...\nExport complete! ")