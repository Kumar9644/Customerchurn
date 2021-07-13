import streamlit as st
from joblib import *
st.title('Telecom Customer Churn Prediction')
model=load('churn.ml')
def main():
    st.image('1.png')
    st.write('Please enter the below asked details')
    num=[0,1]
    contract=['Month-to-Month','One-Year','Two-year']
    payement=['Bank Transfer(automatic)','Credit Card','Electronic Check','Mailed Check']
    num_1=[0,1,2]
    num_2 = [0, 1, 2,3]
    s_citi=['No','Yes']
    line=['DSL','Fiber optic','No']
    citizen=st.radio('Senior Citizen',num,format_func=lambda x:s_citi[x])
    partner=st.radio('Partner',num,format_func=lambda x:s_citi[x])
    depe=st.radio('Dependents',num,format_func=lambda x:s_citi[x])
    tenure=st.number_input('Enter tenure',min_value=0,max_value=100,step=1)
    mple=st.radio('Multiple Lines',num_1,format_func=lambda x:line[x])
    internet=st.radio('Internet Service',num,format_func=lambda x:s_citi[x])
    os = st.radio('Online Security', num, format_func=lambda x: s_citi[x])
    ob=st.radio('Online Backup',num,format_func=lambda x:s_citi[x])
    dp=st.radio('Device Protection',num,format_func=lambda x:s_citi[x])
    ts=st.radio('Tech Support',num,format_func=lambda x:s_citi[x])
    stv=st.radio('Streaming TV',num,format_func=lambda x:s_citi[x])
    smv=st.radio('Streaming Movies',num,format_func=lambda x:s_citi[x])
    cont=st.radio('Contract',num_1,format_func=lambda x:contract[x])
    pb=st.radio('Paperless billing',num,format_func=lambda x:s_citi[x])
    pm=st.radio('Payment Type',num_2,format_func=lambda x:payement[x])
    mc = st.number_input('Monthly Charges', step=1)
    tc=st.number_input('Total Charges',step=1)
    if st.button('Predict Churn'):
        array=[citizen,partner,depe,tenure,mple,internet,os,ob,dp,ts,stv,smv,cont,pb,pm,mc,tc]
        y_pred=model.predict([array])
        if y_pred==0:
            st.write('Likely to churn')
        else:
            st.write('Less likely to churn')









if __name__ == '__main__':
    main()
