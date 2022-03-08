<a href="https://imgs.xkcd.com/comics/five_day_forecast.png">
    <img src="https://imgs.xkcd.com/comics/five_day_forecast.png" alt="FTDB" title="FTDB" align="right" height="80" />
</a>


# Forecast/Time series storage API

## TODO

#### Basic functionalities

- [ ] :sparkles: Implement endpoints possibilities similar to the [Forecast API](https://dataplattforms.azurewebsites.net/fApi.html) and to the [Timeseries API](https://dataplattforms.azurewebsites.net/tApi.html)
- [ ] :white_check_mark: Write tests for all endpoints and backend functions (Make Sonarqube shine green!)
- [ ] :recycle:  Refactor the backend to use the core Python/SQL rather than HTTP calls to Azure Functions
- [ ] :bug: Fixing expected problems coming from [CORS](https://fastapi.tiangolo.com/tutorial/cors/)

#### Access Control functionalities
- [ ] :passport_control: Implement [authentication](https://fastapi.tiangolo.com/tutorial/security/#openid-connect)
- [ ] :passport_control: Implement [authorization](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/)

#### CI/CD and API versioning

- [ ] :construction_worker: [Conditional configuration/deployment](https://fastapi.tiangolo.com/advanced/conditional-openapi/) depending on the environment
- [ ] :bookmark: Multiple [API versioning](https://medium.com/geoblinktech/fastapi-with-api-versioning-for-data-applications-2b178b0f843f) akka "How to let your end-users upgrade to the latest version of the API when they want, not just when you come up with a breaking change!"
- [ ] :tada: Build a template REST API configured with Statnett/Azure specific settings for other to use thanks to [Cookiecutter](https://cookiecutter.readthedocs.io)

#### Improve performance

- [ ] :zap: Make calls to backend to run asynchronously with [async](https://fastapi.tiangolo.com/async/)


## Serve the REST API

`uvicorn forecast_timeseries_db_api.api.main:app --reload --port 8888 --host 0.0.0.0`

and open it in your web browser [http://localhost:8888](http://localhost:8888)


## Deployment as web app on Azure (not working yet)

- poetry export -f requirements.txt --output requirements.txt
- follow the [tutorial](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-portal%2Cterminal-bash%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cdeploy-instructions-zip-azcli)
