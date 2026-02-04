import google.generativeai as genai
genai.configure(api_key="AIzaSyAJJX3lYKv5JiISoJnJP02z_5Gfs1pFgYo")
model = genai.GenerativeModel("gemini-pro")

store = ""
def reply(ask):
    global store
    store = store + "User : " + ask + "\n"

    output = model.generate_content(store)
    answer = output.text

    store += f"Jenny: {answer}\n"
    return answer

while True:
    user = input("User: ")
    if user =="exit":
        break
    answer = reply(user)
    print("Jenny:", answer)