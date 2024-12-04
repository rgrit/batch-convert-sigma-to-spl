import os
import yaml


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


def process_directory(directory_path):
    """
    Finds all YAML files in a directory and extracts their titles.

    :param directory_path: Path to the directory.
    """
    if not os.path.isdir(directory_path):
        print(f"The provided path is not a directory: {directory_path}")
        return

    print(f"Processing directory: {directory_path}\n")
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".yaml") or file_name.endswith(".yml"):
            file_path = os.path.join(directory_path, file_name)
            title = get_sigma_title(file_path)
            print(f"File: {file_name} -> Title: {title}")


# Specify the directory containing YAML files
directory = r"C:\Users\jsph_\PycharmProjects\Sigma\test_rules\test_rules_1"  # Change this to the path of your directory
process_directory(directory)
