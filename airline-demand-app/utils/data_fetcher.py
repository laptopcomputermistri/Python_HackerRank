import httpx
import pandas as pd
import datetime

API_KEY = "0036e9922b85004ceffb3e9409cb7abb"

async def fetch_airline_data(origin="", destination=""):
    # AviationStack endpoint for flight data
    url = "http://api.aviationstack.com/v1/flights"
    params = {
        "access_key": API_KEY,
        "dep_iata": origin or None,  # IATA code for origin (e.g., SYD)
        "arr_iata": destination or None,  # IATA code for destination (e.g., MEL)
        "flight_status": "scheduled",
        "limit": 100  # You can change this as needed
    }
    # Remove None values to avoid API errors
    params = {k: v for k, v in params.items() if v is not None}

    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
        data = resp.json().get("data", [])

    # Parse and structure data
    flights = []
    for flight in data:
        try:
            flights.append({
                "origin": flight["departure"].get("iata", "N/A"),
                "destination": flight["arrival"].get("iata", "N/A"),
                "date": flight["departure"].get("scheduled", "")[:10],  # YYYY-MM-DD
                "airline": flight["airline"].get("name", "N/A"),
                "flight_number": flight.get("flight", {}).get("number", "N/A"),
                "price": None,  # Pricing data not available from AviationStack free tier
                "demand": 1  # Each entry is one scheduled flight
            })
        except Exception:
            continue

    return flights

def process_data(data):
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])

    # Fill missing columns for compatibility
    if "price" not in df.columns:
        df["price"] = 0

    # --- Weekly Aggregation ---
    weekly = df.resample('W-MON', on='date').agg({'demand': 'sum', 'price': 'mean'}).reset_index()
    weekly_chart = {
        "x": weekly['date'].dt.strftime('%Y-%m-%d').tolist(),
        "y": weekly['demand'].fillna(0).astype(int).tolist(),
    }

    # --- Monthly Aggregation ---
    monthly = df.resample('M', on='date').agg({'demand': 'sum', 'price': 'mean'}).reset_index()
    monthly_chart = {
        "x": monthly['date'].dt.strftime('%Y-%m').tolist(),
        "y": monthly['demand'].fillna(0).astype(int).tolist(),
    }

    # Popular Routes
    route_counts = df.groupby(["origin", "destination"]).size().reset_index(name="count")
    popular_routes = route_counts.sort_values("count", ascending=False).head(5).to_dict("records")

    # Demand Trend
    demand_trend = df.groupby("date")["demand"].sum().reset_index()
    demand_chart = {
        "x": demand_trend["date"].astype(str).tolist(),
        "y": demand_trend["demand"].tolist()
    }

    # Price Trend (for this API, all prices may be 0)
    price_chart = {
        "x": df["date"].astype(str).tolist(),
        "y": df["price"].tolist()
    }

    # Top Airlines
    if "airline" in df.columns:
        top_airlines = (
            df.groupby("airline")
            .size()
            .reset_index(name="count")
            .sort_values("count", ascending=False)
            .head(5)
        )
        top_airlines_chart = {
            "x": top_airlines["airline"].tolist(),
            "y": top_airlines["count"].tolist()
        }
    else:
        top_airlines_chart = {"x": [], "y": []}

    return {
        "popular_routes": popular_routes,
        "demand_chart": demand_chart,
        "price_chart": price_chart,
        "top_airlines_chart": top_airlines_chart,
        "weekly_chart": weekly_chart,
        "monthly_chart": monthly_chart,
    }