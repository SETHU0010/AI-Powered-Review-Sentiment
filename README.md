# NEUBAITICS FULLSTACK AI  

## AI-Powered Review Sentiment & Insights Dashboard  

### Objective  
Develop a full-stack AI-powered web application that allows users to input product/service reviews, analyze sentiment, and visualize trends over time. The system includes user authentication and a dashboard to track sentiment insights.  

## Project Scope  

### 1. User Features  
- **User Registration & Login** (JWT-based authentication)  
- **Review Submission**: Users can enter product reviews.  
- **Sentiment Analysis**: AI model classifies sentiment as:  
  - Positive ✅  
  - Negative ❌  
  - Neutral 🟡  
- **Dashboard**:  
  - Sentiment distribution over time 📊  
  - Recent reviews with sentiment highlights 📃  
  - Filter by date range ⏳  

## 2. Tech Stack  

| Component      | Technology |
|---------------|------------|
| **Frontend**  | React.js (Vite/Next.js) + Tailwind CSS |
| **Backend**   | FastAPI / Flask (Python) |
| **Database**  | PostgreSQL / MongoDB |
| **AI Model**  | Hugging Face Transformers (BERT) / NLTK (VADER) |
| **Authentication** | JWT-based login & session management |
| **Deployment** | Frontend (Vercel/Netlify) + Backend (Render/AWS) |

---

## Features Breakdown  

### **Frontend (React.js)**  
- JWT-based Login & Signup  
- Review Submission Form  
- Sentiment Result Display  
- **Interactive Dashboard:**  
  - 📈 Line graph for sentiment trends  
  - 🎨 Reviews displayed with sentiment color coding  
  - 🔍 Filters for selecting time range  

### **Backend (FastAPI / Flask)**  
- Secure User Authentication (Signup, Login, Logout - JWT)  
- API for Review Submission & Sentiment Analysis  
- AI-based Sentiment Classification (VADER/BERT)  
- Dashboard API for Sentiment Trends  

### **AI Model**  
- **Basic**: NLTK VADER for quick analysis  
- **Advanced**: Fine-tuned BERT model from Hugging Face  
- **Functionality**:  
  - Preprocesses text  
  - Predicts sentiment category  
  - Returns confidence score  

### **Database (PostgreSQL / MongoDB)**  
- **Users Table**: Stores credentials  
- **Reviews Table**: Stores reviews & sentiment results  
- **Sentiment Trends**: Aggregates data for visualization  

---

## **Deployment Plan**  
- **Frontend** → Vercel / Netlify  
- **Backend** → Render / AWS EC2  
- **Database** → MongoDB Atlas / Supabase (PostgreSQL)  

---

## **Evaluation Criteria**  

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

## **Submission Requirements**  
- **GitHub Repository** (frontend & backend in separate folders)  
- **README Documentation**:  
  - Installation & Setup Instructions  
  - API Endpoints  
  - Features Breakdown  
- **Live Deployed Links** (Frontend, Backend API, and Database)  

---

## **Bonus Features (For Extra Challenge 🚀)**  
- AI Explanation: Why the model classified sentiment a certain way  
- Email Notifications: Weekly sentiment trend reports 📩  
- Admin Dashboard: Manage reviews & monitor trends  

---

## **Application Flow**  

1. **User Registration & Authentication**  
   - Users sign up/login via JWT authentication.  
2. **Review Submission**  
   - Users submit a product review.  
3. **AI Sentiment Analysis**  
   - AI model classifies the sentiment.  
4. **Data Storage**  
   - Review & sentiment result are stored in the database.  
5. **Displaying Sentiment Result**  
   - Users see real-time feedback on their review.  
6. **Dashboard Insights**  
   - Users track sentiment trends.  
7. **Admin Panel (Optional)**  
   - Admin manages reviews & analytics.  
8. **Deployment & Live Access**  
   - App is deployed for real-world use.  

