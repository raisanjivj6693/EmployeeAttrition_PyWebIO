from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server

import pickle
import numpy as np
model = pickle.load(open('random_forest_classification_model_top.pkl', 'rb'))
app = Flask(__name__)

def predict():
    Age = input("Enter the Employee Age :", type=NUMBER)
    MonthlyIncome = input("Enter the Employee's Monthly Income :", type=NUMBER)
    YearsAtCompany  = input("Enter the Employee's Years in Company :", type=NUMBER)
    TotalWorkingYears = input("Enter the Employee's Total Working Years :", type=NUMBER)
    NumCompaniesWorked = input("Enter Employee's Numbers of Company Worked :", type=NUMBER)

    overtime = select("Employee having Overtime :", ['Yes', 'No'])
    if(overtime=='Yes'):
        overtime=1
    else:
        overtime=0

    DistanceFromHome = input("Enter the Employee's Home Distance from Office' :", type=NUMBER)

    JobSatisfaction  = select("Employee's Job Satisfaction' :", ['1', '2', '3', '4'])
    if(JobSatisfaction=='1'):
        JobSatisfaction=1
    elif(JobSatisfaction=='2'):
        JobSatisfaction=2
    elif (JobSatisfaction == '3'):
        JobSatisfaction = 3
    else:
        JobSatisfaction = 4

    EnvironmentSatisfaction  = select("Employee's Environment Satisfaction' :", ['1', '2', '3', '4'])
    if (EnvironmentSatisfaction == '1'):
        EnvironmentSatisfaction = 1
    elif (EnvironmentSatisfaction == '2'):
        EnvironmentSatisfaction = 2
    elif (EnvironmentSatisfaction == '3'):
        EnvironmentSatisfaction = 3
    else:
        EnvironmentSatisfaction = 4

    RelationshipSatisfaction  = select("Employee's Relationship Satisfaction' :", ['1', '2', '3', '4'])
    if (RelationshipSatisfaction == '1'):
        RelationshipSatisfaction = 1
    elif (RelationshipSatisfaction == '2'):
        RelationshipSatisfaction = 2
    elif (RelationshipSatisfaction == '3'):
        RelationshipSatisfaction = 3
    else:
        RelationshipSatisfaction = 4

    prediction=model.predict([[ overtime, Age, TotalWorkingYears, MonthlyIncome, JobSatisfaction, YearsAtCompany, EnvironmentSatisfaction, RelationshipSatisfaction, DistanceFromHome, NumCompaniesWorked]])
    print(prediction)

    if prediction != 1:
        put_text("No Attrition - Safe Zone")
    else:
        put_text("Attrition Possible - Danger Zone")

app.add_url_rule('/tool', 'webio_view', webio_view(predict),
            methods=['GET', 'POST', 'OPTIONS'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(predict, port=args.port)

#if __name__ == '__main__':
    #predict()

# app.run(host='localhost', port=80)

#visit http://localhost/tool to open the PyWebIO application.
