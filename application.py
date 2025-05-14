from flask import Flask, render_template, request
from pipeline.prediction_pipeline import hybrid_recommendation

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = None
    error = None
    if request.method == 'POST':
        try:
            print(request.form)  # Debug line
            user_id_str = request.form.get('user_id')

            if not user_id_str:
                error = "User ID is required."
            else:
                user_id = int(user_id_str)
                recommendations = hybrid_recommendation(user_id)

        except Exception as e:
            print("Error Occurred", e)
            error = f"Something went wrong: {e}"

    return render_template('index.html', recommendations=recommendations, error=error)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
