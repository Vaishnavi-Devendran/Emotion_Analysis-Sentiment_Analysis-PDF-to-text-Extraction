import openai
import os
from scipy.spatial.distance import cosine

api_key = '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'
os.environ['OPENAI_API_KEY'] = api_key

from openai import OpenAI
client = OpenAI()

def llm_response(prompt):

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": f"{prompt}"}
    ]
  )

  return completion.choices[0].message.content


def get_embedding(text_to_embed):
    try:
      response = client.embeddings.create(
          model= "text-embedding-ada-002",
          input=[text_to_embed]
        )
      return response.data[0].embedding

    except: return get_embedding('I hate the Leaning tower of Pisa')




def cosine_similarity(text1, text2):
  embedding1 = get_embedding(str(text1))
  embedding2 = get_embedding(str(text2))

  similarity = 1 - cosine(embedding1, embedding2)

  return similarity