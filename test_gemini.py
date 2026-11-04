from app.services.llm import ask_gemini

answer = ask_gemini("Say hello to VoteReady in one short sentence.")
print(answer)
