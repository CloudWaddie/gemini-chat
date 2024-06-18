import google.generativeai as genai

api_key = input("API Key: ")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

chat_session = model.start_chat(history=[])

while True:
  try:
    question = input("Question: ")
    if question != "":
      response = chat_session.send_message(question)
      print(response.text)
  except KeyboardInterrupt:
    print("Exiting...")
    break
