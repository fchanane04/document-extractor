import os
from dotenv import load_dotenv

load_dotenv()

def get_llm(provider: str = None):
    # Use default provider from .env if none specified
    if provider is None:
        provider = os.getenv("DEFAULT_PROVIDER", "groq")

    if provider == "groq":
        from langchain_groq import ChatGroq
        return ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=0  # 0 = consistent, deterministic output
        )

    elif provider == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(
            model="gpt-4o",
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0
        )

    elif provider == "anthropic":
        from langchain_anthropic import ChatAnthropic
        return ChatAnthropic(
            model="claude-3-5-sonnet-20241022",
            api_key=os.getenv("ANTHROPIC_API_KEY"),
            temperature=0
        )

    else:
        raise ValueError(f"Unknown provider: {provider}. Choose: groq, openai, anthropic")