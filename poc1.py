from openai import OpenAI

client = OpenAI(
    api_key="sk-proj-xxxxxxxx"
)
message_history=[
    {"role":"system","content":"you are vega, an AI model created by openAI.you are helpful to people find an answer."}
]
def reply(question):
    message_history.append({"role":"user","content":question})
    responses = client.responses.create(
        model="gpt-5-nano",
        input=message_history
    )
    vega_reply=responses.output_text
    message_history.append({"role":"assistant","content":vega_reply})
    return vega_reply

print("Vega is Ready to Give you answer! (exit to quit the chat)")

while True:
    user = input("User: ")

    if user.lower() == "exit":
        print("Vega: Bye.have a nice day!")
        break

    answer = reply(user)
    print("Vega:", answer)