from models import Weather, ElectricDemand


def electricity_demand_forecast():
    # Get data from database
    weather_data = Weather.query.all()
    electric_demand_data = ElectricDemand.query.all()

    # Data Science Part
    # analysis the data and make prediction
    print("Electricity Demand Forecast")
    return
