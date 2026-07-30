from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

CSV_FILE_PATH = PROJECT_ROOT / "data" / "spanish.csv"

CATEGORY_TO_FILTER = "Spanisch lernen"

CHROME_USER_DATA_DIR = Path.cwd() / "dreaming_spanish_profile"

CHROME_PROFILE_NAME = "Default"

TARGET_URL = "https://app.dreaming.com/spanish/progress/time-outside"
