from io import StringIO
from pathlib import Path

import pandas as pd


def load_activities(
    csv_path: Path,
    category: str,
    start_date: pd.Timestamp,
) -> pd.DataFrame:
    """
    Load, clean and filter activity data from the Simple Time Tracker CSV export.
    """

    with csv_path.open("r", encoding="utf-8") as file:
        lines = file.readlines()

    cleaned_lines = []

    for line in lines:
        line_str = line.strip()

        if line_str.startswith('"') and line_str.endswith('"'):
            line_str = line_str[1:-1].replace('""', '"')

        cleaned_lines.append(line_str)

    csv_data = "\n".join(cleaned_lines)

    df = pd.read_csv(StringIO(csv_data))

    df.columns = df.columns.str.strip()

    df["parsed_date"] = pd.to_datetime(
        df["time started"],
        errors="coerce",
    )

    df = df.dropna(subset=["parsed_date"])

    df["categories"] = df["categories"].fillna("").astype(str).str.strip()

    filter_mask = (df["categories"] == category) & (df["parsed_date"] >= start_date)

    filtered_df = df[filter_mask].copy()

    filtered_df = filtered_df.sort_values(by="parsed_date")

    return filtered_df.drop(columns=["parsed_date"])
