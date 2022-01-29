# IDS721_Class_Project1_FastAPI
[![CI with Github Actions](https://github.com/nansuwang/IDS721_Class_Project1_FastAPI/actions/workflows/main.yml/badge.svg)](https://github.com/nansuwang/IDS721_Class_Project1_FastAPI/actions/workflows/main.yml)

It is a demo project for assignment in IDS721 course.
A containerized prediction service has been built using Fast API

It uses age, years of experience, salary one year ago, and slaray two years age to predict the current salary (in EURO).

It is containerized using Docker! Docker image could be easily built by running
```shell
docker build -t .
```

The dataset is from Kaggle. https://www.kaggle.com/parulpandey/2020-it-salary-survey-for-eu-region?select=IT+Salary+Survey+EU+2018.csv
