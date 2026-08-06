# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "Most Streamed Artists on Spotify (17_07_2026) V1.1.csv"

# Load the latest version
df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "rishavsvault/most-streamed-artists-on-spotify",
        file_path
    )

print("First 5 records:", df.head())