from unicodedata import category
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# function to select number os lines to display
def show_line_number(dataframe):
    numb_lines = st.sidebar.slider('Select number of lines that you want to display: ',min_value = 1, max_value = len(dataframe), step =1)
    st.write(dataframe.head(numb_lines).style.format(subset = ['overall_score'],formatter="{:.1f}"))

# function to creat chart
def plot_chart(dataframe, category):

    data_plot = dataframe.query('industry == @category')

    fig, ax = plt.subplots(figsize=(8,6))
    ax = sns.barplot(x = 'size', y = 'overall_score', data = data_plot)
    ax.set_title(f'Numer of companies at {category}', fontsize = 16)
    ax.set_xlabel('industry', fontsize = 12)
    ax.tick_params(rotation = 20, axis = 'x')
    ax.set_ylabel('size', fontsize = 12)
  
    return fig

#loading csv data
b_data = pd.read_csv('b_impact_simple.csv',index_col=0,sep=';')

st.title('B Corp analysis: an investor`s perspective\n')
st.write('This article aims to propose suitable impact-based incentive structures for Impact Fund Managers using by B-Corp Scores')

#show table
checkbox_show_table = st.sidebar.checkbox('Show Table')
if checkbox_show_table:
    st.sidebar.markdown('## Table filter')
    
    size_group = list(b_data['size'].unique())
    size_group.append('All')

    categories = st.sidebar.selectbox('Select company size', options= size_group)

    if size_group != 'All':
        df_size_group = b_data.query('size == @categories')
        show_line_number(df_size_group)
    else:   
        show_line_number(b_data)

# Chart filter
st.sidebar.markdown('## Chart filter')

chart_category = st.sidebar.selectbox('Select Industry to be displayed: ', options=b_data['industry'].unique())
chart = plot_chart(b_data,chart_category)
st.pyplot(chart)






