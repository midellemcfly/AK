from flask import Flask, request, render_template_string

app = Flask(__name__)

SECRET_ANSWER = "banana pancakes"  # change to your inside joke (lowercase!)

PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>💖 A Surprise for You 💖</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #ffd6e8, #fff1f7);
            text-align: center;
            padding-top: 80px;
        }
        input {
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
            width: 250px;
        }
        button {
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            background-color: #ff4d88;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }
        .card {
            background: white;
            display: inline-block;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }
        .error { color: #ff4d88; }
    </style>
</head>
<body>
    <div class="card">
        <h1>💌 Hi, my love 💌</h1>
        <p>Answer this to unlock your surprise:</p>
        <p><i>What do we always order together?</i></p>

        <form method="POST">
            <input name="answer" placeholder="Type your answer..." required />
            <br><br>
            <button type="submit">Unlock 💖</button>
        </form>

        {% if error %}
            <p class="error">{{ error }}</p>
        {% endif %}
    </div>
</body>
</html>
"""

SECRET_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>🎉 Surprise 🎉</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            background: #fff0f6;
            padding-top: 100px;
        }
    </style>
</head>
<body>
    <h1>🎂 Happy Birthday, My Favorite Human 🎂</h1>
    <p>You did it 💕</p>
    <p>
        I love you more than coffee in the morning,<br>
        more than naps on Sundays,<br>
        and more than anything 💖
    </p>
    <p>Here’s to many more banana pancakes together 🥞</p>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_answer = request.form["answer"].lower().strip()
        if user_answer == SECRET_ANSWER:
            return render_template_string(SECRET_PAGE)
        else:
            return render_template_string(PAGE, error="Hmm… that’s not it 👀 Try again 💕")

    return render_template_string(PAGE)

if __name__ == "__main__":
    app.run(debug=True)