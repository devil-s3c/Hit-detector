import requests
import argparse
import threading
import queue

results_lock = threading.Lock()
results = queue.Queue()

# ANSI escape codes for text color
RED = "\033[91m"
GREEN = "\033[92m"
ENDC = "\033[0m"

def send_request(url):
    try:
        response = requests.get(url)
        headers = response.headers
        if any("HIT" in value for value in headers.values()):
            status = GREEN + "HIT" + ENDC
            result = url
            print(f"{result} => {status}")  # print progress
            with open("cache-status.txt", "a") as file:
                file.write(result + "\n")  # save "HIT" URLs to file
        elif any("MISS" in value for value in headers.values()):
            status = RED + "MISS" + ENDC
            print(f"{url} => {status}")  # print progress
        else:
            status = "No cache"
        return None
    except Exception as e:
        result = f"Error for {url}: {e}"
        print(result)  # print error message
        return result

def worker():
    while True:
        url = urls.get()
        if url is None:
            break
        result = send_request(url)
        if result:
            results.put(result)
        urls.task_done()

def main():
    parser = argparse.ArgumentParser(description="Cache Checker Tool")
    parser.add_argument("-f", "--file", help="File containing URLs to check")
    parser.add_argument("-t", "--threads", type=int, help="Number of threads to use", default=80)
    parser.add_argument("-e", "--encoding", help="File encoding", default="utf-8")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding=args.encoding, errors="ignore") as file:
            global urls
            urls = queue.Queue()
            for url in file.read().splitlines():
                urls.put(url)
    else:
        parser.error("Please provide a file containing URLs using the -f/--file argument.")
        return

    threads = []
    for _ in range(args.threads):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()

    # Stop worker threads
    for _ in range(args.threads):
        urls.put(None)
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
