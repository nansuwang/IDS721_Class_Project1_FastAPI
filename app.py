import pickle

import uvicorn
from predictors import profile
from fastapi import FastAPI

app = FastAPI()
pickle_in = open("regression_model.pkl", "rb")
classifier = pickle.load(pickle_in)


@app.get("/")
async def read_main():
    return {"msg": "Hello World!"}


@app.get("/{name}")
def get_name(name: str):
    return {"Welcome To Salary Prediction API": f"{name}"}


@app.post("/predict")
def predict_salary(data: profile):
    data = data.dict()
    Age = data["Age"]
    exp = data["exp"]
    Salary_one_year_ago = data["Salary_one_year_ago"]
    Salary_two_years_ago = data["Salary_two_years_ago"]
    prediction = classifier.predict(
        [[Age, exp, Salary_one_year_ago, Salary_two_years_ago]]
    )
    prediction = round(prediction[0], 2)
    return {"The predicted salary (EUR) is ": prediction}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
