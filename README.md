# CareerOneStop Video Scraper

This project is a web scraper designed to extract career information from CareerOneStop career video pages. It reads a list of career URLs from an input CSV file, scrapes each page for relevant information (such as career descriptions, video URLs, and transcripts), and outputs the data to a new CSV file.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Output](#output)
- [Duplicate Career Check](#duplicate-career-check)
- [Troubleshooting](#troubleshooting)

## Features

- Scrapes career descriptions, video URLs, and transcripts from CareerOneStop.
- Uses Docker for environment consistency and easy deployment.
- Excludes video duration calculation for simplicity and to avoid access restrictions.
- Outputs the collected data in a clean CSV format for easy analysis.

## Project Structure

- `main.py` - Main Python script for scraping career data.
- `Dockerfile` - Docker configuration file for building the containerized environment.
- `docker-compose.yml` - Manages the Docker container for the project.
- `input/` - Folder to store input CSV files (place `career_urls.csv` here).
- `output/` - Folder where the output CSV file will be saved.

## Setup and Installation

### Prerequisites

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/) if not already installed.
- **Docker Compose**: Comes bundled with Docker on most platforms.

### Steps

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd careeronestop-video-scraper
   ```

2. **Prepare Input CSV**:

   - Place `career_urls.csv` in the `input/` directory.
   - Ensure it includes columns for `Career` and `URL`, with each row representing a career name and the associated URL.

3. **Build and Run the Docker Container**:
   - Run the following command to build and start the container:
     ```bash
     docker-compose up --build
     ```

## Usage

1. **Start Scraping**:

   - The container will start scraping data from each career URL listed in `career_urls.csv`.
   - A progress bar will indicate the current status of the scraping.

2. **View the Output**:
   - When complete, the data will be saved as `career_data_output.csv` in the `output/` directory.

## Output

The output CSV file (`career_data_output.csv`) will contain the following columns:

| Career         | URL                            | Description                | Video URL                             | Transcript                             |
| -------------- | ------------------------------ | -------------------------- | ------------------------------------- | -------------------------------------- |
| Example Career | https://example.com/career-url | Cleaned career description | https://cdn.example.com/video-url.mp4 | Cleaned transcript text without prefix |

## Duplicate Career Check

To check for duplicate career entries in the output file, run the following code snippet in Python:

```python
import pandas as pd

# Load the output CSV file
output_file = 'output/career_data_output.csv'
career_data = pd.read_csv(output_file)

# Identify duplicate careers
duplicates = career_data[career_data.duplicated(subset="Career", keep=False)]
print("Duplicate Careers:\n", duplicates)
```

This will print any duplicate career entries in the output file.

## Troubleshooting

- **451 Client Errors**: If you encounter HTTP `451` errors, the server might be restricting access to the video resources due to geographic or other restrictions. Video durations are skipped in this project to avoid this issue.
- **Storage Issues**: If you receive "no space left on device" errors during the Docker build, clean up Docker resources using:
  ```bash
  docker system prune -a --volumes
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

```

This `README.md` provides clear guidance on the project’s purpose, setup, and usage, as well as troubleshooting and instructions for checking duplicates. Let me know if you’d like to add anything further!
```
