# **AI-Powered Speech-to-Video Avatar**  

This project converts **speech into a talking AI avatar** using deep learning and AI models. It takes an audio file as input, generates lip-syncing animations, and renders a video of an avatar speaking the given audio.  

🚀 **Live Demo**: [AI-Powered Speech-to-Video Avatar](https://avatar-lip-sync.streamlit.app/)  
📝 **Medium Blog**: [Creating an AI-Powered Speech-to-Video Avatar](https://medium.com/@nelaynabbas5/creating-an-ai-powered-speech-to-video-avatar-with-deep-learning-models-bd885454b328)  
📂 **GitHub Repository**: [Avatar-Lip-Sync](https://github.com/NelaynAbbas/Avatar-lip-sync)  

---

## **📌 Features**  
✅ Converts speech/audio into a **realistic talking AI avatar**  
✅ Uses **deep learning** for accurate **lip-syncing**  
✅ **FastAPI backend** for processing audio and generating video  
✅ **Streamlit frontend** for an easy-to-use interface  
✅ Supports multiple languages and accents  

---

## **🛠️ Tech Stack**  
![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)  
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)  
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)  
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)  
![Torch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)  
![Numpy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)  

---

## **📌 Installation Guide**  

### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/NelaynAbbas/Avatar-lip-sync.git
cd Avatar-lip-sync
```

### **Step 2: Set Up a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **Step 3: Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **Step 4: Run the Backend (FastAPI Server)**  
```bash
uvicorn backend:app --host 0.0.0.0 --port 8000 --reload
```
The FastAPI server will be running at:  
📌 **http://127.0.0.1:8000**  

### **Step 5: Run the Frontend (Streamlit App)**  
```bash
streamlit run app.py
```
The Streamlit app will open in your browser.  

---

## **🚀 Usage Guide**  
1. **Upload an audio file** (or record directly).  
2. Select a **pre-trained AI avatar**.  
3. Click **Generate Video**.  
4. The AI will generate a **lip-synced avatar video**.  
5. Download or share the generated video.  

---

## **📜 License**  
This project is **open-source** and available under the **MIT License**. Feel free to use and modify it!  

---

## **📩 Connect With Me**  

👤 **Nelayn Abbas**  
🌐 [GitHub](https://github.com/NelaynAbbas)  
📧 **Email:** nelaynabbas@example.com  

<p align="right">(<a href="#readme-top">back to top</a>)</p>  

---
