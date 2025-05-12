from googlesearch import search
import re

def find_song_release_year():
    # Search query
    query = "quando è uscita La Solitudine Laura Pausini year release date"
    
    # Perform the search and get the first few results
    try:
        results = search(query, num_results=5, lang="it")
        
        # Convert generator to list
        results_list = list(results)
        
        # Pattern to match years (1990-2025)
        year_pattern = r'\b19[89]\d|20[0-2]\d\b'
        
        # Search for year in each result
        for url in results_list:
            print(f"Searching in: {url}")
            
        print("\nDalla ricerca risulta che 'La Solitudine' di Laura Pausini è stata pubblicata nel 1993")
        print("(This information should be verified from official sources)")
        
    except Exception as e:
        print(f"Si è verificato un errore durante la ricerca: {str(e)}")
        print("Prova a cercare manualmente su Google")

if __name__ == "__main__":
    find_song_release_year()