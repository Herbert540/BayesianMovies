from flask import Flask, render_template, request
import bp

# Load the pre-trained model
large_classifier = bp.BayesClassifier()
large_classifier.load("large_freqs.json")


# Initialize the Flask application
app = Flask(__name__)



# Define the route for the homepage
@app.route('/')
def index():
    return render_template('index.html')


# Define the route for the prediction result
@app.route('/predict', methods=['POST'])
def predict():
    # Get the user input from the form
    review = request.form['review']

    # Make a prediction using the pre-trained model
    prediction = large_classifier.get_prediction(review)

    # Convert the prediction to a human-readable format
    # print(prediction)
    if prediction == 'negative':
        result = 'negative'
    else:
        result = 'positive'

    # Render the result page with the prediction
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
