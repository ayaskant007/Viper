# Viper Search Engine

A lightweight, privacy-focused search engine with a Python backend and modern React frontend. Viper crawls and indexes websites to provide fast, indexed search results with a sleek dark-themed user interface.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.x-green)
![React](https://img.shields.io/badge/React-19.x-61DAFB?logo=react)
![Whoosh](https://img.shields.io/badge/Whoosh-Search-yellow)

## Features

- **Web Crawler** - Automatically crawls and indexes websites
- **Full-Text Search** - Fast indexed search using Whoosh search engine
- **Modern UI** - Responsive dark-themed interface built with React
- **Privacy-Focused** - Local-first search without tracking
- **Fast Performance** - Instant search results with indexed data


## Tech Stack

### Backend
- **FastAPI** - Modern, fast Python web framework
- **Whoosh** - Full-text search library for Python
- **BeautifulSoup4** - HTML parsing and web scraping
- **Requests** - HTTP library for web crawling

### Frontend
- **React 19** - JavaScript library for building user interfaces
- **CSS3** - Modern styling with custom properties and animations
- **HTML5** - Semantic markup

## Installation

### Prerequisites
- Python 3.8 or higher
- Node.js 14 or higher
- npm or yarn

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ayaskant007/Viper.git
   cd Viper
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install fastapi uvicorn whoosh beautifulsoup4 requests
   ```

4. **Run the web crawler** (to index websites)
   ```bash
   python crawlerParser.py
   ```
   This will create an `index_dir` folder containing the indexed search data.

5. **Start the API server**
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to the UI directory**
   ```bash
   cd viper-ui
   ```

2. **Install Node dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm start
   ```
   The UI will open at `http://localhost:3000`

## Usage

### Searching
1. Open the Viper UI in your browser
2. Enter your search query in the search bar
3. Click the "Strike" button or press Enter
4. Results will display instantly

### Crawling New Sites
Edit the `queue` list in `crawlerParser.py` to add websites you want to index:

```python
queue = [
    "https://example.com",
    "https://another-site.com",
    # Add more URLs as needed
]
```

Then run the crawler:
```bash
python crawlerParser.py
```

## API Endpoints

### GET /search
Searches the indexed content.

**Query Parameters:**
- `q` (string, optional) - Search query

**Response:**
```json
[
  {
    "title": "Page Title",
    "url": "https://example.com"
  }
]
```

**Example:**
```
GET http://localhost:8000/search?q=python
```

## Configuration

### Adding Origins (CORS)
Modify the `origins` list in `main.py` to add allowed domains:

```python
origins = [
    "http://localhost:3000",
    "https://yourdomain.com",
]
```

### Search Configuration
Adjust the search index schema in `crawlerParser.py`:

```python
my_schema = Schema(
    url=ID(stored=True, unique=True),
    title=TEXT(stored=True),
    content=TEXT
)
```

## Performance Tips

- **Indexing**: First crawl will take time depending on site sizes. Subsequent updates are faster.
- **Search Results**: Results are returned instantly from the local index.
- **Caching**: Consider enabling response caching for frequently searched queries.

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Android)

## Known Limitations

- Search index is local to the server
- Requires re-crawling to update indexed content
- Some websites may block automated crawling (respect robots.txt)

## Troubleshooting

### Index folder not found
```bash
python crawlerParser.py
```
This will recreate the index directory and re-index websites.

### CORS errors in browser
Ensure the frontend URL is added to the `origins` list in `main.py`.

### Search returns no results
Make sure you've run `crawlerParser.py` to populate the index before searching.

### Port already in use
- FastAPI default: Change with `uvicorn main:app --port 8001`
- React default: Change with `PORT=3001 npm start`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms in the [LICENSE](LICENSE) file.

## Disclaimer

This search engine is designed for educational and personal use. Users are responsible for respecting website terms of service and robots.txt when crawling.
