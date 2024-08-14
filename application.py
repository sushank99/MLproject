from flask import Flask, request, render_template, redirect, url_for
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "POST":
        # Retrieve form data and handle missing values
        gender = request.form.get("gender")
        race_ethnicity = request.form.get("race_ethnicity")
        parental_level_of_education = request.form.get("parental_level_of_education")
        lunch = request.form.get("lunch")
        test_preparation_course = request.form.get("test_preparation_course")
        
        # Check if the scores are provided and valid
        try:
            reading_score = float(request.form.get("reading_score", "0"))
            writing_score = float(request.form.get("writing_score", "0"))
        except ValueError:
            # Handle invalid float conversion
            return render_template("home.html", error="Invalid input for scores. Please enter valid numbers.")

        # Create CustomData object
        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score,
        )

        # Convert data to DataFrame
        pred_df = data.get_data_as_data_frame()
        print(pred_df)  # Debugging: Check the input data

        # Predict and handle errors
        try:
            predict_pipeline = PredictPipeline()
            result = predict_pipeline.predict(pred_df)
            print(result)  # Debugging: Check the prediction result

            # Redirect to result page with prediction
            return redirect(url_for("show_result", prediction=result[0]))
        except Exception as e:
            print(f"Error during prediction: {e}")  # Debugging: Print any error during prediction
            return render_template("home.html", error="Error during prediction. Please try again.")
    
    # If GET request or invalid POST request
    return render_template("home.html")

@app.route("/result")
def show_result():
    # Retrieve the prediction score from query parameters
    prediction = request.args.get('prediction')
    return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
