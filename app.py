from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import tempfile
from resume_parser import parse_resume
from nlp_utils import analyze_resume

app = Flask(__name__)
CORS(app)


def _get_request_payload():
    if request.is_json:
        data = request.get_json(silent=True) or {}
        return {
            "job_description": (data.get("job_description") or "").strip(),
            "resume_text": (data.get("resume_text") or "").strip(),
        }

    return {
        "job_description": (request.form.get("job_description") or "").strip(),
        "resume_text": (request.form.get("resume_text") or "").strip(),
    }


@app.route('/analyze', methods=['POST'])
def analyze():
    """
    Analyze resume against job description.

    Expects:
    - file: PDF resume (optional)
    - resume_text: Text resume (optional)
    - job_description: Text job description (required)
    """
    try:
        payload = _get_request_payload()
        job_desc = payload["job_description"]
        if not job_desc:
            return jsonify({'error': 'Job description is required'}), 400

        resume_text = None
        if 'file' in request.files:
            file = request.files['file']
            if file.filename:
                with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
                    file.save(temp_file.name)
                    resume_text = parse_resume(file_path=temp_file.name)
                os.unlink(temp_file.name)
        elif payload["resume_text"]:
            resume_text = payload["resume_text"]
        else:
            return jsonify({'error': 'Resume file or text is required'}), 400

        if not resume_text:
            return jsonify({'error': 'Could not parse resume'}), 400

        result = analyze_resume(resume_text, job_desc)
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
