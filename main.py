import streamlit as st
from streamlit_option_menu import option_menu
import pickle

heart_disease = pickle.load(open('heart_disease.sav','rb'))
diabetes_disease = pickle.load(open('diabetes_disease.sav','rb'))
kidney_disease = pickle.load(open('kidney_disease.sav','rb'))
lung_disease = pickle.load(open('lung_cancer.sav','rb'))
breast_disease = pickle.load(open('breast_cancer.sav','rb'))
st.set_page_config(page_title='Disease Prediction', page_icon=':syringe:')
#Title
st.title('Disease Prediction using ML')

#Hiding Streamlit Style
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_st_style,unsafe_allow_html=True)

#Slider Menu
with st.sidebar:
    selected = option_menu(
        menu_title="Select the Disease",
        options=["Heart Disease","Diabetes","Kidney Disease","Lung Cancer","Breast Cancer"],
        menu_icon="None",
        
    )
#--Heart Disease
if selected == "Heart Disease":
    #Title 
    st.header("Heart Disease Prediction")

    #Getting the input from the User
    col1 ,col2, col3 = st.columns(3)

    with col1:
            age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
         cp = st.text_input('Chest Pain Type')
    with col1:
         trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')    
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')    
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')    
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')    
    with col3:
        exang = st.text_input('Exercise Induced Angina')    
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')    
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')    
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')    
    with col1:
        thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    #Code for prediction 
    heart_result=''

    #Button for prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])

        if(heart_prediction[0]==0):
            heart_result = ' The Person is Not suffering from Heart Disease'
        else:
            heart_result = ' The Person is Suffering from Heart Disease'
    st.success(heart_result)
    st.caption('Made by Rushi Shah')
    

#--Diasbetes Disease 
if selected == "Diabetes":
    #Title
    st.header("Diabetes Prediction")

    #Getting the input from users
    col1 ,col2 , col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure')
    with col1:
        SkinThickness = st.text_input('Skin Thickness')
    with col2:
        Insuline = st.text_input('Insuline')
    with col3:
        BMI = st.text_input('BMI')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree')
    with col2:
        Age = st.text_input('Age')
        
    #Code for prediction 
    diabetes_result =''

    #Button for prediction
    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_disease.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

        if (diabetes_prediction [0]==0):
            diabetes_result = 'The Person is Not suffering from Diabetes'
        else:
            diabetes_result = 'The Person is Suffering from Diabetes'
        
    st.success(diabetes_result)
    st.caption('Made by Rushi Shah')
    


#--Kidney Disease
if selected == "Kidney Disease":
    #Title
    st.header("Kidney Disease Prediction")

    #Getting the Inputs from User
    col1 , col2 , col3 = st.columns(3)

    with col1:
        Bp = st.text_input('Blood Pressuer')
    with col2:
        Sg = st.text_input('Specific Grravity')
    with col3:
        Al = st.text_input('Alumin level')
    with col1:
        Su = st.text_input('Sugar level')
    with col2:
        Rbc = st.text_input('Red Blood Cell')
    with col3:
        Bu = st.text_input('Blood Urea')
    with col1:
        Sc = st.text_input('Serum Creatinine')
    with col2:
        Sod = st.text_input('Sodium level')
    with col3:
        Pot = st.text_input('Pottasium level')
    with col1:
        Hemo = st.text_input('Hemoglobin level')
    with col2:
        Wbcc = st.text_input('White Blood Cell Count')
    with col3:
        Rbcc = st.text_input('Red Blood Cell Count')
    with col1:
        Htn = st.text_input('Hypertension')

    #Code for prediction 
    kidney_result = ''

    #Button for prediction
    if st.button('Kidney Test Result'):
        kidney_prediction = kidney_disease.predict([[Bp,Sg,Al,Su,Rbc,Bu,Sc,Sod,Pot,Hemo,Wbcc,Rbcc,Htn]])

        if (kidney_prediction [0]==0):
            kidney_result = 'The Person is Not suffering from Diabetes'
        else:
            kidney_result = 'The Person is Suffering from Diabetes'
        
    st.success(kidney_result)
    st.caption('Made by Rushi Shah')

