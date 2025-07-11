from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import json

# Import our detail extraction functions
from details import extract_company_url, extract_company_details

app = FastAPI()

# Allow frontend to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search_company(q: str = Query(..., min_length=2)):
    session = requests.Session()

    # Step 1: Visit the finder page to receive a fresh session cookie
    try:
        session.get("https://projects.instafinancials.com/cin-finder/cin-finder-by-name.aspx", headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to initialize session: {e}")

    # Step 2: Prepare headers and payload for POST
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.8',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://projects.instafinancials.com',
        'referer': 'https://projects.instafinancials.com/cin-finder/cin-finder-by-name.aspx',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }

    body = json.dumps({"strSearch": q, "mode": "SCBN"})

    try:
        response = session.post(
            "https://projects.instafinancials.com/ajax-caller.aspx/GetCompanyNames",
            headers=headers,
            data=body
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch search results: {e}")

@app.get("/details")
def get_company_details(cin: str = Query(..., min_length=1)):
    url = extract_company_url(cin)
    if not url:
        raise HTTPException(status_code=404, detail=f"Company with CIN {cin} not found")

    try:
        details = extract_company_details(url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return details

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)