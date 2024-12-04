import os
import yaml
import pandas as pd
from sigma.collection import SigmaCollection
from sigma.backends.splunk import SplunkBackend
from sigma.exceptions import SigmaError


def get_sigma_title(file_path):
    """
    Extracts the title field from a Sigma rule YAML file.

    :param file_path: Path to the YAML file.
    :return: The title of the Sigma rule or 'Title not found'.
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

    :param file_path: Path to the YAML file.
    :return: The Splunk query or an error message.
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


def process_directory_recursive_to_excel(directory_path, output_file):
    """
    Recursively finds all YAML files in a directory and its subdirectories,
    extracts their titles, converts the rules to Splunk queries,
    and saves the results to an Excel file.

    :param directory_path: Path to the directory.
    :param output_file: Path to save the Excel file.
    """
    if not os.path.isdir(directory_path):
        print(f"The provided path is not a directory: {directory_path}")
        return

    data = []  # Store results for Excel
    print(f"Processing directory: {directory_path}\n")

    for root, _, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(".yaml") or file_name.endswith(".yml"):
                file_path = os.path.join(root, file_name)
                title = get_sigma_title(file_path)
                splunk_query = convert_to_splunk(file_path)

                # Add results to the list for Excel output
                data.append({
                    "File Path": file_path,
                    "File Name": file_name,
                    "Title": title,
                    "Splunk Query": splunk_query
                })

                # Print to the terminal
                print(f"File: {file_path}")
                print(f"Title: {title}")
                print(f"Splunk Query: {splunk_query}\n")

    # Save to Excel
    df = pd.DataFrame(data, columns=["File Path", "File Name", "Title", "Splunk Query"])
    df.to_excel(output_file, index=False)
    print(f"Excel file created: {output_file}")


# Specify the directory containing YAML files and the output Excel file path
directory = r"test_rules"  # Change this to your directory
output_excel = "sigma_rules_output.xlsx"

# Process the directory and save results to Excel
process_directory_recursive_to_excel(directory, output_excel)
