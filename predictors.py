from pydantic import BaseModel


class profile(BaseModel):
    Age: float
    exp: float
    Salary_one_year_ago: float
    Salary_two_years_ago: float
