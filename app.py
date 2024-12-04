import streamlit as st
import joblib
import time
st.title('----------Housing Model🏘️------------')

with st.form(key='model'):
    num1 = st.number_input('Enter the area size:', min_value=0, max_value=20000000)
    num2 = st.number_input('Enter the number of bedrooms:', min_value=0, max_value=20000000)
    num3 = st.number_input('Enter the number of bathrooms:', min_value=0, max_value=20000000)
    num4 = st.number_input('Enter the number of stories:', min_value=0, max_value=20000000)
    
    
    num5 = st.selectbox('Is there a mainroad?', ['Yes', 'No'])
    num5 = 1 if num5 == 'Yes' else 0  # Convert to 1 or 0

    num6 = st.number_input('Enter the number of guestrooms:', min_value=0, max_value=20000000)
    
    
    num7 = st.selectbox('Is there an Air conditioner?', ['Yes', 'No'])
    num7 = 1 if num7 == 'Yes' else 0  # Convert to 1 or 0
    
    
    num8 = st.selectbox('Is parking available?', ['Yes', 'No'])
    num8 = 1 if num8 == 'Yes' else 0  # Convert to 1 or 0
    
   
    num9 = st.selectbox('Is the area a preferred area?', ['Yes', 'No'])
    num9 = 1 if num9 == 'Yes' else 0 

   
    num10 = st.selectbox('Is there a basement?', ['Yes', 'No'])
    num10 = 1 if num10 == 'Yes' else 0
    


    
    # Submit button for form
    submit_button = st.form_submit_button(label='Submit')

# If the form is submitted, load the model and make a prediction
if submit_button:
    model = joblib.load('housing_model')
    answer = model.predict([[num1, num2, num3, num4, num5, num6, num7, num8, num9]])

    # Display the prediction result
    #st.success(f'The Predicted Answer is: {answer[0]}')
    #st.balloons()
with st.spinner('Making prediction...'):
    model = joblib.load('housing_model')
    answer = model.predict([[num1, num2, num3, num4, num5, num6, num7, num8, num9]])
    time.sleep(2)  # type: ignore # Simulate a delay while the model is predicting
    # After waiting for the model to make a prediction
    st.success(f'The Predicted Answer is: {answer[0]}')
