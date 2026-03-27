## ATS Resume Checker - AI-Powered Application

An intelligent web application that analyzes resumes against job descriptions using NLP techniques. It provides ATS match scores, identifies missing keywords, highlights matching skills, and offers improvement suggestions.

### 🚀 Quick Start

#### Prerequisites
- Python 3.8 or higher
- Windows, macOS, or Linux

#### Setup & Run

1. **Navigate to the project directory:**
   ```PowerShell
   cd "c:/Web Developement Project/6.3 CSS Box Model/Ai Agent"
   ```

2. **Start the Backend API (in one terminal):**
   ```PowerShell
   cd backend
   .\venv\Scripts\python.exe app.py
   ```
   The backend will run on `http://localhost:5000`

3. **Start the Frontend Server (in another terminal):**
   ```PowerShell
   cd ..
   .\backend\venv\Scripts\python.exe server.py
   ```
   The frontend will run on `http://localhost:8000`

4. **Open the Application:**
   Go to `http://localhost:8000` in your web browser

### 📋 How to Use

1. **Upload Resume:**
   - Upload a PDF resume OR paste resume text directly

2. **Enter Job Description:**
   - Paste the job description text

3. **Click "Analyze Resume":**
   - The application will analyze and display results

4. **Review Results:**
   - **ATS Match Score:** Percentage match (0-100%)
   - **Matching Skills:** Skills from your resume that match the job
   - **Missing Keywords:** Key terms to add to improve match
   - **Suggestions:** Actionable recommendations
   - **Section Feedback:** Insights on Skills, Experience, Education

5. **Download Suggestions:**
   - Click "Download Suggestions" to save a text file with improvement tips

### 🏗️ Project Structure

```
Ai Agent/
├── backend/
│   ├── venv/                 (Python virtual environment)
│   ├── app.py               (Flask API server)
│   ├── nlp_utils.py         (NLP processing logic)
│   ├── resume_parser.py     (Resume parsing utilities)
│   └── requirements.txt     (Python dependencies)
├── frontend/
│   ├── index.html           (Main UI)
│   ├── script.js            (Frontend logic & API calls)
│   └── style.css            (Custom styles)
├── server.py                (Frontend HTTP server)
├── test_backend.py          (Backend API test)
└── README.md               (This file)
```

### 🔧 Technology Stack

**Backend:**
- **Framework:** Flask
- **NLP Libraries:** spaCy, NLTK, scikit-learn
- **PDF Processing:** pdfplumber
- **Server:** Python built-in HTTP server

**Frontend:**
- **HTML5 / CSS3** with Bootstrap 5
- **JavaScript** (Vanilla, no frameworks)
- **Charts:** Chart.js (optional)

### 🎯 Core Features

✅ **Resume Parsing**
- Extract text from PDF files
- Support for text input

✅ **Intelligent Analysis**
- Extract keywords and skills
- Calculate similarity scores
- Identify missing keywords

✅ **ATS Scoring**
- 50% keyword match score
- 50% semantic similarity score
- Combined ATS percentage

✅ **Comprehensive Feedback**
- Matching skills highlighted
- Missing keywords listed
- Actionable suggestions
- Section-wise feedback

✅ **User-Friendly Output**
- Progress bar visualization
- Color-coded results
- Downloadable suggestions
- Responsive design

### 🚨 Troubleshooting

**Issue: "Page Not Found" Error**
- Ensure both servers are running (backend on 5000, frontend on 8000)
- Check that port 5000 and 8000 are not blocked by firewall

**Issue: No matching skills found**
- Try using more technical terms in your resume
- Check the Skills section in feedback

**Issue: API Connection Error**
- Verify backend is running: `http://localhost:5000`
- Check browser console (F12) for detailed error messages
- Make sure you're accessing frontend via `http://localhost:8000` not `file://`

**Issue: PDF Upload Not Working**
- Ensure PDF file is valid and not corrupted
- Try using text input instead
- Check browser console for file size errors

### 📊 Sample Resume & Job Description

**Sample Resume:**
```
John Doe
Software Engineer

Skills:
Python, JavaScript, React, Node.js, AWS, Docker, Git

Experience:
- Developed REST APIs using Python Flask
- Built React web applications
- Managed AWS infrastructure

Education:
BS Computer Science
```

**Sample Job Description:**
```
We are hiring a Full-Stack Developer
Required Skills:
- Python programming
- JavaScript and React
- AWS and Docker
- REST API development

Experience Required: 3+ years
```

**Expected Score:** 70-80%

### 🔑 API Endpoint

**POST /analyze**

Analyze a resume against a job description.

**Request:**
```json
{
    "resume_text": "Your resume text here",
    "job_description": "Job description text here"
}
```

**Or (with file upload):**
```
Form Data:
- file: [PDF file]
- job_description: [Job description text]
```

**Response:**
```json
{
    "ats_score": 75.5,
    "matching_skills": ["python", "react", "aws"],
    "missing_keywords": ["docker", "kubernetes"],
    "suggestions": ["Add Docker experience", "Highlight cloud skills"],
    "feedback": {
        "skills": "Good match on core skills",
        "experience": "Add quantifiable metrics",
        "education": "Verify degree requirements"
    }
}
```

### 🎓 How It Works

1. **Resume Extraction:** Extracts text from PDF or accepts direct input
2. **Text Processing:** Tokenizes and cleans both resume and job description
3. **Skill Matching:** Identifies technical skills using pattern matching
4. **Keyword Analysis:** Extracts and compares keywords using TF-IDF
5. **Similarity Scoring:** Calculates semantic similarity using cosine similarity
6. **ATS Calculation:** Combines keyword match (50%) + semantic similarity (50%)
7. **Suggestions:** Generates improvement recommendations based on gaps

### 📈 Future Enhancements

- [ ] Download optimized resume with suggestions
- [ ] Save analysis history (user dashboard)
- [ ] Advanced ML models (BERT, GPT)
- [ ] LinkedIn integration
- [ ] Database integration for user profiles
- [ ] Cloud deployment (AWS, Heroku)
- [ ] Mobile app version
- [ ] Real-time collaboration

### 📝 License

This project is open source and available for educational and personal use.

### 💡 Tips for Best Results

1. **Keep resume updated** with recent skills and projects
2. **Use industry-specific keywords** relevant to your field  
3. **Quantify achievements** (e.g., "Reduced load time by 40%")
4. **Match job description language** in your resume
5. **Test multiple job descriptions** to refine your resume
6. **Focus on high-scoring matches** (70%+) for job applications

### 🤝 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review the browser console (F12) for errors
3. Verify both servers are running
4. Check file permissions and disk space

---

**Happy Job Hunting!** 🎯 Resume tips from the ATS Resume Checker