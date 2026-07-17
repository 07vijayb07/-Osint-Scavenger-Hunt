from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from data import challenges
import os

app = Flask(__name__)
CORS(app)
# =========================
# HOME ROUTE
# =========================
@app.route("/")
def home():

    return "OSINT Backend Running Successfully"
# =========================
# IMAGE FOLDER
# =========================
IMAGE_FOLDER = os.path.join(app.root_path, "static/images")


# =========================
# GET ALL CHALLENGES
# =========================
@app.route("/api/challenges")
def get_challenges():
    return jsonify(challenges)


# =========================
# GET SINGLE CHALLENGE
# =========================
@app.route("/api/challenges/<int:id>")
def get_challenge(id):

    for challenge in challenges:

        if challenge["id"] == id:
            return jsonify(challenge)

    return jsonify({
        "error": "Challenge not found"
    }), 404


# =========================
# SERVE IMAGES
# =========================
@app.route("/images/<path:filename>")
def get_image(filename):

    return send_from_directory(
        IMAGE_FOLDER,
        filename
    )


# =========================
# SUBMIT ANSWER
# =========================
@app.route("/api/submit-answer", methods=["POST"])
def submit_answer():

    data = request.get_json()

    challenge_id = data.get("challengeId")
    user_answer = data.get("answer", "").strip().lower()

    for challenge in challenges:

        if challenge["id"] == challenge_id:

            correct_answer = challenge["answer"]

            # MULTIPLE ANSWERS SUPPORT
            if isinstance(correct_answer, list):

                is_correct = user_answer in [
                    ans.strip().lower()
                    for ans in correct_answer
                ]

            else:

                is_correct = (
                    user_answer
                    == correct_answer.strip().lower()
                )

            return jsonify({

                "correct": is_correct,

                "correctAnswer": correct_answer,

                "pointsEarned": (
                    challenge["points"]
                    if is_correct
                    else 0
                ),

                "message": (
                    "Correct answer! Well done."
                    if is_correct
                    else "Incorrect answer. Try again."
                )

            })

    return jsonify({
        "error": "Challenge not found"
    }), 404


# =========================
# RUN APP
# =========================
if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5007
    )