import os
import yaml
import pandas as pd
from sigma.collection import SigmaCollection
from sigma.backends.splunk import SplunkBackend
from sigma.exceptions import SigmaError


def clean_data(value):
    """
    Cleans data for CSV output by removing invalid characters or truncating long strings.
    """
    if isinstance(value, str):
        # Replace invalid characters
        value = value.replace("*", "").replace("?", "").replace("\"", "").strip()
        # Truncate excessively long strings
        if len(value) > 32000:  # Typical safe limit for CSV files
            value = value[:32000] + "..."
    return value


def get_sigma_title(file_path):
    """
    Extracts the title field from a Sigma rule YAML file.
    """
    try:
        with open(file_path, 'r') as file:
            sigma_rule = yaml.safe_load(file)
            return sigma_rule.get("title", "Title not found")
    except yaml.YAMLError as e:
        return f"Error parsing YAML: {e}"
    except Exception as e:
        return f"Error reading file: {e}"


def convert_to_splunk(file_path):
    """
    Converts a Sigma rule to a Splunk query.
    """
    try:
        with open(file_path, 'r') as file:
            sigma_rule = file.read()

        # Parse the Sigma rule as a collection
        sigma_collection = SigmaCollection.from_yaml(sigma_rule)

        # Create the Splunk backend
        splunk_backend = SplunkBackend()

        # Convert the Sigma rules to Splunk query
        splunk_query = splunk_backend.convert(sigma_collection)
        return "\n".join(splunk_query)
    except SigmaError as e:
        return f"Error converting to Splunk: {e}"
    except Exception as e:
        return f"Error reading file: {e}"


def process_directory_recursive_to_csv(directory_path, output_file):
    """
    Recursively processes a directory of YAML files, extracts metadata, and saves results to a CSV file.
    """
    if not os.path.isdir(directory_path):
        print(f"The provided path is not a directory: {directory_path}")
        return

    data = []  # Store results for CSV output
    print(f"Processing directory: {directory_path}\n")

    for root, _, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(".yaml") or file_name.endswith(".yml"):
                file_path = os.path.join(root, file_name)
                title = get_sigma_title(file_path)
                splunk_query = convert_to_splunk(file_path)

                # Add results to the list for CSV output
                data.append({
                    "File Path": clean_data(file_path),
                    "File Name": clean_data(file_name),
                    "Title": clean_data(title),
                    "Splunk Query": clean_data(splunk_query)
                })

                # Print to the terminal
                print(f"File: {file_path}")
                print(f"Title: {title}")
                print(f"Splunk Query: {splunk_query}\n")

    # Save to CSV
    df = pd.DataFrame(data, columns=["File Path", "File Name", "Title", "Splunk Query"])
    df.to_csv(output_file, index=False)
    print(f"CSV file created: {output_file}")


# Specify the directory containing YAML files and the output CSV file path
directory = r"C:\SigmaRules\sigma\rules"  # Change this to your directory
output_csv = "sigma_rules_output.csv"

# Process the directory and save results to CSV
process_directory_recursive_to_csv(directory, output_csv)
