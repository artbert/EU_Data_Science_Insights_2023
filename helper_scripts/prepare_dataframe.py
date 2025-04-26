import ast
import pandas as pd
from datasets import load_dataset

EUROPEAN_COUNTRIES = [
    "Germany",
    "United Kingdom",
    "France",
    "Italy",
    "Spain",
    "Ukraine",
    "Poland",
    "Romania",
    "Netherlands",
    "Belgium",
    "Sweden",
    "Czech Republic",
    "Portugal",
    "Greece",
    "Hungary",
    "Austria",
    "Belarus",
    "Switzerland",
    "Bulgaria",
    "Serbia",
    "Denmark",
    "Finland",
    "Norway",
    "Slovakia",
    "Ireland",
    "Croatia",
    "Bosnia and Herzegovina",
    "Moldova",
    "Lithuania",
    "Albania",
    "Slovenia",
    "Latvia",
    "North Macedonia",
    "Estonia",
    "Luxembourg",
    "Montenegro",
    "Malta",
    "Iceland",
    "Andorra",
    "Liechtenstein",
    "Monaco",
    "San Marino",
    "Holy See",
]


def load_and_clean_data() -> pd.DataFrame:
    """Load and clean the job dataset."""
    dataset = load_dataset("lukebarousse/data_jobs")
    df = dataset["train"].to_pandas()
    df["job_posted_date"] = pd.to_datetime(df["job_posted_date"])
    df["job_skills"] = df["job_skills"].apply(
        lambda x: ast.literal_eval(x) if pd.notna(x) else x
    )
    return df


def get_fulldataframe() -> pd.DataFrame:
    """Get the full dataframe with cleaned data."""
    return load_and_clean_data()


def get_european_dataframe() -> pd.DataFrame:
    """Get the dataframe filtered for European countries."""
    df = load_and_clean_data()
    return df[df["job_country"].isin(EUROPEAN_COUNTRIES)]
