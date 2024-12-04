import yaml


def get_sigma_title(yaml_content):
    """
    Extracts the title field from a Sigma rule.

    :param yaml_content: String containing the Sigma rule in YAML format.
    :return: The title of the Sigma rule or None if not found.
    """
    try:
        sigma_rule = yaml.safe_load(yaml_content)
        return sigma_rule.get("title", "Title not found")
    except yaml.YAMLError as e:
        return f"Error parsing YAML: {e}"


# Example Sigma rule
sigma_yaml = """
title: Example Sigma Rule
id: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
description: Detects [brief explanation of suspicious or malicious behavior]
logsource:
  category: system
  product: windows
detection:
  selection:
    EventID: 4624
  condition: selection
falsepositives:
  - Unknown
level: medium
tags:
  - attack.execution
"""

# Extract and print the title
title = get_sigma_title(sigma_yaml)
print(f"Title: {title}")
