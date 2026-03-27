import requests
import json

# Test data
test_resume = """
John Doe
Senior Software Engineer
Email: john@example.com

SKILLS:
Python, Java, JavaScript, React, Node.js, AWS, Docker, Git

EXPERIENCE:
- Developed REST APIs using Python and Flask
- Built React web applications
- Managed AWS infrastructure using Docker containers

EDUCATION:
B.S. Computer Science
"""

test_job_description = """
We are looking for a Software Engineer with the following skills:
- Python programming
- JavaScript and React experience
- AWS and Docker knowledge
- REST API development
- Version control with Git

The ideal candidate will have 3+ years of experience in full-stack development.
"""

# Make request to backend
url = 'http://localhost:5000/analyze'
data = {
    'resume_text': test_resume,
    'job_description': test_job_description
}

try:
    response = requests.post(url, data=data)
    result = response.json()
    
    print("Response Status:", response.status_code)
    print("\nAnalysis Results:")
    print(json.dumps(result, indent=2))
    
    if response.status_code == 200:
        print("\n✓ Backend is working correctly!")
    else:
        print("\n✗ Backend returned an error")
        
except requests.exceptions.ConnectionError:
    print("✗ Could not connect to backend at http://localhost:5000")
    print("Make sure the Flask server is running:")
    print("  cd backend && .\\venv\\Scripts\\python.exe app.py")
except Exception as e:
    print(f"✗ Error: {str(e)}")
