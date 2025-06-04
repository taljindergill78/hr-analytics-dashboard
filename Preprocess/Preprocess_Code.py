import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype

def clean(df: pd.DataFrame) -> pd.DataFrame:
    # Attrition: Convert 'Yes'/'No' to '1'/'0'
    df['Attrition'] = df['Attrition'].map({'Yes': '1', 'No': '0'}).fillna('0')

    # BusinessTravel: Clean and specific fix TravelRarely -> Travel_Rarely
    df['BusinessTravel'] = df['BusinessTravel'].astype(str).str.strip()
    df['BusinessTravel'] = df['BusinessTravel'].replace('TravelRarely', 'Travel_Rarely')

    # OverTime: Convert 'Yes'/'No' to '1'/'0'
    df['OverTime'] = df['OverTime'].map({'Yes': '1', 'No': '0'}).fillna('0')

    # Education_Updated
    edu_map = {
        1: 'Very Less Educated',
        2: 'Less Educated',
        3: 'Moderately Educated',
        4: 'Highly Educated',
        5: 'Very Highly Educated'
    }
    df['Education_Updated'] = df['Education'].map(edu_map)

    # EnvironmentSatisfaction_Updated
    env_map = {
        1: 'Low',
        2: 'Medium',
        3: 'High',
        4: 'Very High'
    }
    df['EnvironmentSatisfaction_Updated'] = df['EnvironmentSatisfaction'].map(env_map)

    # JobInvolvement_Updated
    job_inv_map = {
        1: 'Low',
        2: 'Medium',
        3: 'High',
        4: 'Very High'
    }
    df['JobInvolvement_Updated'] = df['JobInvolvement'].map(job_inv_map)

    # JobLevel_Updated
    job_level_map = {
        1: 'Very Low',
        2: 'Low',
        3: 'Medium',
        4: 'High',
        5: 'Very High'
    }
    df['JobLevel_Updated'] = df['JobLevel'].map(job_level_map)

    # JobSatisfaction_Updated
    job_sat_map = {
        1: 'Low',
        2: 'Medium',
        3: 'High',
        4: 'Very High'
    }
    df['JobSatisfaction_Updated'] = df['JobSatisfaction'].map(job_sat_map)

    # RelationshipSatisfaction_Updated
    rel_sat_map = {
        1: 'Low',
        2: 'Medium',
        3: 'High',
        4: 'Very High'
    }
    df['RelationshipSatisfaction_Updated'] = df['RelationshipSatisfaction'].map(rel_sat_map)

    # WorkLifeBalance_Updated
    worklife_map = {
        1: 'Low',
        2: 'Medium',
        3: 'High',
        4: 'Very High'
    }
    df['WorkLifeBalance_Updated'] = df['WorkLifeBalance'].map(worklife_map)

    # YearsWithCurrManager: Fill missing with median
    median_years_with_mgr = df['YearsWithCurrManager'].median()
    df['YearsWithCurrManager'] = df['YearsWithCurrManager'].fillna(median_years_with_mgr)

    return df

def getOutputSchema():
    return pd.DataFrame({
        'EmpID': pd.Series(dtype='str'),
        'Age': pd.Series(dtype='int'),
        'AgeGroup': pd.Series(dtype='str'),
        'Attrition': pd.Series(dtype='str'),
        'BusinessTravel': pd.Series(dtype='str'),
        'DailyRate': pd.Series(dtype='int'),
        'Department': pd.Series(dtype='str'),
        'DistanceFromHome': pd.Series(dtype='int'),
        'Education': pd.Series(dtype='int'),
        'Education_Updated': pd.Series(dtype='str'),
        'EducationField': pd.Series(dtype='str'),
        'EmployeeCount': pd.Series(dtype='int'),
        'EmployeeNumber': pd.Series(dtype='int'),
        'EnvironmentSatisfaction': pd.Series(dtype='int'),
        'EnvironmentSatisfaction_Updated': pd.Series(dtype='str'),
        'Gender': pd.Series(dtype='str'),
        'HourlyRate': pd.Series(dtype='int'),
        'JobInvolvement': pd.Series(dtype='int'),
        'JobInvolvement_Updated': pd.Series(dtype='str'),
        'JobLevel': pd.Series(dtype='int'),
        'JobLevel_Updated': pd.Series(dtype='str'),
        'JobRole': pd.Series(dtype='str'),
        'JobSatisfaction': pd.Series(dtype='int'),
        'JobSatisfaction_Updated': pd.Series(dtype='str'),
        'MaritalStatus': pd.Series(dtype='str'),
        'MonthlyIncome': pd.Series(dtype='int'),
        'SalarySlab': pd.Series(dtype='str'),
        'MonthlyRate': pd.Series(dtype='int'),
        'NumCompaniesWorked': pd.Series(dtype='int'),
        'Over18': pd.Series(dtype='str'),
        'OverTime': pd.Series(dtype='str'),
        'PercentSalaryHike': pd.Series(dtype='int'),
        'PerformanceRating': pd.Series(dtype='int'),
        'RelationshipSatisfaction': pd.Series(dtype='int'),
        'RelationshipSatisfaction_Updated': pd.Series(dtype='str'),
        'StandardHours': pd.Series(dtype='int'),
        'StockOptionLevel': pd.Series(dtype='int'),
        'TotalWorkingYears': pd.Series(dtype='int'),
        'TrainingTimesLastYear': pd.Series(dtype='int'),
        'WorkLifeBalance': pd.Series(dtype='int'),
        'WorkLifeBalance_Updated': pd.Series(dtype='str'),
        'YearsAtCompany': pd.Series(dtype='int'),
        'YearsInCurrentRole': pd.Series(dtype='int'),
        'YearsSinceLastPromotion': pd.Series(dtype='int'),
        'YearsWithCurrManager': pd.Series(dtype='float')
    })
