# 按照notebook训练时的输入格式准备数据
# 在notebook中使用的是: X = np.array(training_data.get('request_number')).reshape(-1, 1)
# 每个数字代表一个请求数量(request_number)，作为单一特征输入模型
request_numbers = [
    1976, 2966, 496801,
    1135, 356, 495307,
    4852, 2300, 498510,
    3179, 215, 494471
]

from pathlib import Path
import numpy as np
import xgboost as xgb

model_path = Path(__file__).parent / "training_model" / "modelsfile" / "xgboost_newest_model_5.json"

# load model file
model = xgb.Booster()
model.load_model(model_path)


# Booster 需要 DMatrix 对象作为输入
for x in request_numbers:
    dmatrix = xgb.DMatrix([[x]])
    predictions = model.predict(dmatrix)

    print("Predictions (request_number -> predicted_process_time):")
    print(f"{x} -> {predictions[0]}")
