import spacy
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re


def _ensure_nltk_resource(path, package):
    try:
        nltk.data.find(path)
    except LookupError:
        nltk.download(package, quiet=True)


_ensure_nltk_resource('corpora/stopwords', 'stopwords')
_ensure_nltk_resource('tokenizers/punkt', 'punkt')


def _load_spacy_model():
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        print("Warning: spaCy model 'en_core_web_sm' not found. Using keyword-only matching.")
        return None


nlp = _load_spacy_model()

COMMON_SKILLS = {
    'python', 'java', 'javascript', 'typescript', 'c++', 'sql', 'html', 'css', 'react',
    'node.js', 'nodejs', 'node', 'machine learning', 'data analysis', 'project management',
    'agile', 'scrum', 'aws', 'docker', 'git', 'linux', 'rest api', 'tensorflow', 'pytorch',
    'excel'
}


def extract_keywords(text):
    """
    Extract keywords from text using NLTK.

    Args:
        text (str): Input text

    Returns:
        set: Set of keywords
    """
    stop_words = set(stopwords.words('english'))
    try:
        words = nltk.word_tokenize(text.lower())
    except LookupError:
        words = re.findall(r"[A-Za-z0-9]+", text.lower())

    keywords = {
        word
        for word in words
        if word.isalnum() and word not in stop_words and len(word) > 2
    }
    return keywords


def extract_skills(text):
    """
    Extract skills from text using spaCy and a curated skills list.

    Args:
        text (str): Input text

    Returns:
        set: Set of skills
    """
    text_lower = re.sub(r"\s+", " ", text.lower()).strip()
    skills = set()

    for skill in COMMON_SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"
        if re.search(pattern, text_lower):
            skills.add(skill)

    if nlp:
        doc = nlp(text_lower)
        for ent in doc.ents:
            ent_text = ent.text.lower()
            if ent_text in COMMON_SKILLS:
                skills.add(ent_text)

    return skills


def calculate_similarity(text1, text2):
    """
    Calculate cosine similarity between two texts using TF-IDF.

    Args:
        text1 (str): First text
        text2 (str): Second text

    Returns:
        float: Similarity score (0-1)
    """
    if not text1 or not text2:
        return 0.0

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return float(similarity)


def analyze_resume(resume_text, job_desc):
    """
    Analyze resume against job description.

    Args:
        resume_text (str): Resume content
        job_desc (str): Job description

    Returns:
        dict: Analysis results
    """
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_desc)
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)

    if job_keywords:
        keyword_match = len(resume_keywords & job_keywords) / len(job_keywords)
    else:
        keyword_match = 0.0

    semantic_sim = calculate_similarity(resume_text, job_desc)
    ats_score = 0.5 * keyword_match + 0.5 * semantic_sim

    missing_keywords = sorted(job_keywords - resume_keywords)
    matching_skills = sorted(resume_skills & job_skills)

    suggestions = []
    if missing_keywords:
        suggestions.append(
            f"Add missing keywords: {', '.join(missing_keywords[:8])}"
        )
    if not matching_skills:
        suggestions.append("Highlight relevant skills in your resume.")
    if ats_score < 0.5:
        suggestions.append("Align your experience bullets with the job requirements.")
    suggestions.append("Tailor your resume to match the job description more closely.")

    feedback = {
        'skills': (
            f"Matching skills: {', '.join(matching_skills) if matching_skills else 'None found'}. "
            "Consider adding more relevant skills."
        ),
        'experience': "Ensure your experience section quantifies achievements.",
        'education': "Verify education requirements are met."
    }

    return {
        'ats_score': round(ats_score * 100, 2),
        'missing_keywords': missing_keywords,
        'matching_skills': matching_skills,
        'suggestions': suggestions,
        'feedback': feedback
    }
