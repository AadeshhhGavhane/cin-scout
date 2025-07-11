# CIN Scout 🔍

FastAPI-powered CIN lookup for Indian companies. Search, extract ROC codes, founding dates & director details from public registries.

## Features

- Search companies by name with real-time results
- Retrieve detailed company information (ROC codes, founding dates, directors)
- Clean web interface and RESTful API
- Command-line tool for direct CIN lookup

## Installation

### Prerequisites
- Python 3.12 or higher
- `uv` package manager

### Setup

1. **Clone and install**
   ```bash
   git clone https://github.com/AadeshhhGavhane/cin-scout
   cd cin-scout
   uv sync
   ```

2. **Run the application**
   ```bash
   uvicorn server:app --host 0.0.0.0 --port 8000 --reload
   ```

3. **Open the web interface**
   - Navigate to `http://localhost:8000` or open `index.html` directly

## Usage

### Web Interface
1. Type a company name in the search box (minimum 3 characters)
2. Click on search results to view detailed information
3. View legal name, ROC code, founding date, and directors

### API Endpoints

**Search Companies:**
```bash
GET /search?q={company_name}
curl "http://localhost:8000/search?q=tata"
```

**Get Company Details:**
```bash
GET /details?cin={CIN}
curl "http://localhost:8000/details?cin=L28920MH1868PLC000014"
```

### Command Line
```bash
python details.py <CIN>
```

## Project Structure

```
cin-scout/
├── server.py          # FastAPI server
├── details.py         # Company detail extraction
├── index.html         # Web interface
└── pyproject.toml     # Dependencies
```

## Dependencies

- FastAPI - Backend framework
- BeautifulSoup4 - HTML parsing
- Requests - HTTP requests
- Uvicorn - ASGI server

## Data Sources

- Company Search: [InstaFinancials CIN Finder](https://www.instafinancials.com/)
- Company Details: [AllIndiaITR.com](https://www.allindiaitr.com/)

## Disclaimer

This tool is for informational purposes only. Data is sourced from publicly available websites and should be verified independently for official use.