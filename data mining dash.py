#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 20:13:40 2021

@author: a1
"""

#import different libraries
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

import joblib
from joblib import load


#dash layout
app = dash.Dash(__name__)

app.layout = html.Div(children=
    [
    html.H1('Predict the heart disease!'),
    html.Br(),

    
    html.H4('Age  '),
    dcc.Input(
        id="Age",
        value=0.0,
        
    ),
    html.H4('Sex  '),
    dcc.Input(
        id="Sex",
        value=0.0,
        
    ),
    html.H4('Chest-pain type  '),
    dcc.Input(
        id="Chest-pain type",
        value=0.0,
        
    ),
    html.H4('Resting Blood Pressure  '),
    dcc.Input(
        id="Resting Blood Pressure",
        value=0.0,
        
    ),
    html.H4('Serum Cholesterol  '),
    dcc.Input(
        id="Serum Cholesterol",
        value=0.0,
        
    ),
    html.H4('Resting ECG  '),
    dcc.Input(
        id="Resting ECG",
        value=0.0,
        
    ),
    html.H4('Maximum heart rate achieved   '),
    dcc.Input(
        id="Maximum heart rate achieved ",
        value=0.0,
        
    ),
    html.H4('Exercise induced angina (1 = yes; 0 = no)  '),
    dcc.Input(
        id="Exercise induced angina (1 = yes; 0 = no)",
        value=0.0,
        
    ),
    html.H4('Oldpeak = ST depression induced by exercise relative to rest  '),
    dcc.Input(
        id="Oldpeak = ST depression induced by exercise relative to rest",
        value=0.0,
        
    ),
    html.H4('The slope of the peak exercise ST segment   '),
    dcc.Input(
        id="The slope of the peak exercise ST segment ",
        value=0.0,
        
    ),

    html.H2(id='num'), 
])


#callback
@app.callback(
    Output(component_id="num", component_property="children"),
    Input(component_id="Age", component_property="value"),
    Input(component_id="Sex", component_property="value"),
    Input(component_id="Chest-pain type", component_property="value"),
    Input(component_id="Resting Blood Pressure", component_property="value"),
    Input(component_id="Serum Cholesterol", component_property="value"),
    Input(component_id="Resting ECG", component_property="value"),
    Input(component_id="Maximum heart rate achieved ", component_property="value"),
    Input(component_id="Exercise induced angina (1 = yes; 0 = no)", component_property="value"),
    Input(component_id="Oldpeak = ST depression induced by exercise relative to rest", component_property="value"),
    Input(component_id="The slope of the peak exercise ST segment ", component_property="value"),
)

#outcome prediiction
def update_prediction(X1,X2,X3,X4,X5,X6,X7,X8,X9,X10): #define a function called update_prediction
    input_X = np.array([X1,X2,X3,X4,X5,X6,X7,X8,X9,X10]).reshape(1,-1)  #reshape the array to new array with one row  (https://discuss.codingblocks.com/t/what-is-meaning-of-reshape-1-1/14830)    
    prediction = model.predict(input_X)[0] #make prediction based on input_X
    return "Prediction: {}".format(prediction,1) 

if __name__ == "__main__":
    model=joblib.load(r'/Users/a1/Desktop/SVMmodel_pickle') #The address for pickle file should be changed if necessary
    app.run_server(debug=True)
