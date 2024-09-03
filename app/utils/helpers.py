# app/utils/helpers.py
import re
from datetime import datetime
import json

def sanitize_string(input_string: str) -> str:
    """
    Remove special characters and extra whitespace from a string.
    """
    # Remove special characters
    sanitized = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
    # Remove extra whitespace
    sanitized = ' '.join(sanitized.split())
    return sanitized

def format_datetime(dt: datetime) -> str:
    """
    Format a datetime object to a string.
    """
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def load_json_file(file_path: str) -> dict:
    """
    Load a JSON file and return its contents as a dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Invalid JSON in file: {file_path}")
        return {}

def save_json_file(data: dict, file_path: str) -> None:
    """
    Save a dictionary as a JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def truncate_string(input_string: str, max_length: int) -> str:
    """
    Truncate a string to a maximum length, adding '...' if truncated.
    """
    if len(input_string) <= max_length:
        return input_string
    return input_string[:max_length - 3] + '...'

def generate_unique_id() -> str:
    """
    Generate a unique ID based on the current timestamp.
    """
    return datetime.now().strftime('%Y%m%d%H%M%S%f')