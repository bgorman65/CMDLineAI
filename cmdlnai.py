import sys
import openai
# Gathering Key from file
API_Key = open("API_KEY", "r").read()
openai.api_key = API_Key
# Gathering command line arguments and converting them into a string to pass into openAI
ArgLen = len(sys.argv)
cmdInput = ""
for i in range(1, ArgLen):
    cmdInput += sys.argv[i]
    cmdInput += " "
# Creating the first prompt and printing out the response
cmdResponse = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{"role": "user", "content": cmdInput}]
)
print("Anwer: " + cmdResponse["choices"][0]["message"]["content"])
# Creating a loop to continue asking questions if needed
while True:
    print("\n|||||Enter another question or enter QUIT to stop|||||\n")
    userInput = input()
    if userInput == "QUIT":
        break
    else:
        userResponse = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [{"role": "user", "content": userInput}]
        )
        print("Anwer: " + userResponse["choices"][0]["message"]["content"])