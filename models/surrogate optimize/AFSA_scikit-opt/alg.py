import streamlit as st

# Define possible modelsd in a dict
# Format of the dict: model name -> model code

MODEL = {
    "model": "AFSA",
}

# LightGBM can use -- categorical features -- as input directly. It doesn’t need to convert 
# to one-hot encoding, and is much faster than one-hot encoding (about 8x speed-up).

def show():
    """Shows the components for the template and returns user inputs as dict."""
    
    # `show()` is the only method required in this module. You can add any other code 
    # you like above or below. 
    
    inputs = {}  # dict to store all user inputs until return
    
    # with st.sidebar:
        
    # Render all template-specific sidebar components here. 

    # Use ## to denote sections. Common sections for training templates: 
    # Model, Input data, Preprocessing, Training, Visualizations
    # Store all user inputs in the `inputs` dict. This will be passed to the code
    # template later.
    inputs["model"] = MODEL["model"]
    
    
    st.info('TO SOLVE **OPT**')

    col1, col2 = st.columns([2,2])
    with col1:
        with st.expander("Hyper Parameter"):
            inputs['n dim'] = st.number_input('variable dim', 1, 20, 1)
            inputs['size pop'] = st.number_input('size pop', 1, 500, 20)
            inputs['max iter'] = st.number_input('max iter', 1, 10000, 50)
            inputs['max try num'] = st.number_input('max try num',1, 1000, 100)
            inputs['step'] = st.slider('step', 0.0, 1.0, 0.5)
            inputs['visual'] = st.slider('vissual', 0.0, 1.0, 0.3)
            inputs['q'] = st.slider('q', 0.0, 1.0, 0.98)
            inputs['delta'] = st.slider('delta', 0.0, 1.0, 0.5)
            
    return inputs,col2
        
# To test the alg independent of the app or template, just run 
# `streamlit run alg.py` from within this folder.
if __name__ == "__main__":
    show()
    
    