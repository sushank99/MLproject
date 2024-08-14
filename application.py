from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)


@app.route("/app")
def index():
    return render_template("index.html")


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "POST":
        data = CustomData(
            gender=request.form.get("gender"),
            race_ethnicity=request.form.get("race_ethnicity"),
            parental_level_of_education=request.form.get("parental_level_of_education"),
            lunch=request.form.get("lunch"),
            test_preparation_course=request.form.get("test_preparation_course"),
            reading_score=float(request.form.get("reading_score")),
            writing_score=float(request.form.get("writing_score")),
        )

        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(pred_df)
        print(result)
        return render_template("home.html", result=result[0])
    return render_template("home.html")


if __name__ == "__main__":
    app.run(port=5001)  # Ensure port 5000 or use a different one if needed
