from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from utils.data_fetcher import fetch_airline_data, process_data

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Default view with all data
    raw_data = await fetch_airline_data()
    processed = process_data(raw_data)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "routes": processed["popular_routes"],
        "demand_chart": processed["demand_chart"],
        "price_chart": processed["price_chart"],
        "top_airlines_chart": processed.get("top_airlines_chart", {}),
        "weekly_chart": processed.get("weekly_chart", {}),
        "monthly_chart": processed.get("monthly_chart", {}),
        "selected_origin": "",
        "selected_dest": "",
    })


@app.post("/", response_class=HTMLResponse)
async def filter_results(
    request: Request,
    origin: str = Form(""),
    destination: str = Form("")
):
    raw_data = await fetch_airline_data(origin=origin, destination=destination)
    processed = process_data(raw_data)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "routes": processed["popular_routes"],
        "demand_chart": processed["demand_chart"],
        "price_chart": processed["price_chart"],
        "top_airlines_chart": processed.get("top_airlines_chart", {}),
        "weekly_chart": processed.get("weekly_chart", {}),
        "monthly_chart": processed.get("monthly_chart", {}),
        "selected_origin": origin,
        "selected_dest": destination,
    })