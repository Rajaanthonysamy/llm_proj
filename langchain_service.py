import os
from secret_key import openapi_key
from langchain_openai import OpenAI
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"]=openapi_key

llm=OpenAI(temperature=0.1)



def generate_restaurant_name_and_items(cuisine):
    print("Method call")
    promt_template_name = PromptTemplate(
        input_var=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this"
    )

    name_chain = LLMChain(llm=llm, prompt=promt_template_name, output_key="restaurant")

    promt_template_item = PromptTemplate(
        input_var=["restaurant"],
        template="Suggest me some food menu for {restaurant}. Return as a comma seperated list"
    )

    food_item_chain = LLMChain(llm=llm, prompt=promt_template_item, output_key="menu_items")
    seq_chain = SequentialChain(
        chains=[name_chain, food_item_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant", "menu_items"]
    )
    response=seq_chain({'cuisine': cuisine})
    return response