from fastapi import FastAPI
from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ix = open_dir("index_dir")

value= "Google"

@app.get("/search")
def search(q: str = None):  # Adding 'q' makes it dynamic!
    if q:
        with ix.searcher() as searcher:
            query = MultifieldParser(["title", "content"], ix.schema).parse(q)
            results = searcher.search(query, limit=None)
            
            # Convert results to a list inside the 'with' block
            return [{"title": r["title"], "url": r["url"]} for r in results]
    return {"error": "No query provided"}



# value=input("Enter your desired search query: ")

# with ix.searcher() as searcher:
#     query = MultifieldParser(["title", "content"], ix.schema).parse(value)
#     results = searcher.search(query, limit=None)

#     if len(results) == 0:
#         print("No matches found. Viper missed the target!")

#     else:
#         print(f"Found {len(results)} results: ")

#         for hit in results:
#             print(f"Title: {hit['title']}")
#             print(f"URL: {hit['url']}")
#             print("-" * 20)