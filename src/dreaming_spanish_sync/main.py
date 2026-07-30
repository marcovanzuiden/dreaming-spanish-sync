import pandas as pd

from dreaming_spanish_sync.config import (
    CATEGORY_TO_FILTER,
    CSV_FILE_PATH,
)
from dreaming_spanish_sync.csv_loader import load_activities


def main():
    start_date_input = input(
        "Frome which date one shoud we import the listings? (YYYY-MM-DD): "
    )

    start_date = pd.to_datetime(
        start_date_input,
        format="%Y-%m-%d",
    )

    activities = load_activities(
        CSV_FILE_PATH,
        CATEGORY_TO_FILTER,
        start_date,
    )

    print(activities)


if __name__ == "__main__":
    main()
