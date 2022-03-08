from enum import Enum
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, constr

from forecast_timeseries_db_api.api import backend

description = """
The Forecast/Timeseries DB (FTDB) will help you store and read time series and forecast data.

## Curve Data

Curve data are the datapoints of a time series.
They are made of a single observation for a specific timestamp.

## Curve

A Curve defines the metadata of a time series associated to a series of Curve data.
(ex: time series for temperature, optionally attached to a specific location, a geopoint.)

## Loadset

Loadset are a logical grouping of curves.
(ex: Weather data from MET.no which can include
different curves about temperature, humidity, wind, ...)

## Geopoint

a Geopoint defines the coordinates of a location (latitute, longitude, altitude).

## Geopoint group

A Geopoint group is a logical way to group a list of Geopoints.
(ex.: All geopoints for a given family of sensors.)

"""

app = FastAPI(
    title="FTDB",
    description=description,
    version="0.0.1",
    terms_of_service="https://slangapp.com/legal/terms",
    contact={
        "name": "Santanett",
        "url": "https://www.freeconferencecall.com/global/no/santa-hotline",
        "email": "3020@santanett.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


class TypeTS(Enum):
    HISTORICAL = "historical"
    FORECAST = "forecast"


class Frequency(str, Enum):
    minute = "m"
    hour = "H"
    day = "D"
    week = "W"
    month = "M"
    quarter = "Q"
    year = "A"


class Loadset(BaseModel):
    id: int
    name: str
    description: Optional[str]
    freq: constr(regex=r"^([a-zA-Z]+)([1-9]*)$", min_length=1)
    unit: str

    class Config:
        schema_extra = {
            "example": {
                "id": 78,
                "name": "DLR.LocationForecast",
                "description": "Bjerkreim-Stokkeland 111-112.Temp.C.10m.F",
                "freq": "H",
                "unit": "Celcius",
            }
        }


@app.get("/")
def read_root():
    return RedirectResponse("/docs")


@app.post("/loadsets/", response_model=Loadset, summary="Create a loadset")
async def save_loadset(loadset: Loadset):
    """
    Create a loadset with all the information:

    - **name**: each loadset must have a name
    - **id**: each loadset must have an id (hidden in the futur!)
    - **description**: a long description (optional)
    - **freq**: frequency of the time series, required (ex.: m, m5, H, D, W, M)
    - **unit**: the unit of the time series (ex.: Celcius, %, on/off, ...)
    \f
    :param loadset: User input.
    :return:
    """
    # do something in the database
    return loadset


@app.get("/loadsets")
def read_loadsets(type_timeseries: Optional[str] = None):
    values = [item.value for item in TypeTS]
    if type_timeseries is None or type_timeseries in values:
        pass
    else:
        raise HTTPException(
            status_code=404,
            detail=f"if using the query parameter 'timeseries_type', "
            f"it should be one of '{', '.join(values)}'",
        )

    enable_timeseries = enable_forecasts = True
    if type_timeseries == TypeTS.FORECAST.value:
        enable_timeseries = False
    elif type_timeseries == TypeTS.HISTORICAL.value:
        enable_forecasts = False
    return backend.list_datasets(ts_historical=enable_timeseries, ts_forecasts=enable_forecasts)
