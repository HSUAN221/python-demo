"""
OpenAI Demo
# pip install langchain
# pip install openai
"""
import os
import openai
import demo
from langchain.llms import OpenAI

OPENAI_API_KEY = "MY KEY"
r = demo.add(2.5, 10)
print(r)

# Demo: use openai.Completion.create
openai.api_key = OPENAI_API_KEY
# temperature 代表生成文本的隨機度
response = openai.Completion.create(
  model="code-davinci-002",
  prompt="##### Fix bugs in the below function\n \n### Buggy Python\n \
  import Random\n \
  a = random.randint(1,12)\n \
  b = random.randint(1,12)\n \
  for i in range(10):\n \
      question = \"What is \"+a+\" x \"+b+\"? \"\n \
      answer = input(question)\n \
      if answer = a*b\n \
            print (Well done!)\n \
      else:\n \
            print(\"No.\")\n  \
  \n### Fixed Python",
  temperature=0,
  max_tokens=182,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["###"]
)
completed_text = response['choices'][0]['text']
print(completed_text)

# Topic: We could use GPT-3 to build a bot that could answer basic technical questions about Moldex3D.
# use langchain
# https://community.openai.com/t/using-a-specific-knowledge-base-with-gpt/24440/7
# https://dagster.io/blog/chatgpt-langchain?utm_source=pocket_reader
# https://weaviate.io/
# https://docs.cohere.ai/docs/prompt-engineering
# https://github.com/hwchase17/langchain
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

