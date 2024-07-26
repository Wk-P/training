from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import os

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



def draw(X, Y):
    plt.scatter(X, [0]*len(X))
    plt.xlabel('X axis')
    plt.ylabel('Y axis (default 0)')
    plt.title('Scatter Plot with Only X Data')
    plt.show()
    pass





if __name__ == "__main__":
    dirpath = Path.cwd() / "results" / "result_processTime_waitTasks"
    file_suffix = ".xlsx"
    filename = "RandomRequestNumberclientv5#loops1#requests_batch200#Thu-Jul-25-23-28-51-2024processTime#waitTasksresult" + file_suffix 

    data = read_excel(dirpath, filename)

    accu: list = strToFloat(data.get("accuracy"))
    test = data['test']
    pred = data['prediction']
    diff = data['difference']

        # 仅有 x 轴数据
    x = [1, 2, 3, 4, 5]

    # 创建 y 轴数据，默认设为零
    y = [0] * len(x)

    # 绘制折线图
    plt.plot(x, y, marker='o', linestyle='-', color='b')  # 'o' 表示点标记，'-' 表示折线
    plt.xlabel('X axis')
    plt.ylabel('Y axis (default 0)')
    plt.title('Line Plot with X Data and Default Y Values')
    plt.grid(True)
    plt.show()
