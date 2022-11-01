<h1 align="center">
  <br>
  <a href="https://worldhappiness.report/"><img src="https://pbs.twimg.com/profile_images/1495156089037361155/2WDTtM_Z_400x400.jpg" alt="WHR" width="200"></a>
  <br>
  World Happiness Report
  <br>
</h1>

<h4 align="center">A Machine Learning Model built in scikit-learn using Support Vector Regressors and ensemble modeling with Gradient Boost Regressor and Cross Validation. 
</h4>

<p align="center">
  <a href='https://www.kaggle.com/' target="_blank"><img alt='kaggle' src='https://img.shields.io/badge/Kaggle-100000?style=for-the-badge&logo=kaggle&logoColor=FFFFFF&labelColor=37BAE8&color=37BAE8'/></a> <a href='https://github.com/shivamkapasia0' target="_blank"><img alt='scikit-learn' src='https://img.shields.io/badge/scikit-learn-100000?style=for-the-badge&logo=scikit-learn&logoColor=FFFFFF&labelColor=FF6A00&color=1882EA'/></a> <a href='https://github.com/shivamkapasia0' target="_blank"><img alt='flask' src='https://img.shields.io/badge/Flask-100000?style=for-the-badge&logo=flask&logoColor=FFFFFF&labelColor=000000&color=949DA6'/></a> <a href='https://joblib.readthedocs.io/en/latest/' target="_blank"><img alt='joblib' src='https://img.shields.io/badge/Joblib-100000?style=for-the-badge&logo=joblib&logoColor=EA1616&labelColor=BD9B7A&color=000000'/></a> <a href='https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi0tfXl3Iv7AhUVTDABHZOWB-AQFnoECBEQAQ&url=https%3A%2F%2Fwww.json.org%2F&usg=AOvVaw3WUMhwoap01T91PbRZTt_w' target="_blank"><img alt='json' src='https://img.shields.io/badge/Json-100000?style=for-the-badge&logo=json&logoColor=3C3B3B&labelColor=D7CEC7&color=D7D7D7'/></a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a> 
</p>

![screenshot](https://github.com/santiagoahl/world-happiness/blob/main/intro.gif)

## Key Features

This machine learning model predicts de happines score, which is a number between 0 and 10. The dataset is taken from the [World Happiness Report Kaggle Competition](https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2017.csv). So here are the key features of this project:

* Prediction is based on this country's features:
  - `high` 
  - `low` 
  - `gdp` 
  - `family`
  - `lifexp` 
  - `freedom` 
  - `generosity` 
  - `corruption` 
  - `dystopia` : Imaginary country that has the world's least-happy people.
* Professional Modularization on this Project.  Some modules are programmed using **OOP**.
* Build with an Rest API programmed in **Flask** .
* Based on **Scikit-Learn** modules and functions such like:
  -  `svm.SVR` :   Support Vector Regressor.
  - `ensemble.GradientBoostingRegressor` :   Gradiente Boosting Regressors Ensemble method.
  - `model_selection.GridSearchCV` :   Cross validation method.

## How To Use

To clone and run this application, follow these steps

```bash
# Clone this repository
$ git clone https://github.com/santiagoahl/world-happiness.git

# Go into the repository
$ cd world-happiness

# Install dependencies
$ pip install -r requirements.txt

# Run the app
$ python3 server.py

#View results putting the following on your browser (If port 8080 is busy change it)

http://127.0.0.1:8080/predict
```

## Credits

This software uses the following packages:

- [Scikit-Learn](https://scikit-learn.org/stable/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Joblib](https://joblib.readthedocs.io/en/latest/)


## License

MIT

---

> Web Site [santiagoal.com](https://santiagoal.super.site/) &nbsp;&middot;&nbsp;
> GitHub [@santiagoahl](https://github.com/santiagoahl) &nbsp;&middot;&nbsp;
> Twitter [@sahumadaloz](https://twitter.com/sahumadaloz)
