from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from secret import openai_key

import os
os.environ['OPENAI_API_KEY']=openai_key

llm = ChatOpenAI(
    temperature=0.5, 
    api_key=openai_key, 
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-3.5-turbo"
)

# 1. Chain to generate Restaurant Name
prompt_template_name = PromptTemplate(
    input_variables=['cuisine'],
    template="I want to open a restraunt for {cuisine} food. Suggest one fancy name for this."
)
name_chain = prompt_template_name | llm

# 2. Chain to generate Menu Items
prompt_template_items = PromptTemplate(
    input_variables=['restaurant_name'],
    template="Suggest me some menu items for {restaurant_name}. Return it as a comma separated list."
)
food_items_chain = prompt_template_items | llm

def generate_restaurant_name_items(cuisine):
    # Step 1: Get Name
    response_name = name_chain.invoke({"cuisine": cuisine})
    restaurant_name = response_name.content
    
    # Step 2: Get Menu Items using the result from Step 1
    response_items = food_items_chain.invoke({"restaurant_name": restaurant_name})
    menu_items = response_items.content
    
    return {
        'restaurant_name': restaurant_name.strip(),
        'menu_items': menu_items.strip()
    }
    
if __name__=="__main__":
    print(generate_restaurant_name_items("Indian"))