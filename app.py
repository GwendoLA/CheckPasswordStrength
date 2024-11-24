from flask import Flask, request, jsonify, render_template

app = Flask(__name__)  # creates an instance of flask 

def load_common_words(): # Pull most common english and french words
    common_words = set()
    with open("./data/most-common-english.txt", "r") as file:
        common_words.update(line.strip().lower() for line in file)
    with open("./data/most-common-french.txt", "r") as file:
         common_words.update(line.strip().lower() for line in file)
    return common_words

def check_password_strength(password, name, surname): # the password check itself

    common_words = load_common_words()

    score = 4
    improvements = []

    if len(password) < 6 : 
        improvements.append("Password is too short (less than 6 characters)")
        score -= 3
    if len(password) > 6 and len(password) < 12: 
        improvements.append(f"{len(password)} characters is good but consider using a password with at least 12 characters")
        score += 1
    if len(password)>= 12 :
        score += 2
    if not any(char.isupper() for char in password):
        improvements.append("Use uppercase characters")
        score -= 1
    if not any(char.islower() for char in password):
        improvements.append("Use lowercase characters")
        score -= 1
    if not any(char.isdigit() for char in password):
        improvements.append("Add digits to your password")
        score -= 1
    if not any(char in "!@#$%^&*()_+" for char in password):
        improvements.append("Use special characters, such as !@#$%^&*()_+")
        score -= 1
    if any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(char in "!@#$%^&*()_+" for char in password):
        score += 2
    if (name.lower() in password.lower()) or (surname.lower() in password.lower()):
        improvements.append("Avoid including your name in your password")
        score -= 1 
    for word in common_words:
        if word in password.lower():
            improvements.append(f"Avoid using common words such as '{word}' in your password")
            score -= 1
            break


    percent_score = max(0, min(score * 12.5, 100))  # Score 0-100%, maximum of 8 points so x12.5 to have it in %

    if percent_score < 20:
        strength = "Very Weak"
    elif percent_score < 40:
        strength = "Weak"
    elif percent_score < 60:
        strength = "Okay"
    elif percent_score < 80:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        "strength": strength,
        "improvements": improvements
    }

@app.route("/")
def index():
    return render_template("index.html") 


@app.route("/check-password", methods=["POST"]) # page called to check the password
def check_password():
    data = request.json
    password = data.get("password", "")
    name = data.get("name", "")
    surname = data.get("surname", "")
    result = check_password_strength(password, name, surname)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)  
