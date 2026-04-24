from flask import Flask, render_template, request

app = Flask(__name__)

volunteers = [
    {"name": "Bhavya", "location": "HAZRATGANJ", "skill": "Medical", "available": True},
    {"name": "Pragati", "location": "MATIYARI", "skill": "Food", "available": True},
    {"name": "Himanshi", "location": "MATIYARI", "skill": "Medical", "available": True},
    {"name": "Swara", "location": "RAJAJIPURAM", "skill": "Rescue", "available": True},
    {"name": "Abhyuday", "location": "MATIYARI", "skill": "Rescue", "available": True},
    {"name": "Nikhil", "location": "RAJAJIPURAM", "skill": "Transport", "available": True},
    {"name": "Utkarsh", "location": "HAZRATGANJ", "skill": "Transport", "available": True},
    {"name": "Harshit", "location": "RAJAJIPURAM", "skill": "Food", "available": True},
    {"name": "Riya", "location": "CHINHAT", "skill": "Medical", "available": True},
]


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/allocate', methods=['POST'])
def allocate ():
    location = request.form['location']
    help_type = request.form['type']
    count = int(request.form['count'])
    urgency = int(request.form['urgency'])

    selected = []

    for v in volunteers:
        if v["available"] and v["skill"] == help_type:
            score = 0

            if v["location"] == location:
                score += 2

            score += urgency

            v["score"] = score
            selected.append(v)

    selected = sorted(selected, key=lambda x: x["score"], reverse=True)
    selected = selected[:count]

    return render_template('result.html', volunteers=selected)
if __name__ == "__main__":
    app.run(debug=True)