# rossi-bomberbong

Create frontend and backend stramlit + fastapi: https://medium.com/codex/streamlit-fastapi-%EF%B8%8F-the-ingredients-you-need-for-your-next-data-science-recipe-ffbeb5f76a92

<!-- List files folders and what they are for -->
## Files and Folders
- `state` contains the python files that implement functionalities for each state of the app
- `static` contains the static files for the app
- `app.py` main file that runs streamlit app. Execute with `streamlit run app.py`
- `config_auth.yaml` contains the configuration for the streamlit authenticator
- `db_manager.py` contains the class that manages the SQLite database
- `items.db` SQLite database that stores the items
- `reset_db.py` script to reset the SQLite database
- `rooms.json` JSON file that stores the ETH location names

## Install and compile local model
#### MINI-CPM (Cpu usage)
- git clone https://github.com/ggerganov/llama.cpp
- cd llama.cpp && make
- follow tutorial here https://huggingface.co/openbmb/MiniCPM-V-2_6-gguf to either compile the model or download precompiled and then run it
- Prompt: Analyze the image and identify the main object. Provide a detailed and objective description of its physical features, focusing on visible attributes such as text, colors, shapes, dimensions, logos, brand names, textures, and materials. The response should be a long, cohesive text that covers all discernible details, avoiding any assumptions beyond what is directly observable.
Answer: The main item in the image is described as follows by a cautious writer observer: 
#### CLIP
- use hugging-face or compile it down with same tutorial


## Conda Dependencies
- `streamlit`
- `numpy `
- `folium`
- `matplotlib`
- `pillow`
- `conda-forge::transformers`
- `scikit-learn`

Install dependencies with:
`conda install <dependency1> <dependency2> ...`
Additional pytorch requirement:
`conda install pytorch torchvision torchaudio cpuonly -c pytorch`

## Pip Dependencies
- `streamlit_authenticator`	
- `streamlit_folium`
- `streamlit_extras`
