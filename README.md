# Sigma to Splunk Conversion Script

## Overview
This script automates the processing of Sigma rules, providing a seamless way to convert them into Splunk-compatible queries. It recursively scans directories of Sigma YAML files, extracts critical metadata (e.g., rule titles), and generates Splunk queries. The output is displayed in the terminal for immediate feedback and saved to a CSV file for further analysis and documentation.

---

## Key Features
- **Recursive Directory Processing**: Scans all subdirectories for Sigma YAML files.
- **Rule Metadata Extraction**: Extracts key information, including file path, file name, and rule title.
- **Splunk Query Conversion**: Converts Sigma rules into Splunk-compatible queries using the Sigma library.
- **Dual Output Format**: Displays results in the terminal and saves them to a CSV file.
- **Error Handling**: Handles invalid YAML syntax and failed conversions gracefully.

---

## Requirements
- **Python Version**: Python 3.8 or higher
- **Dependencies**:
  - `PyYAML`: For parsing YAML files.
  - `pandas`: For CSV output generation.
  - `sigma`: For parsing and converting Sigma rules.

Install the required dependencies using the following command:
```bash
pip install PyYAML pandas sigma
```

---

## Installation and Setup
1. Clone or download this repository to your local machine:
   ```bash
   git clone https://github.com/rgrit/batch-convert-sigma-to-splunk.git
   cd batch-convert-sigma-to-splunk
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place your Sigma YAML files in a directory or prepare the path to an existing repository of Sigma rules.

---

## Usage
1. Configure the following variables in the script:
   - `directory`: Path to the directory containing Sigma YAML files.
   - `output_csv`: Path to save the CSV output file.

2. Run the script:
   ```bash
   python batch_convert_spl.py
   ```

3. Review the results:
   - **Terminal Output**: Displays the file path, title, and Splunk query for each processed rule.
   - **CSV Output**: A CSV file containing the following columns:
     - `File Path`
     - `File Name`
     - `Title`
     - `Splunk Query`

---

## Output Example

### Terminal Output
```
Processing directory: C:\SigmaRules

File: C:\SigmaRules\rule1.yaml
Title: Example Rule
Splunk Query: (EventID="4624")

File: C:\SigmaRules\subdir\rule2.yaml
Title: Unauthorized Access Rule
Splunk Query: (ProcessName="cmd.exe")
```

### CSV Output
| **File Path**                             | **File Name**      | **Title**                | **Splunk Query**          |
|-------------------------------------------|--------------------|--------------------------|---------------------------|
| C:\SigmaRules\rule1.yaml                  | rule1.yaml         | Example Rule             | (EventID="4624")          |
| C:\SigmaRules\subdir\rule2.yaml           | rule2.yaml         | Unauthorized Access Rule | (ProcessName="cmd.exe")   |

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing
Contributions are welcome. Please fork the repository, create a feature branch, and submit a pull request. For major changes, please open an issue to discuss your proposed changes.

---

This README provides a comprehensive guide for setting up, using, and understanding the script. It reflects the latest version of the code and supports its professional use in security operations.
