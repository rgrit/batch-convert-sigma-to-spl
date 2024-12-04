import pandas as pd

# File paths
input_file = r"C:\Users\jsph_\PycharmProjects\Sigma\sigma_rules_output.csv"
output_file = r"/sigma_rules_output.csv"

# Search and replace strings
search_string = r"C:\\Users\\jsph_"  # Escape backslashes
replace_string = r"C:\\SigmaRules"

# Load the CSV file
df = pd.read_csv(input_file)

# Replace all instances in the entire DataFrame
df = df.replace(to_replace=search_string, value=replace_string, regex=True)

# Save the updated CSV file
df.to_csv(output_file, index=False)

print(f"All instances of '{search_string}' have been replaced with '{replace_string}'.")
print(f"Updated file saved at: {output_file}")
