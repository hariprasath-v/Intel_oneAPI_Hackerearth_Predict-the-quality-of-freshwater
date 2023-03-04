import requests
import streamlit as st
from shapash import SmartExplainer
from shapash.explainer.smart_predictor import SmartPredictor
from shapash.utils.load_smartpredictor import load_smartpredictor
import pandas as pandas
import numpy as np
import catboost
import dill
from matplotlib import pyplot as plt
import plotly.graph_objects as go
from plotly.graph_objs import *

@st.cache_resource
def loadModel():
  model=requests.get(st.secrets["catboost_shapash_smart_predictor"])
  with open('catboost_shapash_smart_predictor.pkl','wb') as file:
    file.write(model.content)
  model=load_smartpredictor('./catboost_shapash_smart_predictor.pkl')
  return model

class_map={1:"Safe to Drink",0:"Not safe to drink"}


def explanation_plot(prediction_df,val):
  df=prediction_df.drop(['ypred','proba'],axis=1).T.reset_index().rename(columns={'index':'Features',0:'Contribution'}).sort_values(by='Contribution', ascending=True)
  df['Features']=[f"{i}: {j}" for i, j in zip(df['Features'].values,val)]
  df['color']= np.where(df['Contribution']<0, '#f4c000', '#4a628a')
  fig = go.Figure(go.Bar(x=df['Contribution'], y=df['Features'], orientation='h', marker_color=df['color'],
                       text=df['Features'].str.extract('(\w+)'),
                        hovertemplate="Feature: %{text}<br>Contribution: %{x}"+"<extra></extra>") )
  fig.update_layout(template='plotly_white', title={'text':f"Local Explanation<br><sub>Response:<b>\
  {df['ypred'].map(class_map)[0]}</b>\
  Probability:<b>{df['proba'][0].round(5)}</b>\
  </sub>", 'x':0.5,'font_size':24},
  font=dict(color='#191414'),
  xaxis=dict(tickfont=dict(size=18 )),
  yaxis=dict(tickfont=dict(size=15 )))
  fig.show()
  return fig

def page1():
  with st.sidebar:
    st.title("Freshwater Quality Prediction")
    #st.caption("[Project Source](https://github.com/hariprasath-v/Intel_oneAPI_Hackerearth_Predict-the-quality-of-freshwater)")
  with st.form(key='my_form'):
      ph=st.number_input(label="Enter pH Value",min_value=1.057113214784995,max_value=12.910718589310344,step=0.01)
      iron=st.number_input(label="Enter Iron(mscg/dl) Value",min_value=-0.00,max_value=19.35314514968547,step=0.01)
      nitrate=st.number_input(label="Enter Nitrate(ppm) Value",min_value=0.2861727151562775,max_value=96.39077915691342,step=0.01)
      chloride=st.number_input(label="Enter Chloride(mEq/L) Value",min_value=23.63918724615946,max_value=1507.3098813812371,step=0.01)
      lead=st.number_input(label="Enter Lead(µg/dL) Value",min_value=0.0,max_value=5.844281382677685,step=0.01)
      zinc=st.number_input(label="Enter Zinc(µg/mL) Value",min_value=-0.00,max_value=28.368671836331124,step=0.01)
      turbidity=st.number_input(label="Enter Turbidity(NTU) Value",min_value=-0.00,max_value=23.71526964429176,step=0.01)
      fluoride=st.number_input(label="Enter Fluoride(mg/L) Value",min_value=-0.00,max_value=14.64625439721489,step=0.01)
      copper=st.number_input(label="Enter Copper(mg/L) Value",min_value=-0.00,max_value=12.074816454997514,step=0.01)
      odor=st.number_input(label="Enter Odor(ou/m3) Value",min_value=0.0110000703899311,max_value=4.1419978530961,step=0.01)
      sulfate=st.number_input(label="Enter Sulfate(mg/L) Value",min_value=11.940727101003452,max_value=1434.5865433053395,step=0.01)
      conductivity=st.number_input(label="Enter Conductivity(µmhos/cm) Value",min_value=10.599984157611567,max_value=2271.6317219688235,step=0.01)
      chlorine=st.number_input(label="Enter Chlorine(mg/L) Value",min_value=0.9019921000974076,max_value=12.566629947383662,step=0.01)
      manganese=st.number_input(label="Enter Manganese(mg/L) Value",min_value=-0.0,max_value=23.740860018459617,step=0.01)
      total_dissolved_solids=st.number_input(label="Enter Total Dissolved Solids(mg/L) Value",min_value=0.0104890249996087,max_value=579.7999278149582,step=0.01)
      water_temperature=st.number_input(label="Enter Water Temperature(C) Value",min_value=0.6661938382827873,max_value=297.3086294771892,step=0.01)
      air_temperature=st.number_input(label="Enter Air Temperature(C) Value",min_value=-33.870914694640035,max_value=152.12373575647433,step=0.01)
      submitted = st.form_submit_button(label='Submit')
      if submitted:
        predictor = loadModel()
        cols=['pH','Iron','Nitrate','Chloride','Lead','Zinc', 'Turbidity','Fluoride','Copper','Odor',
              'Sulfate','Conductivity', 'Chlorine','Manganese','Total Dissolved Solids',
              'Water Temperature','Air Temperature']
        val=[ph,iron,nitrate,chloride,lead,zinc,turbidity,
                                            fluoride,copper,odor,sulfate,conductivity,
                                            chlorine,
                                            manganese,total_dissolved_solids,
                                            water_temperature,air_temperature]
        predictor.add_input({i:j for i,j in zip(cols,val)})
        predictor_df=predictor.detail_contributions()
        if predictor_df['ypred'][0]==1:
          st.markdown("**:green[Safe to Drink]**")
        elif predictor_df['ypred'][0]==0:
          st.markdown("**:red[Not Safe to Drink]**")
        with st.expander("View Explanation"):
          tab1, tab2 = st.tabs(['Local Explanation Plot', 'Data'])
          with tab1:
            st.plotly_chart(explanation_plot(predictor_df,val),sharing ='streamlit',use_container_width=True)
          with tab2:
            predictor_df['ypred']=predictor_df['ypred'].map(class_map)
            st.download_button(
                    label="Download Annotation Data as CSV",
                    data=predictor_df.to_csv(),
                    file_name=f"Freshwater Qualtiy Prediction Contribution For {predictor_df['ypred']}.csv",
                    mime='text/csv')


if __name__ == '__main__':
  loadModel()
  page1()


          

