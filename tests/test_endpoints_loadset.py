from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/loadset")
async def get_list_loadset():
    return [
        {
            "LoadSetId": 96,
            "Loadset": "Alfred",
            "Freq": "M",
            "CurveType": "Timeseries",
            "CurveLink": "<a href=my_relative_url> ListCurves <a>",
            "Map": "",
            "GeoPts": "",
            "Loader": "",
            "Mapp": "",
            "SourceDoc": "",
            "PlattformOwner": "PlatformAPI",
            "BusinessOwner": "",
            "Azuretool": "Python Function",
            "DirectUse": "",
            "InternalDoc": "",
        },
        {
            "LoadSetId": 13,
            "Loadset": "BI-Cycle",
            "Freq": "H",
            "CurveType": "Timeseries",
            "CurveLink": "<a href=my_relative_url> ListCurves <a>",
            "Map": "",
            "GeoPts": "",
            "Loader": "",
            "Mapp": "",
            "SourceDoc": "<a href=source_url<a>",
            "PlattformOwner": "<a href=url_profile_author>Author name<a>",
            "BusinessOwner": "",
            "Azuretool": "LogicApp",
            "DirectUse": "",
            "InternalDoc": "",
        },
    ]


@app.get("/loadset?type_timeseries=foo_bar")
async def get_list_loadset_unknown_filter():
    raise HTTPException(
        status_code=404,
        detail="if using the query parameter 'timeseries_type', "
        "it should be one of 'historical, forecast'",
    )


@app.get("/loadset?type_timeseries=forecast")
async def get_list_loadset_filter_on_forecast():
    return [
        {
            "LoadSetId": 78,
            "Loadset": "DLR.LocationForecast",
            "Freq": "H",
            "CurveType": "Forecast",
            "CurveLink": "<a href=relative_url> ListCurves <a>",
            "Map": "<a href=relative_url> <img src=image_url.png >  <a>",
            "GeoPts": "<a href=relative_url>  <img src=image_url width=16 height=16 > <a>",
            "Loader": "<a href=relative_url> <img src=image_url width=16 height=16 > <a>",
            "Mapp": "",
            "SourceDoc": "<a href=source_url> Met LocalForecast API<a>",
            "PlattformOwner": "<a href=profile_url>author name<a>",
            "BusinessOwner": "<a href=profle_url>author name<a>",
            "Azuretool": "Python Function",
            "DirectUse": "<a href=relative_url> fd=vd <a>",
            "InternalDoc": "<a href=Naming.html> Naming<a>",
        },
        {
            "LoadSetId": 84,
            "Loadset": "DLR.MEPS.ENS",
            "Freq": "H",
            "CurveType": "Forecast",
            "CurveLink": "<a href=relative_url> ListCurves <a>",
            "Map": "<a href=GeoMap.php?loadsetid=84> <img src=image_url >  <a>",
            "GeoPts": "<a href=relative_url>  <img src=image_url width=16 height=16 > <a>",
            "Loader": "<a href=relative_url> <img src=image_url width=16 height=16 > <a>",
            "Mapp": "",
            "SourceDoc": "",
            "PlattformOwner": "<a href=profile_url>author name<a>",
            "BusinessOwner": "",
            "Azuretool": "Python Function",
            "DirectUse": "",
            "InternalDoc": "",
        },
    ]


client = TestClient(app)


def test_read_all_loadset():
    response = client.get("/loadset")
    assert response.status_code == 200
    resp = response.json()
    assert set(resp[0].keys()) == {
        "GeoPts",
        "BusinessOwner",
        "InternalDoc",
        "Loadset",
        "Map",
        "PlattformOwner",
        "DirectUse",
        "Loader",
        "LoadSetId",
        "SourceDoc",
        "CurveLink",
        "Mapp",
        "Azuretool",
        "CurveType",
        "Freq",
    }


def test_read_loadset_with_filter_forecast():
    response = client.get("/loadset?type_timeseries=forecast")
    assert response.status_code == 200
    resp = response.json()
    assert set(resp[0].keys()) == {
        "GeoPts",
        "BusinessOwner",
        "InternalDoc",
        "Loadset",
        "Map",
        "PlattformOwner",
        "DirectUse",
        "Loader",
        "LoadSetId",
        "SourceDoc",
        "CurveLink",
        "Mapp",
        "Azuretool",
        "CurveType",
        "Freq",
    }


def test_read_loadset_with_filter_unknown():
    response = client.get("/loadset?type_timeseries=foo_bar")
    assert response.status_code == 404
    resp = response.json()
    assert resp == {
        "detail": "if using the query parameter 'timeseries_type', "
        "it should be one of 'historical, forecast'"
    }
