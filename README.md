# NEUBAITICS FULLSTACK AI  

## 🚀 AI-Powered Review Sentiment & Insights Dashboard  

### 📌 Introduction  
With the exponential growth of online reviews, businesses struggle to analyze customer feedback efficiently. Our AI-powered sentiment analysis dashboard simplifies this process by providing a structured way to analyze sentiments, visualize trends, and make data-driven decisions.  

---

## ❓ Problem Statement  
Online businesses receive a massive number of reviews daily. Manually analyzing customer feedback is time-consuming and prone to errors. There is a need for an automated system that can classify reviews into sentiments (Positive, Neutral, Negative) and generate insights for better decision-making.  

---

## 🎯 Aim  
To develop a **full-stack AI-powered web application** that:  
✅ Automates review sentiment analysis  
✅ Provides a user-friendly dashboard for insights  
✅ Helps businesses track sentiment trends over time  

---

## 💡 Motivation  
- **Customer Insights**: Helps businesses understand their customers' opinions.  
- **Market Analysis**: Identifies patterns in customer feedback.  
- **Automation**: Saves time and resources by automating sentiment analysis.  
- **User Experience Improvement**: Enables businesses to improve products/services based on feedback.  

---

## ✅ Advantages  
✔️ **Automated Sentiment Analysis** – No manual effort required  
✔️ **Real-time Insights** – Instant feedback classification  
✔️ **User-friendly Dashboard** – Visual representation of sentiment trends  
✔️ **Scalability** – Can handle a large volume of reviews  
✔️ **Multi-domain Application** – Useful for e-commerce, social media, and customer service  

---

## ❌ Disadvantages  
❌ **AI Model Limitations** – Accuracy depends on dataset quality  
❌ **Context Understanding** – AI may misinterpret sarcasm or complex reviews  
❌ **Real-time Processing** – Can be slow if dealing with a massive dataset  

---

## 🌟 Features  

### 🔐 User Features  
- **User Registration & Login** (JWT-based authentication)  
- **Review Submission**: Users can enter product reviews.  
- **Sentiment Analysis**: AI model classifies sentiment as:  
  - ✅ Positive  
  - ❌ Negative  
  - 🟡 Neutral  
- **Dashboard**:  
  - 📊 Sentiment distribution over time  
  - 📝 Recent reviews with sentiment highlights  
  - ⏳ Filter by date range  

---

## 🛠 Tech Stack  

| Component      | Technology |
|---------------|------------|
| **Frontend**  | React.js (Vite/Next.js) + Tailwind CSS |
| **Backend**   | FastAPI / Flask (Python) |
| **Database**  | PostgreSQL / MongoDB |
| **AI Model**  | Hugging Face Transformers (BERT) / NLTK (VADER) |
| **Authentication** | JWT-based login & session management |
| **Deployment** | Frontend (Vercel/Netlify) + Backend (Render/AWS) |

---

## 🔧 Features Breakdown  

### **Frontend (React.js)**  
✅ JWT-based Authentication (Signup/Login)  
✅ Review Submission Form  
✅ AI Sentiment Analysis Display  
✅ **Interactive Dashboard:**  
  - 📈 Line graph for sentiment trends  
  - 🎨 Sentiment color coding for reviews  
  - 🔍 Filters for selecting time range  

### **Backend (FastAPI / Flask)**  
✅ Secure User Authentication (JWT)  
✅ API for Review Submission & Sentiment Analysis  
✅ AI-based Sentiment Classification (VADER/BERT)  
✅ API for Sentiment Trends & Dashboard Data  

### **AI Model**  
- **Basic**: NLTK VADER for quick analysis  
- **Advanced**: Fine-tuned BERT model from Hugging Face  
- **Functionality**:  
  - Preprocesses text  
  - Predicts sentiment category  
  - Returns confidence score  

### **Database (PostgreSQL / MongoDB)**  
✅ **Users Table**: Stores credentials  
✅ **Reviews Table**: Stores reviews & sentiment results  
✅ **Sentiment Trends**: Aggregates data for visualization  

---

## 🚀 Deployment Plan  

| Component | Platform |
|-----------|----------|
| **Frontend** | Vercel / Netlify |
| **Backend** | Render / AWS EC2 |
| **Database** | MongoDB Atlas / Supabase (PostgreSQL) |

---

## 📊 Evaluation Criteria  

| Category         | Criteria | Max Marks |
|-----------------|---------------------------|------------|
| **Frontend**    | Responsive UI, smooth UX  | 15 |
| **Backend**     | API correctness, error handling | 15 |
| **Authentication** | Secure JWT-based system | 10 |
| **AI Model**    | Accurate sentiment classification | 15 |
| **Database**    | Efficient schema & query handling | 10 |
| **Dashboard**   | Data visualization & filtering | 15 |
| **Deployment**  | Live working version | 10 |
| **Code Quality** | Modular, well-structured code | 10 |
| **Total**       |  | **100** |

---

## 📌 How to Run the Project  

### 🔥 Prerequisites  
Make sure you have the following installed:  
- **Node.js** (for frontend)  
- **Python** (for backend)  
- **MongoDB/PostgreSQL** (for database)  
- **Git** (for version control)  

### 🛠 Installation Steps  

#### 📍 Clone the Repository  
```sh
git clone https://github.com/SETHU0010/neubaitics-fullstack-ai.git
cd neubaitics-fullstack-ai
