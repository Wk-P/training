from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np

# type hint
from matplotlib.figure import Figure
from matplotlib.axes import Axes

def read_excel(dirpath, filename):
    try:
        filepath = f"{dirpath}/{filename}"
        if not os.path.exists(dirpath):
            raise Exception(f"No {filepath} exsits")
    
        df = pd.read_excel(filepath)

        columns = df.columns.to_list()

        data_dict = {col: df[col].to_list() for col in columns}

        return data_dict

    except Exception as e:
        print(e)
        exit(1)



def strToFloat(data):
    for index in range(len(data)):
        data_item: str = data[index]
        data[index] = float(data_item.replace(" ", "").replace("%", ""))

    return data



def draw(X: list, Y: list, imgpath=None):
    test = X['test']
    pred = X['pred']
    num = Y

    ax: Axes
    fig: Figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # 对数据进行排序（以 num 为依据）
    sorted_indices = np.argsort(num)
    sorted_num = np.array(num)[sorted_indices]
    sorted_test = np.array(test)[sorted_indices]
    sorted_pred = np.array(pred)[sorted_indices]

    ax.scatter(sorted_num, sorted_test, marker='.', color='b', label='test data')
    ax.scatter(sorted_num, sorted_pred, s=1, marker=',', color='r', label='pred data')

    ax.plot(sorted_num, sorted_test, linestyle='-', color='b', alpha=0.5)  # 使用透明度线
    ax.plot(sorted_num, sorted_pred, linestyle='--', color='r', alpha=0.5)  # 使用透明度线

    # 标注具体数值
    for i in range(len(num)):
        ax.annotate(f'{num[i]} | {test[i]:.2f}', (num[i], test[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='b')
        ax.annotate(f'{num[i]} | {pred[i]:.2f}', (num[i], pred[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='r')

    ax.set_xlabel('Request Number')
    ax.set_ylabel('Predicted and Read process on manager node')
    
    ax.grid(True, linestyle='--', linewidth=0.5)
    
    ax.legend()
    
    # fig.savefig(imgpath, format='png', dpi=300, bbox_inches='tight')
    
    plt.show()

    pass





if __name__ == "__main__":
    dirpath = Path.cwd() / "results" / "result_requestNumber_processTime"
    file_suffix = ".xlsx"
    filename = "RandomRequestNumberclientv5#loops1#requests_batch200#Thu-Jul-25-23-28-51-2024requestNumber#responseTimeresult" + file_suffix 

    data = read_excel(dirpath, filename)

    accu: list = strToFloat(data.get("accuracy"))
    num = data['num']
    test = data['test']
    pred = data['prediction']
    diff = data['difference']

    draw({"test": test, "pred": pred}, num)
    
