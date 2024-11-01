# api/routes/health.py
from fastapi import APIRouter

router = APIRouter()

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFaceHub
repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

llm = HuggingFaceHub(
        repo_id=repo_id,
        task="text-generation",
        model_kwargs={
            "max_new_tokens": 512,
            "top_k": 30,
            "temperature": 0.1,
            "repetition_penalty": 1.03,
        },
        huggingfacehub_api_token='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',
    )


@router.get("/")
async def health_check():
    input_text = "from the "
    # Generate a response
    response = llm.generate([input_text])

    # Extract the generated answer
    generated_text = response.generations[0][0].text.strip()

    # Print the extracted answer
    print(generated_text)
    return generated_text
