from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from extractors.llm_provider import get_llm
from dotenv import load_dotenv

load_dotenv()

# The prompt template
EXTRACTION_PROMPT = ChatPromptTemplate.from_template("""
You are a data extraction expert. Your job is to extract customer information from business documents.

Here is the document content:
{document_content}

Extract all customer/company information you can find and return it as a JSON array.
Each customer object must have these fields:
- company_name: the name of the company or organization
- email: billing or contact email address
- country: country name or code
- industry: business industry or sector
- status: "active" or "churned" (if not clear, use "active")
- joined_at: date they became a customer (YYYY-MM-DD format, null if not found)

Rules:
- Return ONLY a valid JSON array, nothing else
- No explanation, no markdown, no code blocks
- If a field is not found, use null
- If multiple customers found, include all of them

Example output:
[
  {{
    "company_name": "TechCorp Inc",
    "email": "billing@techcorp.com",
    "country": "US",
    "industry": "SaaS",
    "status": "active",
    "joined_at": "2024-01-15"
  }}
]
""")

def extract_with_ai(document_content: str, provider: str = "groq") -> list[dict]:
    """
    Use LangChain + LLM to extract customer data from raw text.
    Returns a list of customer dictionaries.
    """
    llm = get_llm(provider)
    parser = JsonOutputParser()

    #creating the chain prompt + LLM + parser
    chain = EXTRACTION_PROMPT | llm | parser

    print(f"Sending to {provider} for extraction...")

    result = chain.invoke({"document_content": document_content})

    print(f"AI extracted {len(result)} customer(s)")
    return result