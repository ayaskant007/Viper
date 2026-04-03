import React, { useState } from "react";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [hasSearched, setHasSearched] = useState(false);

  const handleSearch = async (e) => {
    if (e) e.preventDefault();
    if (!query.trim()) return; // Don't search if the box is empty

    setHasSearched(true); // Triggers the layout shift animation
    setLoading(true);

    try {
      const response = await fetch(`http://localhost:8000/search?q=${query}`);
      const data = await response.json();
      setResults(data);
    } catch (error) {
      console.error("Viper Error:", error);
    }
    setLoading(false);
  };

  return (
    // The class changes based on whether a search has happened
    <div
      className={`app-wrapper ${hasSearched ? "layout-results" : "layout-home"}`}
    >
      <header className="header">
        <div className="logo-container">
          <h1 className="logo">
            VIPER<span>SEARCH</span>
          </h1>
          <p>Secure by default.</p>
        </div>

        <form className="search-form" onSubmit={handleSearch}>
          <div className="search-input-wrapper">
            {/* SVG Search Icon */}
            <svg
              className="search-icon"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
            >
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>

            <input
              type="text"
              placeholder="Search the indexed web..."
              value={query}
              onChange={(e) => setQuery(e.target.value)}
            />

            {/* Clear Button - Only shows if there is text */}
            {query && (
              <button
                type="button"
                className="clear-btn"
                onClick={() => setQuery("")}
              >
                ✕
              </button>
            )}
          </div>

          <button type="submit" className="strike-btn" disabled={loading}>
            {loading ? <div className="spinner"></div> : "Strike"}
          </button>
        </form>
      </header>

      {hasSearched && (
        <main className="main-content">
          {loading ? (
            /* Modern Skeleton Loading State */
            <div className="skeleton-container">
              {[1, 2, 3].map((n) => (
                <div key={n} className="skeleton-card">
                  <div className="skeleton-header"></div>
                  <div className="skeleton-title"></div>
                  <div className="skeleton-desc"></div>
                </div>
              ))}
            </div>
          ) : results.length > 0 ? (
            /* Actual Results */
            <div className="results-list">
              <p className="results-count">
                Viper found {results.length} results
              </p>
              {results.map((item, index) => (
                <article key={index} className="result-item">
                  <div className="result-header">
                    <div className="favicon">V</div>
                    <cite className="result-url">{item.url}</cite>
                  </div>
                  <a
                    href={item.url}
                    target="_blank"
                    rel="noreferrer"
                    className="result-link"
                  >
                    <h3 className="result-title">{item.title}</h3>
                  </a>
                  <p className="result-snippet">
                    Matches found in the indexed database for this URL.
                  </p>
                </article>
              ))}
            </div>
          ) : (
            /* No Results Found */
            <div className="no-results">
              <h2>No prey found.</h2>
              <p>
                Viper couldn't find any matches for "{query}". Try a broader
                term.
              </p>
            </div>
          )}
        </main>
      )}
    </div>
  );
}

export default App;
