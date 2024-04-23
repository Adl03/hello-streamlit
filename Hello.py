# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from datetime import time, datetime
import yfinance as yf


st.title('My financial dashboard')
st.write('Financial analysis of Google stock')
def plot_my_df(values):
  fig, ax = plt.subplots()
  plt.xticks(rotation = 90)
  ax.plot(values, color = 'green', label = 'Open price')
  ax.legend()
  st.pyplot(fig)
  
start_time = st.slider(
     "When do you start?",
     min_value=datetime(2020, 1, 1),
     max_value=datetime(2022, 1, 1),
     format="MM/DD/YY")

end_time = st.slider(
     "When do you end?",
     min_value=start_time,
     max_value=datetime(2024, 1, 1),
     format="MM/DD/YY")

stock_name = st.selectbox(
     'Select the stock name',
     ('GOOGL', 'AAPL', 'TSLA', 'AMD'))
# Download Google stock data

google_stock = yf.download(stock_name, start = start_time, end= end_time)

st.subheader('Visualize the dataframe')
st.write(google_stock)


if st.button('Plot the open price'):
     plot_my_df(google_stock['Open'])



st.subheader('Visualize the summary for each column')
summary_df = google_stock.agg(["min", "max", "mean"])
st.write(summary_df)





