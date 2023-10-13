import os
import csv
from datetime import datetime
from db import db
from flask import Blueprint
from service.electric_demand import get_electric_demand_data
from utils import get_date_range

cmd = Blueprint("cmd", __name__)


@cmd.cli.command("import_weather_data")
def import_weather_data():
    from models import Weather

    print("Importing data from CSV files to the database...")
    folder_path = os.path.join(os.getcwd(), "data")
    csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    weather_record = Weather.query.filter_by(
                        date_time=datetime.fromisoformat(row["Datetime"])
                    ).first()

                    if weather_record:
                        weather_record.temperature = float(row["Temperature"])
                        weather_record.apparent_temperature = float(
                            row["Apparent Temperature"]
                        )

                        weather_record.cloud_cover = float(row["Cloud Cover"])
                        weather_record.dew_point = float(row["Dew Point"])
                        weather_record.dhi = float(row["DHI"])
                        weather_record.dni = float(row["DNI"])
                        weather_record.solar_zenith_angle = float(
                            row["Solar Zenith Angle"]
                        )
                        weather_record.ghi = float(row["GHI"])
                        weather_record.pod = row["Pod"]
                        weather_record.precipitation = float(row["Precipitation"])
                        weather_record.pressure = float(row["Pressure"])
                        weather_record.relative_humidity = float(
                            row["Relative Humidity"]
                        )
                        weather_record.sea_level_pressure = float(
                            row["Sea Level Pressure"]
                        )
                        weather_record.snow_depth = float(row["Snow Depth"])
                        weather_record.solar_radiation = float(row["Solar Radiation"])
                        weather_record.visibility = float(row["Visibility"])
                        weather_record.weather_description = row["Weather Description"]
                        weather_record.weather_code = float(row["Weather Code"])
                        weather_record.weather_icon = row["Weather Icon"]
                        weather_record.wind_direction = float(row["Wind Direction"])
                        weather_record.wind_gust_speed = float(row["Wind Gust Speed"])
                        weather_record.wind_speed = float(row["Wind Speed"])

                        db.session.commit()
                    else:
                        weather_record = Weather(
                            date_time=datetime.fromisoformat(row["Datetime"]),
                            temperature=float(row["Temperature"]),
                            apparent_temperature=float(row["Apparent Temperature"]),
                            cloud_cover=float(row["Cloud Cover"]),
                            dew_point=float(row["Dew Point"]),
                            dhi=float(row["DHI"]),
                            dni=float(row["DNI"]),
                            solar_zenith_angle=float(row["Solar Zenith Angle"]),
                            ghi=float(row["GHI"]),
                            pod=row["Pod"],
                            precipitation=float(row["Precipitation"]),
                            pressure=float(row["Pressure"]),
                            relative_humidity=float(row["Relative Humidity"]),
                            sea_level_pressure=float(row["Sea Level Pressure"]),
                            snow_depth=float(row["Snow Depth"]),
                            solar_radiation=float(row["Solar Radiation"]),
                            visibility=float(row["Visibility"]),
                            weather_description=row["Weather Description"],
                            weather_code=float(row["Weather Code"]),
                            weather_icon=row["Weather Icon"],
                            wind_direction=float(row["Wind Direction"]),
                            wind_gust_speed=float(row["Wind Gust Speed"]),
                            wind_speed=float(row["Wind Speed"]),
                        )
                        db.session.add(weather_record)
                        db.session.commit()
                except ValueError:
                    print(f"Error while importing data from {csv_file}.")
                    print(row)
                    continue

        print(f"Data from {csv_file} imported successfully to the database.")

    print("All CSV files in the folder have been imported.")


@cmd.cli.command("import_electron_data")
def import_electron_data():
    from models import ElectricDemand

    data_range = get_date_range()
    for range in data_range:
        results = get_electric_demand_data(range["start"], range["end"])
        for index, result in results.iterrows():
            try:
                electric_demand_record = ElectricDemand.query.filter_by(
                    date_time=datetime.fromisoformat(result["Date"])
                ).first()

                if electric_demand_record:
                    electric_demand_record.forecast_pool_price = float(
                        result["Forecast Pool Price"]
                    )
                    electric_demand_record.actual_pool_price = float(
                        result["Actual Posted Pool Price"]
                    )
                    electric_demand_record.forecast_ail = float(result["Forecast AIL"])
                    electric_demand_record.actual_ail = float(result["Actual AIL"])
                    electric_demand_record.forecast_ail_difference = float(
                        result["Forecast AIL & Actual AIL Difference"]
                    )

                    db.session.commit()
                else:
                    electric_demand_record = ElectricDemand(
                        date_time=datetime.fromisoformat(result["Date"]),
                        forecast_pool_price=float(result["Forecast Pool Price"]),
                        actual_pool_price=float(result["Actual Posted Pool Price"]),
                        forecast_ail=float(result["Forecast AIL"]),
                        actual_ail=float(result["Actual AIL"]),
                        forecast_ail_difference=float(
                            result["Forecast AIL & Actual AIL Difference"]
                        ),
                    )
                    db.session.add(electric_demand_record)
                    db.session.commit()
            except ValueError as e:
                print(e)
                print(f"Error while importing data from {range['start']}.")
                print(result)
                continue


@cmd.cli.command("electricity_demand_forecast")
def electricity_demand_forecast():
    from service.forecast import electricity_demand_forecast

    electricity_demand_forecast()
