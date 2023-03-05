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
#### Created startified train and test dataset from the entire dataset.
#### Xgboost, lightgbm, catboost trained and evaluated with F1 score.
#### For faster inference models are converted to oneDAL model. 
#### F1 score comparison
#### Model explained with shapash library
#### Lightgbm model Feature Importances
#### Lightgbm model Local explantion for class 1(safe to drink)

#### Catboost model Feature Importances
#### Catboost model Local explantion for class 1(safe to drink)

### Model demo
#### For model demo catboost model is used.The demo app created by using the streamlit.
#### Manual input fields for the columns
#### Local explanation using shapash smart predictor
 



### File information
 
 * mh_google_cloud_bigquery_ltv_prediction_challenge_EDA.ipynb [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/155Z7TuAi0AmQhRvGyfVtG-Q4ptO2QmiS?usp=sharing)
    #### Basic Exploratory Data Analysis
    #### Packages Used,
        * google.cloud
        * seaborn
        * Pandas
        * Numpy
        * Matplotlib
        * klib
        
