# Cache Checker Tool

Cache Checker Tool is a Python script that allows you to check the cache status of a list of URLs. It sends HTTP requests to the provided URLs and displays whether each URL is a cache HIT, MISS, or not cached at all.

## Features

- Multi-threaded URL checking for efficient processing.
- Supports checking cache status (HIT, MISS, or No cache) for a list of URLs.
- Progress tracking and real-time display of cache status for each URL.
- Saves URLs with cache HIT status to a file for future reference.

## Usage

### Prerequisites

- Python 3.x
- Requests library (install via `pip install requests`)

### Usage Instructions

1. Clone the repository or download the `cache-checker.py` file.
2. Create a text file containing the list of URLs you want to check, for example save the result of the "waybackurl/gau" in a text file and check it  
3. Run the script using the following command:

   ```bash
   python cache-checker.py -f list.txt 

### Options
* -f, --file: Specify the path to the file containing URLs to check.
* -t, --threads: Number of threads to use for parallel processing (default is 80).
* -e, --encoding: File encoding (default is utf-8).
