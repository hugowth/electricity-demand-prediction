import io
import requests
import pandas as pd
from utils import convert_date

URL = "http://ets.aeso.ca/ets_web/ip/Market/Reports/ActualForecastWMRQHReportServlet"


def get_electric_demand_data(start, end):
    params = {"beginDate": start, "endDate": end, "contentType": "csv"}
    response = requests.get(URL, params=params)

    if response.status_code == 200:
        csv_data = response.text

        df = pd.read_csv(io.StringIO(csv_data), skiprows=6)

        df.columns = [
            "Date",
            "Forecast Pool Price",
            "Actual Posted Pool Price",
            "Forecast AIL",
            "Actual AIL",
            "Forecast AIL & Actual AIL Difference",
        ]

        df["Date"] = df["Date"].str.replace("*", "").apply(convert_date)
        df["Forecast AIL"] = df["Forecast AIL"].str.replace(",", "")
        df["Actual AIL"] = df["Actual AIL"].str.replace(",", "")

        return df
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
