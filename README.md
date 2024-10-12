# rossi-bomberbong

Create frontend and backend stramlit + fastapi: https://medium.com/codex/streamlit-fastapi-%EF%B8%8F-the-ingredients-you-need-for-your-next-data-science-recipe-ffbeb5f76a92

<!-- List files folders and what they are for -->
## Files and Folders
- `state` contains the python files that implement functionalities for each state of the app
- `app.py` main file that runs streamlit app. Execute with `streamlit run app.py`

## Install and compile local model
### MINI-CPM (Cpu usage)
- git clone https://github.com/ggerganov/llama.cpp
- cd llama.cpp && make
- follow tutorial here https://huggingface.co/openbmb/MiniCPM-V-2_6-gguf to either compile the model or download precompiled and then run it
- Prompt: Analyze the image and identify the main object. Provide a detailed and objective description of its physical features, focusing on visible attributes such as text, colors, shapes, dimensions, logos, brand names, textures, and materials. The response should be a long, cohesive text that covers all discernible details, avoiding any assumptions beyond what is directly observable.
Answer: The main item in the image is described as follows by a cautious writer observer: 
### CLIP
- use hugging-face or compile it down with same tutorial


<!-- list dependencies -->
## Conda Dependencies
- `streamlit`
- `numpy `
- `folium`
- `matplotlib`
- `pillow`

Install dependencies with:
`conda install <dependency1> <dependency2> ...`

## Pip Dependencies
- `streamlit_authenticator`	
- `streamlit_folium`
