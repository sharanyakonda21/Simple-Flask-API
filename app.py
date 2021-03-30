from flask import Flask, request, jsonify
import re

app = Flask("__name__")


@app.route("/v1/sanitized/input", methods=["POST"])
def check_sql_injection():
    body = request.json
    
    if not body:
        return "Invalid JSON in request", 400
    
    payload = body.get("payload")
    if not payload:
        return "JSON must contain payload field", 400
    
    status = "unsanitized" # default status

    escape_sequences = [
        r"\0",
        r"\'",
        r"\"",
        r"\b",
        r"\n",
        r"\r",
        r"\t",
        # r"\Z", not a valid injection character
        r"\\",
        r"\%",
        r"\_",
    ]
    
    pattern_string = f"[{''.join(escape_sequences)}]+?" # non-greedy 
    found = re.search(pattern_string, payload)
    
    print("SQL Injection found:\t", found)
    if not found:
        status = "sanitized"

    return jsonify(result=status)
