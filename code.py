from js import XMLHttpRequest as X
import json

def ask(q):
    x = X.new()
    x.open("POST", "https://api.groq.com/openai/v1/chat/completions", False)
    x.setRequestHeader("Content-Type", "application/json")
    x.setRequestHeader("Authorization", "Bearer gsk_eQZX5fpIKjwws2siXcOdWGdyb3FYo5UgyGRRmFS92S77NO5nt09-(p)")
    x.send(json.dumps({"model":"llama-3.3-70b-versatile","messages":[{"role":"user","content":f"Python code only no backticks no markdown no explanation: {q}"}],"max_tokens":200,"temperature":0}))
    c = json.loads(x.responseText)["choices"][0]["message"]["content"].strip()
    return c.split("\n",1)[1].rsplit("```",1)[0].strip() if c.startswith("```") else c

code = ask("take two numbers as input and print their sum")
print(code)
