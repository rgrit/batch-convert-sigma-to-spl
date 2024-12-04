import os
import yaml
import pandas as pd


def get_sigma_title(file_path):
    """
    Extracts the title field from a Sigma rule YAML file.

    :param file_path: Path to the YAML file.
    :return: The title of the Sigma rule or None if not found.
    """
    try:
        with open(file_path, 'r') as file:
            sigma_rule = yaml.safe_load(file)
            return sigma_rule.get("title", "Title not found")
    except yaml.YAMLError as e:
        return f"Error parsing YAML: {e}"
    except Exception as e:
        return f"Error reading file: {e}"


def process_directory_to_excel(directory_path, output_file):
    """
    Recursively processes a directory of YAML files and saves file path,
    file name, and title information to an Excel file.

    :param directory_path: Path to the directory.
    :param output_file: Path to save the Excel file.
    """
    if not os.path.isdir(directory_path):
        print(f"The provided path is not a directory: {directory_path}")
        return

    data = []  # List to store file info

    for root, _, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(".yaml") or file_name.endswith(".yml"):
                file_path = os.path.join(root, file_name)
                title = get_sigma_title(file_path)
                data.append({
                    "File Path": file_path,
                    "File Name": file_name,
                    "Title": title
                })

    # Convert to DataFrame and save as Excel
    df = pd.DataFrame(data, columns=["File Path", "File Name", "Title"])
    df.to_excel(output_file, index=False)
    print(f"Excel file created: {output_file}")


# Specify the directory containing YAML files and output file path
directory = r"C:\Users\jsph_\PycharmProjects\Sigma\test_rules"  # Change this to your directory
output_excel = "sigma_rules_output.xlsx"

process_directory_to_excel(directory, output_excel)
