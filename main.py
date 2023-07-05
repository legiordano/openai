import openai

openai.api_key = 'api_key'

def get_response(query):
    response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=query,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.7
    )

    answer = response.choices[0].text.strip()

    return answer

user_query = input("Enter your query: ")
model_response = get_response(user_query)
print(model_response)