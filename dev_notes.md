Main features:

- Interviewer
- Candidate
- Job
- Applications
- Interview
- Interview report
- Candidate dashboard
- Interviewer dashboard

### Schemas (Proposed)

Users:

- id (PK)
- name
- email (unique)
- phone
- password_hash
- role (ENUM: 'candidate', 'recruiter', 'admin')
- created_at

candidate_profiles

- id (PK)
- user_id (FK)
- resume_url
- experience_years
- current_company
- skills (optional JSON or separate table)
- education

companies

- id (PK)
- name
- website
- description

recruiters

- id (PK)
- user_id (FK)
- company_id (FK)

jobs

- id (PK)
- title
- company_id (FK)
- description
- location
- salary_min
- salary_max
- experience_required
- status (open, closed, draft)
- expiry_date
- created_by (recruiter_id)
- created_at

skills

- id (PK)
- name

job_skills

- job_id (FK)
- skill_id (FK)

candidate_skills

- candidate_id (FK)
- skill_id (FK)

applications

- id (PK)
- job_id (FK)
- candidate_id (FK)
- status (applied, shortlisted, rejected, hired)
- applied_at
- updated_at

interviews

- id (PK)
- application_id (FK)
- round_number
- interviewer_id (FK → users)
- scheduled_at
- duration
- status (scheduled, completed, cancelled)

interview_reports

- id (PK)
- interview_id (FK)
- rating (1-5)
- feedback_text
- strengths
- weaknesses
- recommendation (hire / reject / maybe)
- created_at