#--Lung Disease
if selected == "Lung Cancer":
    #Title
    st.header("Lung Cancer Prediction")

    #Taking input from user
    col1 , col2 , col3 = st.columns(3)
    
    with col1:
        GENDER = st.text_input('Gender')
    with col2:
        AGE = st.text_input('Age')
    with col3:
        SMOKING = st.text_input('Smoking YES/NO')
    with col1:
        YELLOW_FINGERS = st.text_input('Yellow Fingure YES/NO')
    with col2:
        ANXIETY = st.text_input('Anxiety YES/NO')
    with col3:
        PEER_PRESSURE = st.text_input('Peer Pressure YES/NO')
    with col1:
        CHRONIC_DISEASE = st.text_input('Chronic Disease YES/NO')
    with col2:
        FATIGUE = st.text_input('Flatigue YES/NO')
    with col3:
        ALLERGY = st.text_input('Allergy YES/NO')
    with col1:
        WHEEZING = st.text_input('Wheezing YES/NO')
    with col2:
        ALCOHOL_CONSUMING = st.text_input('Alcohol Consuming YES/NO')
    with col3:
        COUGHING = st.text_input('Coughing YES/NO')
    with col1:
        SHORTNESS_OF_BREATH = st.text_input('Shortness of Breath YES/NO')
    with col2:
        SWALLOWING_DIFFICULTY = st.text_input('Swallowing Problem YES/NO')
    with col3:
        CHEST_PAIN = st.text_input('Chest Pain ')
    
    #Code for Prediction
    lung_result = ''

    #Button for prediction
    if st.button('Lung Test Result'):
        lung_prediction = lung_disease.predict([[GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE ,ALLERGY,WHEEZING,ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]])

        if (lung_prediction [0]==0):
            lung_result = 'The Person is Not suffering from Diabetes'
        else:
            lung_result = 'The Person is Suffering from Diabetes'
        
    st.success(lung_result)
    st.caption('Made by Rushi Shah')


#--Breast Disease
if selected == "Breast Cancer":
    #Title
    st.header("Breast Cancer Prediction")

    #Taking input from user
    col1 , col2 ,col3 = st.columns(3)

    with col1:
        meantexture = st.text_input('Mean Texture')    
    with col2:
        meansmoothness = st.text_input('Mean Smoothness')    
    with col3:
        meancompactness = st.text_input('Mean Compactness')    
    with col1:
        meanconcavity = st.text_input('Mean Concavity')    
    with col2:
        areaerror = st.text_input('Area Error')    
    with col3:
        compactnesserror = st.text_input('Compactness Error')    
    with col1:
        symmetryerror = st.text_input('Symmetry Error')    
    with col2:
        fractaldimensionerror = st.text_input('Fractional Dimension Error')    
    with col3:
        worstradius = st.text_input('Worst Radius')    
    with col1:
        worsttexture = st.text_input('Worst Texture')    
    with col2:
        worstperimeter = st.text_input('Worst Perimeter')    
    with col3:
        worstarea = st.text_input('Worst Area')    
    with col1:
        worstconcavity = st.text_input('Worst Concavity')    
    with col2:
        worstconcavepoints = st.text_input('Worst Concave Points')        
    with col3:
        worstsymmetry = st.text_input('Worst Symmetry')

    #Code for prediction 
    breast_cancer_result =''

    #Button for prediction
    if st.button('Breast Cancer Test Result'):
        breast_cancer_prediction = breast_cancer_disease.predict([[meantexture,meansmoothness,meancompactness,meanconcavity,areaerror,compactnesserror,symmetryerror,fractaldimensionerror,worstradius,worsttexture,worstperimeter,worstarea,worstconcavity,worstconcavepoints,worstsymmetry]])

        if (breast_cancer_prediction [0]==0):
            breast_cancer_result = 'The Person is Not suffering from Breast Cancer'
        else:
            breast_cancer_result = 'The Person is Suffering from Breast Cancer'
        
    st.success(breast_cancer_result)
    st.caption('Made by Rushi Shah')
   


