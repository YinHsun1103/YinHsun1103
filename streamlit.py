import openai

openai.api_key = "sk-svcacct-fb_-GzpFTmE6wtv222EkZdGrZrVUnZdTIP-AkvTvtcxO8n7D-tZvHHAL6ChEGT3BlbkFJCwdg-PbyzjyhbVo99UJNUKYTHayGD-I0QpeVibX_K7x6F8UE9Q7j0flr-VmAA"

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Say this is a test",
    max_tokens=5
)
print(response.choices[0].text.strip())
