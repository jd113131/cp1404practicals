import wikipedia

def main():
    """Simple menu function to interact with wikipedia"""
    query = input("Enter page query: ")
    while query != "":
        try:
            search = wikipedia.page(query, auto_suggest=False)
        except wikipedia.exceptions.DisambiguationError:
            print(f"We need a more specific query. Try one of the following, or a new search:")
            print(wikipedia.search(query))
            pass
        except wikipedia.exceptions.PageError:
            print(f"Page id {query} does not match any pages. Try another id!")
        else:
            print(search.title)
            print(search.summary)
            print(search.url)
        query = input("Enter page query: ")
    
    print("Thank you.")


main()