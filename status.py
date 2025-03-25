import requests
import argparse

"""
Made by loaymorad
youtube: https://www.youtube.com/@LoayMorad
"""


def status(urls):
    results = {}
    for url in urls:
        url = url.strip()
        if not url.startswith("http"):
            url = "https://" + url
        
        try:
            res = requests.get(url, timeout=5)
            status_code = res.status_code
            result = f"{url} [{status_code}]"
            print(result)
            
            if status_code not in results:
                results[status_code] = []
            results[status_code].append(result)
        except requests.RequestException:
            continue
    
    return results

def main():
    parser = argparse.ArgumentParser(description="Check status codes of URLs from a file.")
    parser.add_argument("-f", "--file", required=True, help="Path to the file containing URLs.")
    parser.add_argument("-o", "--output", required=True, help="Path to save the output file.")
    parser.add_argument("-so", "--status-output", nargs="*", help="List of status codes to save separately.")
    parser.add_argument("-sa", "--status-automatic", help="Filename to automatically group status codes.")
    args = parser.parse_args()
    
    try:
        with open(args.file, "r") as file:
            urls = file.readlines()
    except FileNotFoundError:
        print("Error: File not found.")
        return
    
    results = status(urls)
    
    with open(args.output, "w") as output_file:
        for status_code, result_list in results.items():
            for result in result_list:
                output_file.write(result + "\n")
    
    if args.status_output:
        for status_code in args.status_output:
            filename = f"status_{status_code}.txt"
            if int(status_code) in results:
                with open(filename, "w") as status_file:
                    for result in results[int(status_code)]:
                        status_file.write(result + "\n")
                print(f"Saved {status_code} results to {filename}")
    
    if args.status_automatic:
        grouped_results = {}
        for status_code, result_list in results.items():
            category = f"{status_code // 100}xx"
            if category not in grouped_results:
                grouped_results[category] = []
            grouped_results[category].extend(result_list)
        
        for category, result_list in grouped_results.items():
            filename = f"{args.status_automatic}_{category}.txt"
            with open(filename, "w") as status_file:
                for result in result_list:
                    status_file.write(result + "\n")
            print(f"Saved grouped {category} results to {filename}")
    
    print(f"\nScan completed. Results saved in '{args.output}'.")

if __name__ == "__main__":
    main()
