import azure.functions as func
import json
import math

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="CalculateArea")
def CalculateArea(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
        weight = float(data.get("weight", 0))
        height = float(data.get("height", 0))

        if weight <= 0 or height <= 0:
            return func.HttpResponse(
                json.dumps({"error": "Invalid values"}),
                mimetype="application/json",
                status_code=400
            )

        height_m = height / 100
        bmi = round(weight / (height_m ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        return func.HttpResponse(
            json.dumps({"bmi": bmi, "category": category}),
            mimetype="application/json",
            status_code=200
        )
    except Exception as e:
        return func.HttpResponse(str(e), status_code=400)