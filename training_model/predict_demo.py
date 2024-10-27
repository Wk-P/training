import xgboost as xgb
import random

model_path = "D:/model_fit/training/training_model/modelsfile/xgb_number_time_linear.json"
xgb_model = xgb.XGBRegressor()
xgb_model.load_model(model_path)

for i in range(100):
    data = xgb_model.predict([[random.randint(0, 500000)]])
    print(data[0])