# electricity-demand-prediction
Electricity Demand Prediction


## Environment

### Prerequisite

- python 3.11.4
- pipenv

### Install python dependencies

- `brew install pyenv pipenv`
- `pipenv install`

### Flask SQLAlchemy ORM migrations

> Run these two commands only when changes are made to the Flask SQLAlchemy models

```bash
flsak db init

flask db upgrade
```


create a migration script (if changes are made to the Flask SQLAlchemy models)
``` bash
flask db migrate -m "Initial migration."
```
### Cli commands

```bash 
# Import weather data from csv file
flask cmd import_weather_data
```

```bash
# Import electricity demand data
flask cmd import_electron_data
```

```bash
# First, import weather data and electricity demand data
# Electricity demand prediction
flask cmd electricity_demand_forecast
```

### Testing
```bash
python -m unittest
```