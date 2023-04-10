import numpy as np
from django.shortcuts import render

import pickle
from .forms import PredictionForm


def index(request):
    form = PredictionForm()

    if request.method == "POST":
        form = PredictionForm(request.POST)

        if form.is_valid():
            pregnancies = form.cleaned_data["pregnancies"]
            glucose = form.cleaned_data["glucose"]
            bmi = form.cleaned_data["bmi"]
            age = form.cleaned_data["age"]

            with open("predictor/diabetes_model.pkl", "rb") as file:
                model = pickle.load(file)

            input_data = np.array([[pregnancies, glucose, bmi, age]])
            prediction = model.predict(input_data)[0]

            return render(request, "predictor/index.html",
                          {"prediction": "Positive" if prediction else "Negative", "form": form})

    return render(request, "predictor/index.html", {"form": form})


def about(request):
    return render(request, 'predictor/about.html')