# BMI Calculator — Azure Web App

A full-stack BMI (Body Mass Index) calculator built with Python and HTML, deployed to Microsoft Azure.

Started as a simple frontend project, then refactored into a proper API architecture using Azure Functions.

## What it does

Takes height and weight as input and returns the BMI value along with the category (Underweight / Normal / Overweight / Obese).

## Versions

**v1 — Monolith**
- Single Python file handling both frontend and logic

**v2 — API Split**
- Frontend separated into `index.html`
- BMI logic moved to Azure Functions (`function_app.py`)
- CI/CD pipeline configured with GitHub Actions

## Stack

- Python, HTML, CSS
- Azure App Service + Azure Functions
- GitHub Actions for automated deployment

```bash
pip install -r requirements.txt
func start
```

Then open `index.html` in your browser.
