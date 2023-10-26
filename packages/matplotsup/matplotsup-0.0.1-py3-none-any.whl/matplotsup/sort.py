import matplotlib.pyplot as plt
import random
import time
from IPython.display import display, clear_output

def init(data):
    fig, ax = plt.subplots()
    ax.set_title('Selection Sort Visualization')
    bars = ax.bar(range(len(data)), data)
    return fig, bars

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        yield arr
        
def sort_animat(fig, bars, data):
    for step, sorted_data in enumerate(selection_sort(data)):
        for bar, value in zip(bars, sorted_data):
            bar.set_height(value)

        # 시각화 업데이트
        clear_output(wait=True)
        display(fig)

        time.sleep(0.1)