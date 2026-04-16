# main.py
# Entry point — runs screening pipeline for all 3 resumes


import os
os.environ["LANGCHAIN_PROJECT"] = "resume-screening"

import os
from dotenv import load_dotenv

load_dotenv()

from data.resumes import JOB_DESCRIPTION, STRONG_RESUME, AVERAGE_RESUME, WEAK_RESUME
from chains.screening_chain import run_screening_pipeline

# --------------------------------------------------
# Candidate Labels
# --------------------------------------------------
candidates = [
    ("Strong Candidate – Aisha Sharma", STRONG_RESUME),
    ("Average Candidate – Ravi Mehta", AVERAGE_RESUME),
    ("Weak Candidate – Priya Patil", WEAK_RESUME),
]

# --------------------------------------------------
# Helper (clean output)
# --------------------------------------------------
def clean(text):
    return text.strip() if text else "No output"

# --------------------------------------------------
# Run Pipeline
# --------------------------------------------------
def main():
    print("=" * 60)
    print("   AI RESUME SCREENING SYSTEM")
    print("   Powered by LangChain + LangSmith")
    print("=" * 60)

    for label, resume in candidates:
        print(f"\n{'=' * 60}")
        print(f"  Processing: {label}")
        print(f"{'=' * 60}")

        result = run_screening_pipeline(resume, JOB_DESCRIPTION)

        print(f"\n📋 EXTRACTED INFO:\n{clean(result['extracted_info'])}")
        print(f"\n🔗 MATCH ANALYSIS:\n{clean(result['match_result'])}")
        print(f"\n🎯 SCORE:\n{clean(result['score'])}")
        print(f"\n💬 EXPLANATION:\n{clean(result['explanation'])}")

        print("\n" + "-" * 60)


if __name__ == "__main__":
    main()