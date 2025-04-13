import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .stSelectbox, .stNumberInput {
            margin-bottom: 20px;
        }
        .st-b7 {
            color: #2c3e50;
        }
        .st-cj {
            background-color: #e9ecef;
        }
        .stHeader {
            color: #3498db;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        .stSuccess {
            background-color: #d4edda !important;
            color: #155724 !important;
            border-radius: 5px;
            padding: 10px;
            font-size: 18px;
            margin-top: 20px;
        }
        .stTitle {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# App content
st.title("📐 UNIT CONVERTER")

# Add some space
st.markdown("<br>", unsafe_allow_html=True)

conversion_type = st.selectbox('Select the unit type', ['Temperature', 'Length'])

if conversion_type == "Temperature":
    st.header('🌡️ Temperature Converter')
    
    col1, col2 = st.columns(2)
    with col1:
        input_temperature = st.number_input('Enter temperature value:', value=0.0)
    
    with col2:
        original_temperature = st.selectbox('From:', ['Celsius', 'Fahrenheit'])
        converted_temperature = st.selectbox('To:', ['Celsius', 'Fahrenheit'])
    
    if original_temperature == 'Celsius' and converted_temperature == 'Fahrenheit':
        final_temperature = (input_temperature * 1.8) + 32
        st.success(f'Converted Temperature = {final_temperature:.2f} °F')
    elif original_temperature == 'Fahrenheit' and converted_temperature == 'Celsius':
        final_temperature = (input_temperature - 32) / 1.8
        st.success(f'Converted Temperature = {final_temperature:.2f} °C')
    elif original_temperature == converted_temperature:
        st.success(f"Temperature remains the same = {input_temperature:.2f} °{original_temperature[0]}")
    else:
        st.error('Invalid Conversion')

else:
    st.header('📏 Length Converter')
    
    col1, col2 = st.columns(2)
    with col1:
        input_length = st.number_input('Enter length value:', value=0.0)
    
    with col2:
        original_length = st.selectbox('From:', ['Metres', 'Feet'])
        converted_length = st.selectbox('To:', ['Metres', 'Feet'])
    
    if original_length == "Metres" and converted_length == "Feet":
        final_length = input_length * 3.28
        st.success(f"Converted Length = {final_length:.2f} ft")
    elif original_length == "Feet" and converted_length == "Metres":
        final_length = input_length / 3.28
        st.success(f"Converted Length = {final_length:.2f} m")
    elif original_length == converted_length:
        st.success(f"Length remains the same = {input_length:.2f} {'m' if original_length == 'Metres' else 'ft'}")
    else:
        st.error("Invalid Conversion")

# Add some space at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)