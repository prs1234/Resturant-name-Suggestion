import os
from dotenv import load_dotenv
from key import GOOGLE_API_KEY

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain

load_dotenv()

# ✅ Define the LLM globally
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY
)

def generate_restaruant_name(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template='I want to open a restaurant for {cuisine} food. Suggest a fancy name for this. Only one name please.'
    )
    chain_name = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_description = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest 10 creative menu item names for a restaurant called '{restaurant_name}'. Only return a simple numbered list without descriptions."
    )
    chain_description = LLMChain(llm=llm, prompt=prompt_description, output_key="menu")

    # Run first chain to get restaurant name
    restaurant_name_result = chain_name.invoke({"cuisine": cuisine})
    restaurant_name = restaurant_name_result["restaurant_name"].strip().strip('"').strip("'")

    # Run second chain to get menu
    menu_result = chain_description.invoke({"restaurant_name": restaurant_name})
    menu = menu_result["menu"]

    return {
        "cuisine": cuisine,
        "restaurant_name": restaurant_name,
        "menu_items": menu
    }

if __name__ == "__main__":
    cuisine_input = "Indian"
    output = generate_restaruant_name(cuisine_input)
    print("\n🎉 Output:\n", output)
