import json

import pandas as pd
import requests


def get_base_url() -> str:
    return "https://erikgetsqlproc.azurewebsites.net/api/erikgetstproc"


def get_headers() -> dict:
    return {
        "Content-Type": "application/json",
    }


def list_datasets(ts_historical: bool = True, ts_forecasts: bool = True) -> pd.DataFrame:
    API_URL = get_base_url()
    payload = {"sqlproc": "Stp_GetmetaDataJson", "paramid": -1}
    response = requests.request(
        "POST", API_URL, data=json.dumps(payload), headers=get_headers(), verify=False
    )
    data = response.json()
    df = pd.json_normalize(data)
    if not ts_historical:
        df = df[df["CurveType"] == "Forecast"]
    if not ts_forecasts:
        df = df[df["CurveType"] == "Timeseries"]
    return df.to_dict(orient="records")


if __name__ == "__main__":
    df_datasets = list_datasets(ts_historical=False)
    # # get_dataset_id_from_names(["DLR.LocationForecast", "Ocean"])

    # df_curves = list_curves_from_dataset(dataset_id=88)
    # list_curves_from_datasets([88, 11])
    # # list_curve_metadata_from_id(curve_id=101056)
    # dct = list_curve_datapoints_from_id(curve_id=127775)
    # print(f"{list(dct.keys())}")
