import streamlit as st
import pickle
import numpy as np

# Load the pickled model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

def make_prediction(features):
    # Perform any necessary preprocessing on the features
    # Make predictions using the loaded model
    prediction = model.predict(np.array([15.0,13.2,61.0,3.9,719.0,1.03,0.0,0.0,0.0,1.0,2018.0,4.0,0.0,0.0,0.0]).reshape(1,-1))

    return prediction

def main():
    # Set the title and a short description
    st.title("Bike sharing")
    st.write("Enter the required features and click 'Predict' to get the prediction.")


    # hour
    hour = st.number_input("hour")

    #temp
    temp = st.number_input("temperature")

    #humidity
    humidity = st.number_input("Humidity")

    #wind speed
    wind_speed = st.number_input("Wind Speed")

    #visibility
    visibility = st.number_input("visibility")

    #solar radiation
    solar_radiation = st.number_input("Solar Radiation")

    #Rain fall 
    rain_fall = st.number_input("rain fall")

    #snow fall
    snow_fall = st.number_input("Snow Fall")

    feature3 = st.selectbox("Feature 1", ["Category 1", "Category 2", "Category 3"])
    print(feature3)
    # Create input fields for the features
    feature1 = st.number_input("Feature 1")
    feature2 = st.number_input("Feature 2")
    # Add more input fields for other features if needed

    # Create a button to make predictions
    if st.button("Predict"):
        # Create a feature array from the input values
        features = np.array([feature1, feature2]).reshape(1, -1)

        # Call the make_prediction function
        prediction = make_prediction(features)

        # Display the prediction
        st.write("Prediction:", prediction)

if __name__ == '__main__':
    main()
