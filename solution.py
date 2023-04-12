import pandas as pd
import numpy as np
from scipy import stats

chat_id = 1167847408 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    result = stats.anderson_ksamp(x,y)
    return result.pvalue < 0.04 # Ваш ответ, True или False
