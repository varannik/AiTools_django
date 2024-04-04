"""
LangChain pipeline for generating tags for a URL
"""

import os
os.environ['OPENAI_API_KEY'] = "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"



import time 
from .driver import createDriver, soupParser
from .extractor import GetDefinedTags, GetDefinedPricingLabels, GetDefinedPlatforms

from unstructured.cleaners.core import clean
from langchain.chains import create_structured_output_runnable
from langchain_openai import ChatOpenAI




def outputSchema (data):
    '''Return define output schema for langchain'''
    properties = {}
    required = []

    if data['short_description'] == True:
        properties.update({
            
            "short_description": {
                        "description": "A 150 character SEO-friendly description",
                        "type": "string"
            },

        })
        required.append('short_description')

    if data['review'] == True:
        properties.update({
            
            "review": {
                "description": "A full SEO-friendly description, which contains answers to these questions:[what is this website/app? What is its use?]. A descriptive writing style. A formal tone. Maximum 600 words.",
                "type": "string"
            },

        })
        required.append('review')

    if data['pricing'] == True:
        pricing_options = GetDefinedPricingLabels()
        properties.update({
            
            "pricing": {
                "description": "All Available pricing options",
                "type": "array",
                "enum": pricing_options,
                "multiple": True
            },

        })
        required.append('pricing')

    if data['topic_selection'] == True:
        tags = GetDefinedTags()
        properties.update({

            "topic_selection": {
                "description": "All relative tags that demonstrate the use cases of the tool",
                "type": "array",
                "enum": tags,
                "multiple": True
            },
        })
        required.append('topic_selection')

    if data['platform'] == True:
        platforms = GetDefinedPlatforms()
        properties.update({

            "platform": {
                "description": "All Supported platforms",
                "type": "array",
                "enum": platforms,
                "multiple": True
            },
        })
        required.append('platform')

    if data['lunch_date'] == True:

        properties.update({

            "lunch_date": {
                "description": "Lunch date tool",
                "type": "string",
            }
        })
        required.append('lunch_date')

    schema = {
        "type": "function",
        "function": {
            "name": "tool_tagging",
            "description": "Summarize some information about an AI tool",
            "parameters": {
                "type": "object",
                "properties": properties,
                "required": required,
            }
        }
    }
    return schema


def generate_document(url):
  '''Given an URL, return a langchain Document to futher processing"'''
  # Open target site and
  URL_TARGET = url
  URL_SELENIUM="http://172.19.0.12:4444/wd/hub"  #chrome-2

  driver = createDriver(URL_TARGET, URL_SELENIUM)
  
  driver.get(url)
  time.sleep(2)

  soup = soupParser(driver)

  text_data = ''
  for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'div']):
      text_data += clean(tag.get_text(),      
                          extra_whitespace= True,
                          dashes= True,
                          bullets= True,
                          trailing_punctuation= True,
                          lowercase= True)

  text_data = text_data[:5000]
#   print(text_data)
  driver.quit()
  return text_data


def SORLLM(data):
    '''Create structured output runnable to call function in OpenAI'''
    doc_schema = outputSchema(data)

    llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
    structured_llm = create_structured_output_runnable(
        doc_schema,
        llm,
        mode="openai-tools",
        enforce_function_usage=True,
        return_single=True,
    )
    result = structured_llm.invoke(generate_document(data['URL']))
    result['URL'] = data['URL']
    return result