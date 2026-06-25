from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(tags=["dashboard"])

DASHBOARD_HTML = Path(__file__).resolve().parent.parent / "static" / "dashboard.html"


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    if DASHBOARD_HTML.exists():
        return DASHBOARD_HTML.read_text()
    return "<h1>ISIL Dashboard</h1><p>dashboard.html not found</p>"
