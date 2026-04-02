from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser


value=input("Enter your desired search query: ")
ix = open_dir("index_dir")

with ix.searcher() as searcher:
    query = MultifieldParser(["title", "content"], ix.schema).parse(value)
    results = searcher.search(query, limit=None)

    if len(results) == 0:
        print("No matches found. Viper missed the target!")

    else:
        print(f"Found {len(results)} results: ")

        for hit in results:
            print(f"Title: {hit['title']}")
            print(f"URL: {hit['url']}")
            print("-" * 20)