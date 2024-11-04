import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from tqdm import tqdm
import time

# Input and output directories
INPUT_DIR = "input"
OUTPUT_DIR = "output"


def clean_text(text):
    """
    Cleans the text by:
    - Removing unwanted prefixes like "Description: " and "Video Transcript "
    """
    text = text.replace("Description:", "").replace("Video Transcript ", "")
    return text.strip()


def scrape_career_data(career_url):
    """
    Scrapes the career page at the provided URL to extract:
    - Description of the career (without "Description:" prefix)
    - Video URL for the career video
    - Transcript text (without "Video Transcript" prefix)

    Returns:
        description (str), video_url (str), transcript (str)
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(career_url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract and clean description
        description_tag = soup.find(id="ctl16_ctl00_videoDesc")
        description = (
            clean_text(description_tag.get_text(strip=True))
            if description_tag
            else "N/A"
        )

        # Extract video URL from the <video> tag
        video_tag = soup.find("video")
        video_url = video_tag["src"] if video_tag else "N/A"

        # Extract and clean transcript
        transcript_tag = soup.find(id="ctl16_ctl00_videoScript")
        transcript = (
            clean_text(transcript_tag.get_text(separator=" ", strip=True))
            if transcript_tag
            else "N/A"
        )

        return description, video_url, transcript

    except requests.RequestException as e:
        print(f"Error fetching {career_url}: {e}")
        return "N/A", "N/A", "N/A"


def main():
    input_csv = os.path.join(INPUT_DIR, "career_videos.csv")
    output_csv = os.path.join(OUTPUT_DIR, "career_data_output.csv")

    careers_data = []

    with open(input_csv, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

        for row in tqdm(rows, desc="Scraping Career Data", unit="career"):
            career_name = row["Career"]
            career_url = row["URL"]

            description, video_url, transcript = scrape_career_data(career_url)

            careers_data.append(
                {
                    "Career": career_name,
                    "COS URL": career_url,
                    "Description": description,
                    "Video URL": video_url,
                    "Transcript": transcript,
                }
            )

            time.sleep(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df = pd.DataFrame(careers_data)
    df.to_csv(output_csv, index=False, encoding="utf-8")
    print(f"Data saved to {output_csv}")


if __name__ == "__main__":
    main()
