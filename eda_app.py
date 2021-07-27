# Core Packages
import streamlit as st

# Load EDA Packages
import pandas as pd
import numpy as np

# Load Data Viz packages
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 

# Load Data
data = pd.read_csv("data/diabetes_data_upload.csv")
age_dist = pd.read_csv("data/freqdist_of_age_data.csv")
encoded_df = pd.read_csv("data/diabetes_data_upload_clean.csv")

def bi_feature_desc(feature):
    total_count = encoded_df[feature].count()
    st.text('Total Count: {}'.format(total_count))
    yes_no = encoded_df[feature].value_counts()
    st.text("Total 'Yes': {}".format(yes_no.iloc[0]))
    st.text("Total 'No': {}".format(yes_no.iloc[1]))
    yes_no = encoded_df[feature].value_counts(normalize=True)
    yes_perc = yes_no.iloc[0].round(4)
    st.text("'Yes' %: {}%".format(yes_perc*100))
    no_perc = yes_no.iloc[1].round(4)
    st.text("'No' %: {}%".format(no_perc*100))

    

def eda_main():
    st.title('This is from the EDA section')
    

    submenu = st.sidebar.selectbox('Submenu', ['Descriptive Analysis','Plot'])

    # Display the Dataset
    st.dataframe(data)


    if submenu == 'Descriptive Analysis':
        # Initial Data Summary
        col1, col2, col3 = st.beta_columns([3,3,4])
        # Dataset Shape
        with col1:
            expand1 = st.beta_expander('Dataset Shape')
            with expand1:
                rows,columns = data.shape
                st.write('Number of rows : {}'.format(rows))
                st.write('Number of rows : {}'.format(columns))
        
        # Class Info        
            expand3 = st.beta_expander("Target Class Distribution")
            with expand3:
                st.dataframe(data['class'].value_counts())
        
                

        # Age Info
        with col2:
            expand4 = st.beta_expander('Age Column Summary')            
            with expand4:
                st.dataframe(data.describe())
            expand5 = st.beta_expander('Gender Distribution')

        # Gender Distribution    
            with expand5:
                st.dataframe(data['Gender'].value_counts())   
        
        # Dataset Datatypes 
        with col3:     
            expand2 = st.beta_expander('Dataset Datatypes')
            with expand2:
                dtype_df = data.dtypes
                dtype_df.name = 'Datatypes'
                st.dataframe(dtype_df)
        

    elif submenu == 'Plot':
        st.subheader("Plot")

        # Gender Distribution Plots       
        expand1 = st.beta_expander('Distribution Summary of Gender')
        with expand1:
            c1,c2 = st.beta_columns([2,3])
            with c1:
                # Frequency Distribution
                freq_df_gender = data['Gender'].value_counts().reset_index()
                freq_df_gender.columns = ['Gender','Frequency']
                st.dataframe(freq_df_gender)

                # Percentage Distribution
                perc_df_gender = data['Gender'].value_counts(normalize=True).reset_index()
                perc_df_gender.columns = ['Gender','Frequency %']
                perc_df_gender['Frequency %'] = perc_df_gender['Frequency %']*100
                st.dataframe(perc_df_gender)

                

                # Pie Distribution
                pie, ax = plt.subplots()
                labels = ['Male', 'Female']
                ax = plt.pie(x=perc_df_gender['Frequency %'], autopct="%.1f%%",  labels=labels, pctdistance=0.5,colors=['#AFCDDC', 'Pink'])
                plt.legend(loc='best')
                st.pyplot(pie)


            with c2:
                
                # Countplot
                fig= plt.figure(figsize=(5,3))
                sns.countplot(data=data, x= 'Gender', palette='RdBu_r')
                st.pyplot(fig)

                # Bar Plot
                fig= plt.figure(figsize=(5,3))
                sns.barplot(data=perc_df_gender, x= 'Gender',y='Frequency %', palette='RdBu_r')
                st.pyplot(fig)

        # Class Distribution
        expand2 = st.beta_expander('Distribution Summary of Class')
        with expand2:
            c1,c2 = st.beta_columns([2,3])
            with c1:
                # Frequency Distribution
                freq_df = data['class'].value_counts().reset_index()
                freq_df.columns = ['Target Class','Frequency']
                st.dataframe(freq_df)

                # Percentage Distribution
                perc_df = data['class'].value_counts(normalize=True).reset_index()
                perc_df.columns = ['Target Class','Frequency %']
                perc_df['Frequency %'] = perc_df['Frequency %']*100
                st.dataframe(perc_df)

                

                # Pie Distribution
                pie, ax = plt.subplots()
                labels = ['Yes', 'No']
                ax = plt.pie(x=perc_df['Frequency %'], autopct="%.1f%%",  labels=labels, pctdistance=0.5,colors=['#5bd45b', '#d4a45b'])
                plt.legend(loc='best')
                st.pyplot(pie)


            with c2:
                
                # Countplot
                fig= plt.figure(figsize=(5,3))
                sns.countplot(data=data, x= 'class', palette='Spectral_r')
                st.pyplot(fig)

                # Bar Plot
                fig= plt.figure(figsize=(5,3))
                sns.barplot(data=perc_df, x= 'Target Class',y='Frequency %', palette='Spectral_r')
                st.pyplot(fig)
        
        # Frequency Distribution of Age
        expand3 = st.beta_expander('Frequency Distribution of Age')
        with expand3:
            #age_dist.drop(['Unnamed: 0'],axis=1,inplace=True)
            c1, c2 = st.beta_columns(2)
            with c1:
                st.dataframe(age_dist)
            with c2:
                fig, ax = plt.subplots()
                ax = sns.barplot(data=age_dist, x='Age', y='count',color = '#f63366')
                plt.setp(ax.get_xticklabels(), rotation=90)
                st.pyplot(fig)
        
        # Outlier Detection
        expand4 = st.beta_expander('Outlier Detection')
        with expand4:
            p1 = px.box(data,x='Age',color='Gender')
            st.plotly_chart(p1,use_container_width=True)

        # Binary Features Descriptive Summary
        expand5 = st.beta_expander('Binary Features Descriptive Summary')
        with expand5:
            c1, c2 = st.beta_columns(2)

            bi_features_df = encoded_df.iloc[:,2:]
            with c1:
                attribute = st.selectbox('Choose column',bi_features_df.columns)
            with c2:
                bi_feature_desc(attribute)

        # Correlations
        expand6 = st.beta_expander('Correlations')
        with expand6:
            corr_matrix = encoded_df.corr()
            fig = plt.figure(figsize=(20,10))
            sns.heatmap(corr_matrix, annot=True, cmap='rocket_r')
            st.pyplot(fig)