# IDS721_Class_Project1_FastAPI
[![CI with Github Actions](https://github.com/nansuwang/IDS721_Class_Project1_FastAPI/actions/workflows/main.yml/badge.svg)](https://github.com/nansuwang/IDS721_Class_Project1_FastAPI/actions/workflows/main.yml)

It is a demo project for assignment in IDS721 course.
A containerized prediction service has been built using Fast API

It uses age, years of experience, salary one year ago, and slaray two years age to predict the current salary (in EURO).

It is containerized using Docker! Docker image could be easily built by running
```shell
docker build -t .
```

Main Process:
1. Set up a AWS Cloud9 environment and link it to this Github repo
2. Train a random forest regression model and export the model as pkl file. (training_rf.py)
3. Make the input class using pydantic.BaseModel for doing input in the API. (beer.py)
4. Build API using FastAPI object, defining GET request and POST request. I put the welcome information in GET requests both in main.py and app.py and put predict function in the POST request.
5. Set up AWS App Runner Service linking with Github Repo. If changes are pushed to this repo, click the deploy buttion in the AWS App Runner could trigger the CD process.
6. Could using the default url to reach the content in the GET request in the root directory; could add '/docs' at the end of the url to enter the swagger.
7. I use the CI workflow: (1) Lint with Super-Linter; (2) Check setup (install); (3) Make tests using pytest.
