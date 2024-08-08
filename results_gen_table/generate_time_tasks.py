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
    diff = X['diff']
    accu = X['accu']
    num = Y

    ax1: Axes
    ax2: Axes
    ax3: Axes
    fig: Figure
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(45, 28))
    # 对数据进行排序（以 num 为依据）
    sorted_indices = np.argsort(num)
    sorted_num = np.array(num)[sorted_indices]
    sorted_accu = np.array(accu)[sorted_indices]
    sorted_diff = np.array(diff)[sorted_indices]
    sorted_test = np.array(test)[sorted_indices]
    sorted_pred = np.array(pred)[sorted_indices]

    # fig 1
    ax1.scatter(sorted_num, sorted_accu, marker='.', color='b', label="accuracy")

    # fig2
    ax2.scatter(sorted_num, sorted_test, marker='.', color='b', label="real process time")
    ax2.scatter(sorted_num, sorted_pred, marker='.', color='r', label="predicted process time")
    
    ax2.plot(sorted_num, sorted_test, linestyle='-', color='b', alpha=0.2, label="test time")
    ax2.plot(sorted_num, sorted_pred, linestyle='--', color='r', alpha=0.2, label="predicted time")

    # fig3
    ax3.errorbar(sorted_num, sorted_test, yerr=sorted_diff, fmt='.', color='b', ecolor='lightblue', elinewidth=1, capsize=2, label='Test difference')
    ax3.errorbar(sorted_num, sorted_pred, yerr=sorted_diff, fmt='.', color='y', ecolor='salmon', elinewidth=1, capsize=2, label='Prediction difference')


    #@ 标注具体数值
    #@ Annotate specific numerical values

    # for i in range(len(num)):
    #     ax.annotate(f'{num[i]} | {test[i]:.2f}', (num[i], test[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='b')
    #     ax.annotate(f'{num[i]} | {pred[i]:.2f}', (num[i], pred[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='r')

    ax1.set_xlabel('Request Number')
    ax1.set_ylabel('Accuracy')
    ax1.set_title('Scatter plot of prediction accuracy distribution')

    ax2.set_xlabel('Request Number')
    ax2.set_ylabel('Test and prediction')
    ax2.set_title('Prediction of accuracy')

    ax1.grid(True, linestyle='--', linewidth=0.5)
    ax2.grid(True, linestyle='--', linewidth=0.5)
    
    ax1.legend()
    ax2.legend()

    if imgpath:
        fig.savefig(imgpath, format='png', dpi=300, bbox_inches='tight')
    
    plt.show()

    pass





if __name__ == "__main__":
    dirpath = Path.cwd() / "results" / "result_processTime_waitTasks"
    file_suffix = ".xlsx"
    filename = "RandomRequestNumberclientv5#loops4#requests_batch200#Fri-Jul-26-18-36-52-2024processTime#waitTasks_v4result" + file_suffix 

    data = read_excel(dirpath, filename)

    accu: list = strToFloat(data.get("accuracy"))
    num = data['num']
    test = data['test']
    pred = data['prediction']
    diff = data['difference']

    image_path = Path.cwd() / 'results' / 'tables' / 'The relationship v4.png'
    draw({"test": test, "pred": pred, "diff": diff, "accu": accu}, num, image_path)
