from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the machine learning model
model = joblib.load('loan_approval_random_forest_model.pkl')

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/prediction', methods=['POST'])
def predict():
    # Get input data from the form

    input_data = request.form.to_dict()
    input_data = list(input_data.values())

    # Make predictions using the model
    prediction = model.predict([input_data])

    return render_template('prediction_result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


