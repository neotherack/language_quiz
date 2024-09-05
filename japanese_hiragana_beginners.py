import ollama

MODEL1 = "llama3.1:latest"
commands1 = ["Say one vocabulary word in ingles which matches to a basic japanese vocabulary.", \
           "Only the word, no other additional info nor explanations nor comments.", \
           "Do not translate it, just the word in english."]

PROMPT1 = "".join(commands1)
response1 = ollama.generate(model=MODEL1, prompt=PROMPT1, stream=False)
print(f"{response1['response']}")


MODEL2 = "gemma2:latest"
commands2 = ["Create a quiz, one question and four choice possible answers.", \
            "One of the wrong answers should be funny or a joke.", \
            "Topic is japanese-english vocabulary and verb translation, level should be japanese for beginners.", \
           f"The vocabulary word is '{response1['response']}', keep it in english, use ONLY hiragana for the answers", \
            "'<<' and '>>' are placeholders where to place your choice answers", \
            "Do not reply other than pure JSON like this:", \
            "{\"question\":\"Meaning of <<vocabulary word>> ?\", " \
            "\"choices\":{\"a\":\"<<hiragana 1>>\",\"b\":\"<<hiragana 2>>\",\"c\":\"<<hiragana 3>>\",\"d\":\"<<hiragana 4>>\"}, " \
            "\"answer\":\"<correct answer letter>\",\"funny\":\"<funny answer letter>\"}"]

PROMPT2 = "".join(commands2)
response2 = ollama.generate(model=MODEL2, prompt=PROMPT2, stream=False)
print(f"{response2['response']}")
