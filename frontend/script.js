document.getElementById('analyzeForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const formData = new FormData();
    const fileInput = document.getElementById('resumeFile');
    const resumeText = document.getElementById('resumeText').value.trim();
    const jobDesc = document.getElementById('jobDesc').value.trim();

    if (!jobDesc) {
        alert('Please enter a job description.');
        return;
    }

    if (fileInput.files.length > 0) {
        formData.append('file', fileInput.files[0]);
    } else if (resumeText) {
        formData.append('resume_text', resumeText);
    } else {
        alert('Please upload a resume file or paste resume text.');
        return;
    }

    formData.append('job_description', jobDesc);

    try {
        const response = await fetch('http://localhost:5000/analyze', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (response.ok) {
            displayResults(result);
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        alert('Error: ' + error.message);
    }
});

function displayResults(result) {
    document.getElementById('results').style.display = 'block';

    // Score
    const score = result.ats_score;
    document.getElementById('scoreBar').style.width = score + '%';
    document.getElementById('scoreBar').textContent = score + '%';
    document.getElementById('scoreText').textContent = `ATS Match Score: ${score}%`;

    // Missing Keywords
    document.getElementById('missingKeywords').textContent = result.missing_keywords.join(', ') || 'None';

    // Matching Skills
    document.getElementById('matchingSkills').textContent = result.matching_skills.join(', ') || 'None';

    // Suggestions
    const suggestionsList = document.getElementById('suggestions');
    suggestionsList.innerHTML = '';
    result.suggestions.forEach(suggestion => {
        const li = document.createElement('li');
        li.textContent = suggestion;
        suggestionsList.appendChild(li);
    });

    // Feedback
    const feedbackDiv = document.getElementById('feedback');
    feedbackDiv.innerHTML = '';
    for (const [section, feedback] of Object.entries(result.feedback)) {
        const p = document.createElement('p');
        p.innerHTML = `<strong>${section.charAt(0).toUpperCase() + section.slice(1)}:</strong> ${feedback}`;
        feedbackDiv.appendChild(p);
    }
}

document.getElementById('downloadBtn').addEventListener('click', function() {
    const suggestions = Array.from(document.querySelectorAll('#suggestions li')).map(li => li.textContent).join('\n');
    const blob = new Blob([suggestions], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'resume_suggestions.txt';
    a.click();
    URL.revokeObjectURL(url);
});