# chains/screening_chain.py
# Modular LangChain pipeline using Groq (Stable + Clean Output)

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

from prompts.prompt_templates import (
    skill_extraction_prompt,
    matching_prompt,
    scoring_prompt,
    explanation_prompt
)

# --------------------------------------------------
# ✅ GROQ LLM (BEST CHOICE)
# --------------------------------------------------

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

parser = StrOutputParser()

# --------------------------------------------------
# Chains (LCEL)
# --------------------------------------------------

extraction_chain = skill_extraction_prompt | llm | parser
matching_chain = matching_prompt | llm | parser
scoring_chain = scoring_prompt | llm | parser
explanation_chain = explanation_prompt | llm | parser

# --------------------------------------------------
# Pipeline
# --------------------------------------------------

def run_screening_pipeline(resume: str, job_description: str) -> dict:

    extracted_info = extraction_chain.invoke({"resume": resume})
    print("✅ Step 1 Complete: Skill Extraction")

    match_result = matching_chain.invoke({
        "extracted_info": extracted_info,
        "job_description": job_description
    })
    print("✅ Step 2 Complete: Matching")

    score_output = scoring_chain.invoke({
        "match_result": match_result,
        "job_description": job_description
    })
    print("✅ Step 3 Complete: Scoring")

    explanation = explanation_chain.invoke({
        "score": score_output,
        "match_result": match_result,
        "extracted_info": extracted_info
    })
    print("✅ Step 4 Complete: Explanation\n")

    return {
        "extracted_info": extracted_info,
        "match_result": match_result,
        "score": score_output,
        "explanation": explanation
    }