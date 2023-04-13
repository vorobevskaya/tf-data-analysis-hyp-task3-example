import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

chat_id = 689606612 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    p = mannwhitneyu(x, y).pvalue
    if p >= 0.09:
      result = bool(0)
    else:
      result = bool(1)
    return result # Ваш ответ, True или False
