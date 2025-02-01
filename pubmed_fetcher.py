import argparse
import pandas as pd
from Bio import Entrez
import re

# Set the email address to avoid any potential issues with Entrez
Entrez.email = 'siddhanthagarwal984@gmail.com'


def fetch_papers(query, debug=False, output_file=None):
    """
    Fetch papers from PubMed based on a query and save the data to a CSV file or print to console.

    Parameters:
    - query (str): Search query for PubMed.
    - debug (bool): Enables debug mode for verbose output.
    - output_file (str): Filename to save the CSV output; prints to console if None.

    Returns:
    - None
    """

    # Search for papers in PubMed using the query
    handle = Entrez.esearch(db='pubmed', retmax=10, term=query)
    record = Entrez.read(handle)
    id_list = record['IdList']
    #######
    # Initialize a DataFrame to store the extracted data
    df = pd.DataFrame(columns=['PubmedID', 'Title', 'Publication Date', 'Non-academic Author(s)', 'Company Affiliation(s)', 'Corresponding Author Email'])

    for pmid in id_list:
        handle = Entrez.efetch(db='pubmed', id=pmid, retmode='xml')
        records = Entrez.read(handle)

        for record in records['PubmedArticle']:
            title = record['MedlineCitation']['Article']['ArticleTitle']
            
            # Extract publication date with safety checks
            publication_date = record['MedlineCitation']['Article']['Journal']['JournalIssue'].get('PubDate', {})
            year = publication_date.get('Year', 'No year')
            month = publication_date.get('Month', 'No month')
            day = publication_date.get('Day', 'No day')
            
            if 'No month' in month and 'No day' in day:
                publication_date = f"{year}"
            elif 'No month' in month:
                publication_date = f"{year}-{month}"
            else:
                publication_date = f"{year}-{month}-{day}"

            # Extract authors
            authors = ', '.join(author.get('LastName', '') + ' ' + author.get('ForeName', '') for author in record['MedlineCitation']['Article']['AuthorList'])
            
            # Extract affiliations and search for emails
            affiliations = []
            emails = []
            for author in record['MedlineCitation']['Article']['AuthorList']:
                if 'AffiliationInfo' in author and author['AffiliationInfo']:
                    for affiliation in author['AffiliationInfo']:
                        aff_text = affiliation['Affiliation']
                        
                        # Search for email pattern in the affiliation text
                        email_matches = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', aff_text)
                        emails.extend(email_matches)
                        
                        # Remove emails from affiliation text
                        cleaned_affiliation = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '', aff_text).strip()
                        if cleaned_affiliation:  # Add non-empty cleaned affiliations
                            affiliations.append(cleaned_affiliation)
            
            affiliations = '; '.join(set(affiliations)) if affiliations else "No affiliations"
            corresponding_email = ', '.join(emails) if emails else "No email available"
            
            # Add to DataFrame
            new_row = pd.DataFrame({
                'PubmedID': [pmid],
                'Title': [title],
                'Publication Date': [publication_date],
                'Non-academic Author(s)': [authors],
                'Company Affiliation(s)': [affiliations],
                'Corresponding Author Email': [corresponding_email]
            })

            df = pd.concat([df, new_row], ignore_index=True)

    if output_file:
        df.to_csv(output_file, index=False)
    else:
        print(df)






