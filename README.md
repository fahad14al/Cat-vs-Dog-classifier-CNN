Dog vs Cat Convolution Neural Network Classifier

WebApp link : https://cat-vs-dog-classifier-cnn.streamlit.app/

# Cat vs Dog Classifier (CNN)

A deep learning based image classifier built using Convolutional Neural Networks (CNN) to distinguish between images of cats and dogs.  
This project includes training, inference via a Streamlit web app, and deployment components.

---

## 📂 Repository Structure

.
├── app.py
├── cats_dogs_model.h5
├── cats_vs_dogs.ipynb
├── requirements.txt
└── README.md


- **app.py** — Streamlit application for inference / demo  
- **cats_dogs_model.h5** — Trained CNN model weights  
- **cats_vs_dogs.ipynb** — Notebook containing data exploration, preprocessing, training, and evaluation  
- **requirements.txt** — Python dependencies required to run the project  
- **README.md** — This documentation file  

---

## 🧠 Features & Workflow

1. **Data preprocessing & augmentation** (inside the notebook)  
2. **Model building**: a CNN architecture to classify images  
3. **Training & evaluation**, saving the best model  
4. **Inference / Web App**: upload an image in the Streamlit app and get prediction (Cat or Dog)  
5. **Deployment**: (optional) can be deployed on Streamlit Cloud / Heroku / etc.

---

## 📥 Requirements & Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/fahad14al/Cat-vs-Dog-classifier-CNN.git
   cd Cat-vs-Dog-classifier-CNN

2.python -m venv venv
source venv/bin/activate        # On Linux / macOS
.\venv\Scripts\activate         # On Windows PowerShell

3.pip install -r requirements.txt

4.pip install -r requirements.txt
