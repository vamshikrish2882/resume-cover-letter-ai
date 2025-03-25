def resume_prompt(job_description, experience_summary):
    return f"""
You are a professional resume writer.
Create a customized resume summary for this job:

Job Description:
{job_description}

Candidate Experience:
{experience_summary}

Output a 4-5 sentence resume summary tailored to the job.
"""

def cover_letter_prompt(job_description, experience_summary):
    return f"""
You are a professional cover letter writer.
Write a personalized cover letter based on the following:

Job Description:
{job_description}

Candidate Experience:
{experience_summary}

The tone should be confident and enthusiastic. Keep it concise.
"""
