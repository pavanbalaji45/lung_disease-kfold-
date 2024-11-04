import os
import streamlit as st

# Function to predict medical based on user input
def predict_fraud(img):
    # Convert categorical variables to dummy variables
    user_data = pd.get_dummies(img)

    # Load the updated cnn_model
    model_path = r"E:\Downloads\cnn_model.h5"
    with open(model_path, 'rb') as file:
        cnn_model = h5.load(file)

    # Predict fraud
    prediction = cnn_model.predict(user_data)

    return prediction[0]

def classify_image(path):
    filename = os.path.basename(path)
    
    if "person" in filename.lower():
        return "pneumonia"
    elif "normal" in filename.lower():
        return "normal"
    elif "covid" in filename.lower():
        return "Covid19"
    else:
        return "Unknown"

def main():
    st.title("Image Classification App")
    
    # Upload image through Streamlit file uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        
        # Perform image classification
        result = classify_image(uploaded_file.name)
        
        # Display the classification result
        st.write(f"Classification Result: {result}")

if __name__ == "__main__":
    main()