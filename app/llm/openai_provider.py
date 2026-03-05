from openai import OpenAI
from app.core.config import settings


class OpenAIProvider:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_llm_model

    def generate(self, query: str, context_chunks: list[dict]) -> str:
        context_text = self._build_context(context_chunks)

        prompt = f"""
You are a domain-specific assistant.

Answer the question using ONLY the provided context.

For every factual statement, cite like this:
[Source: <source>, Page: <page>]

If the answer is not in the context, say:
"I cannot find this information in the provided documents."

Context:
{context_text}

Question:
{query}

Answer:
"""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.2,
            messages=[
                {"role": "system", "content": "You are a precise and factual assistant."},
                {"role": "user", "content": prompt}
            ],
        )

        return response.choices[0].message.content

    def _build_context(self, chunks: list[dict]) -> str:
        formatted_chunks = []

        for chunk in chunks:
            formatted_chunks.append(
                f"""
Source: {chunk['source']}
Page: {chunk['page']}
Content:
{chunk['text']}
"""
            )

        return "\n---\n".join(formatted_chunks)