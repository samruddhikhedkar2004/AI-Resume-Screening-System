from langchain_core.prompts import PromptTemplate

# --------------------------------------------------
# Step 1: Skill Extraction
# --------------------------------------------------
skill_extraction_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
Instruction: Extract key details from the resume.

Resume:
{resume}

Output:
Skills:
Tools:
Experience:
Domain:

Answer only with the output. Do not repeat the resume.
"""
)

# --------------------------------------------------
# Step 2: Matching
# --------------------------------------------------
matching_prompt = PromptTemplate(
    input_variables=["extracted_info", "job_description"],
    template="""
Instruction: Compare candidate with job description.

Candidate:
{extracted_info}

Job:
{job_description}

Output:
Matched:
Missing:

Answer only with the output.
"""
)

# --------------------------------------------------
# Step 3: Scoring
# --------------------------------------------------
scoring_prompt = PromptTemplate(
    input_variables=["match_result", "job_description"],
    template="""
Instruction: Give a score between 0 and 100.

Match:
{match_result}

Output:
Score: <number>

Only return score.
"""
)

# --------------------------------------------------
# Step 4: Explanation
# --------------------------------------------------
explanation_prompt = PromptTemplate(
    input_variables=["score", "match_result", "extracted_info"],
    template="""
Instruction: Explain the score in simple terms.

Score: {score}
Match: {match_result}

Output:
<short explanation>

Do not repeat input.
"""
)