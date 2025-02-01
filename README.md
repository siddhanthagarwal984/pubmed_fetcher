# PubMed Metadata Fetcher

## Overview
The **PubMed Metadata Fetcher** is a Python-based tool designed to retrieve metadata about research papers from the PubMed database. This tool simplifies extracting crucial information such as article titles, publication dates, authors, affiliations, and corresponding author emails. It is particularly beneficial for researchers, students, and professionals seeking structured data for analysis or citation.

## Code Organization:

- **`get_papers_list.py`**: Provides a command-line interface that allows users to specify search queries and manage output options. This script delegates the core fetching and processing tasks to the `pubmed_fetcher.py` module.
- **`pubmed_fetcher.py`**: Contains the primary logic for querying PubMed, processing XML responses, and structuring the extracted data into a Pandas DataFrame for display or storage.
- **Dependencies**: The project utilizes external libraries such as Biopython and Pandas to efficiently handle API communication and data processing.

## Installation
Follow these steps to set up and run the project:

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Set Up a Python Environment**:
   Ensure you are using Python 3.7 or higher. Create a virtual environment to manage dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Install the required Python libraries using `pip`:
   ```bash
   pip install biopython pandas
   ```

   *Dependencies include:*
   - [Biopython](https://biopython.org/): For interacting with PubMed’s Entrez API.
   - [Pandas](https://pandas.pydata.org/): For organizing and exporting data into CSV format.

4. **Run the Script**:
   Execute the program with the following command:
   ```bash
   python get_papers_list.py "<search_query>" [-f <output_filename>] [-d]
   ```

   - Replace `<search_query>` with your desired search term (e.g., "RNA cardiology").
   - Use `-f` to specify a filename for saving results as a CSV file.
   - Use `-d` to enable debug mode for detailed output.

## Features
- Fetch metadata for up to 10 PubMed articles based on a search query.
- Extract structured data, including:
  - Article titles
  - Publication dates
  - Authors
  - Affiliations
  - Corresponding author emails
- Save results to a CSV file or display them in the console.
- Enable debug mode for verbose execution details.

## Tools and Libraries
- **[Biopython](https://biopython.org/)**: Enables seamless interaction with the PubMed API.
- **[Pandas](https://pandas.pydata.org/)**: Organizes data into DataFrames and allows easy export to CSV format.
