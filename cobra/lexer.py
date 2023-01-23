import parser_1

with open("main.cb", "r") as f:
    lines = f.read()

    text = lines.strip()

result, error = parser_1.run("main.cb", text)

if error:
    print(error.as_string())
else:
    print(result)
