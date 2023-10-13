from app import db


class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_time = db.Column(db.DateTime, unique=True)
    temperature = db.Column(db.Float)
    apparent_temperature = db.Column(db.Float)
    cloud_cover = db.Column(db.Float)
    dew_point = db.Column(db.Float)
    dhi = db.Column(db.Float)
    dni = db.Column(db.Float)
    solar_zenith_angle = db.Column(db.Float)
    ghi = db.Column(db.Float)
    pod = db.Column(db.String(1))
    precipitation = db.Column(db.Float)
    pressure = db.Column(db.Float)
    relative_humidity = db.Column(db.Float)
    sea_level_pressure = db.Column(db.Float)
    snow_depth = db.Column(db.Float)
    solar_radiation = db.Column(db.Float)
    visibility = db.Column(db.Float)
    weather_description = db.Column(db.String)
    weather_code = db.Column(db.Float)
    weather_icon = db.Column(db.String)
    wind_direction = db.Column(db.Float)
    wind_gust_speed = db.Column(db.Float)
    wind_speed = db.Column(db.Float)


class ElectricDemand(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_time = db.Column(db.DateTime, unique=True)
    forecast_pool_price = db.Column(db.Float)
    actual_pool_price = db.Column(db.Float)
    forecast_ail = db.Column(db.Float)
    actual_ail = db.Column(db.Float)
    forecast_ail_difference = db.Column(db.Float)
