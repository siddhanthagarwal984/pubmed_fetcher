import argparse
from pubmed_fetcher import fetch_papers

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Fetch PubMed papers based on a query and save them to a CSV file or print to the console."
    )
    
    # Adding command-line arguments
    parser.add_argument(
        "query", 
        help="The search query to find papers in PubMed (e.g., 'RNA cardiology')."
    )
    
    parser.add_argument(
        "-d", "--debug", 
        action="store_true", 
        help="Enable debug output to print additional details during execution."
    )
    
    parser.add_argument(
        "-f", "--file", 
        help="Specify the filename to save the results as a CSV file. If not provided, the results are printed to the console."
    )

    # Parse the arguments
    args = parser.parse_args()
    
    # Call the fetch_papers function from the pubmed_fetcher module
    fetch_papers(args.query, debug=args.debug, output_file=args.file)

if __name__ == '__main__':
    main()