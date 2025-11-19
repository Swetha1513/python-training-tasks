import polars as pl

print("Customer Data Filter & Exporter\n================================\n")

# Load data
df = pl.read_csv('customers.csv')
print(f"Total customers loaded: {df.height}\n")

# Apply filters
filtered = df.filter((pl.col("Purchase_Amount") > 1000) & (pl.col("Country") == "USA"))
print("Filtered results\n-----------------\n", filtered)

# Summary
print("\nSummary Statistics:\n-----------------\n")
print(f"Total customers found: {filtered.height}")
print(f"Average purchase amount: {filtered['Purchase_Amount'].mean():.2f}")

# Export
filtered.write_csv('filtered_customers.csv')
print("\nExporting to ‘filtered_customers.csv’...\nExport complete! ")