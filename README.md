# Intel_oneAPI_Hackerearth_Predict-the-quality-of-freshwater

### Competition hosted on <a href="https://www.hackerearth.com/challenges/hackathon/intel-oneapi-hackathon-for-open-innovation/">Hackerearth</a>

### Problem

Freshwater is one of our most vital and scarce natural resources, making up just 3% of the earth’s total water volume. It touches nearly every aspect of our daily lives, from drinking, swimming, and bathing to generating food, electricity, and the products we use every day. Access to a safe and sanitary water supply is essential not only to human life, but also to the survival of surrounding ecosystems that are experiencing the effects of droughts, pollution, and rising temperatures.

### Expected Solution:

In this track of the hackathon, you will have the opportunity to apply the oneAPI skills to help global water security and environmental sustainability efforts by predicting whether freshwater is safe to drink and use for the ecosystems that rely on it.

### Dataset

You can download the dataset <a href="https://s3-ap-southeast-1.amazonaws.com/he-public-data/datasetab75fb3.zip">here</a>    

### Mandate 

Usage of Intel® oneAPI AI Analtyics toolkits is mandatory to participate.

### Solution:

### Exploratory Data Analysis
#### The basic exploratory data analysis of the data,
* Missing value analysis
* Numerical column distribtution analysis
* Interaction between categorical and numerical columns
#### The above analysis had done by using,
* modin(intel) pandas  
* numpy
* seaborn
* matplotlib
* missingno
* klib
     
### Data pre-processing
The missing values are imputed by two method.
#### Mean value imputated for following columns,
* Odor
* Total Dissolved Solids
#### Median value imputated for following columns,
* pH
* Iron
* Nitrate
* Chloride
* Lead
* Zinc
* Turbidity
* Fluoride
* Copper
* Odor
* Sulfate
* Conductivity
* Water Temperature
* Air Temperature

#### Color and Source features don't have any interaction with other numerical measures.
#### Month, Day, Time of day these features don't have any relevant information for determining the quality of freshwater.

### Model
#### Created stratified train and test dataset from the entire dataset.
#### Xgboost, lightgbm, catboost models are trained and evaluated with F1 score.
#### For faster inference models are converted to oneDAL model. 
#### F1 score comparison
![Alt text](https://github.com/hariprasath-v/Intel_oneAPI_Hackerearth_Predict-the-quality-of-freshwater/blob/main/Model%20Interpretation/F1%20Score%20Comparison.png)
![Alt text](https://github.com/hariprasath-v/Intel_oneAPI_Hackerearth_Predict-the-quality-of-freshwater/blob/main/Model%20Interpretation/F1%20score%20comparison%20dataframe.PNG)

#### Model explained with shapash library

#### Lightgbm model Feature Importances
![Alt text](https://github.com/hariprasath-v/Intel_oneAPI_Hackerearth_Predict-the-quality-of-freshwater/blob/main/Model%20Interpretation/lightgbm%20model%20shapash%20feature%20importances.png)

#### Lightgbm model Local explantion for class 1(safe to drink)
![Alt text](https://github.com/hariprasath-v/Intel_oneAPI_Hackerearth_Predict-the-quality-of-freshwater/blob/main/Model%20Interpretation/lightgbm%20model%20Local%20explantion%20for%20class%201(safe%20to%20drink).png)

#### Catboost model Feature Importances
![Alt text](https://github.com/hariprasath-v/Intel_oneAPI_Hackerearth_Predict-the-quality-of-freshwater/blob/main/Model%20Interpretation/catboost%20model%20shapash%20feature%20importances.png)

#### Catboost model Local explantion for class 1(safe to drink)
![Alt text](https://github.com/hariprasath-v/Intel_oneAPI_Hackerearth_Predict-the-quality-of-freshwater/blob/main/Model%20Interpretation/catboost%20model%20Local%20explantion%20for%20class%201(safe%20to%20drink).png)

### Model demo
#### For model demo catboost model is used.The demo app created by using the streamlit.
#### Manual input fields for the columns
#### Local explanation using shapash smart predictor
<a href="https://freshwater-quality.streamlit.app">Model Demo App</a>  
 



### File information

 av-job-a-thon-november-2022-model.ipynb [![Open in Kaggle](https://img.shields.io/static/v1?label=&message=Open%20in%20Kaggle&labelColor=grey&color=blue&logo=kaggle)](https://www.kaggle.com/hari141v/av-job-a-thon-november-2022-model)
 
   
        
