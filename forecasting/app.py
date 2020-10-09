import streamlit as st


@st.cache
def load_predictions(data_location):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Run Streamlit app
st.title('Ride Austin Forecast')

if st.checkbox('Show raw forecast data'):
    st.subheader('Forecasts')
    st.write(pred_df)

st.subheader('Prophet Forecast Accuracy (MAPE)')
st.write(mean_absolute_percentage_error(pred_df['y'], pred_df['pred_prophet']))

st.subheader('XGBoost Forecast Accuracy (MAPE)')
st.write(mean_absolute_percentage_error(pred_df['y'], pred_df['pred_xgb']))



# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)
#
# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
#
# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)