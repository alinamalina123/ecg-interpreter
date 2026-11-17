import pytest
import allure
from ecg_interpreter.ecg.heart_rate_analyser import analyze_heart_rate, average_heart_rate, heart_rate_range
from ecg_interpreter.models.interpretation import Diagnosis
from ecg_interpreter.consts.consts import LOW_HEART_RATE, HIGH_HEART_RATE

@allure.epic("Анализ ЧСС")
@allure.feature("Функции анализа сердечного ритма")
class TestHeartRateAnalyzer:

    @allure.story("Позитивные сценарии analyze_heart_rate")
    @pytest.mark.parametrize(
        "heart_rate, expected_diagnosis",
        [
            (LOW_HEART_RATE - 0.1, Diagnosis.BRADYCARDIA),  # 59.9 - Брадикардия
            (LOW_HEART_RATE, Diagnosis.NORMAL),           # 60.0 - Нижняя граница нормы
            (HIGH_HEART_RATE, Diagnosis.NORMAL),          # 100.0 - Верхняя граница нормы
            (HIGH_HEART_RATE + 0.1, Diagnosis.TACHYCARDIA), # 100.1 - Тахикардия
            (50.0, Diagnosis.BRADYCARDIA),                # Явная брадикардия
            (120.0, Diagnosis.TACHYCARDIA),               # Явная тахикардия
            (80.0, Diagnosis.NORMAL),                     # 80.0 - Явная норма
        ]
    )
    def test_analyze_heart_rate_positive(self, heart_rate, expected_diagnosis):
        """Позитивные тесты для analyze_heart_rate с проверкой граничных значений."""
        actual_diagnosis = analyze_heart_rate(heart_rate)
        assert actual_diagnosis == expected_diagnosis, (
            f"При ЧСС {heart_rate} ожидали диагноз '{expected_diagnosis.value}', "
            f"но получили '{actual_diagnosis.value}'"
        )

    @allure.story("Негативные сценарии analyze_heart_rate")
    @allure.title("Негативный тест: отрицательная ЧСС")
    def test_analyze_heart_rate_negative(self):
        with pytest.raises(ValueError, match="Значение ЧСС не может быть отрицательным"):
            analyze_heart_rate(-5.0)

    @allure.story("Среднее значение")
    @allure.title("Вычисление среднего значения ЧСС")
    def test_average_heart_rate(self, ecg_dataset):
        result = average_heart_rate(ecg_dataset)
        assert result == pytest.approx(80.0), f"Ожидалось среднее 80.0, но получено {result}"

    @allure.story("Среднее значение")
    @allure.title("Негативный тест: среднее для пустого списка")
    def test_average_heart_rate_empty(self, empty_ecg_dataset):
        with pytest.raises(ValueError, match="Список измерений не может быть пустым"):
            average_heart_rate(empty_ecg_dataset)

    @allure.story("Диапазон значений")
    @allure.title("Нахождение минимального и максимального ЧСС")
    def test_heart_rate_range(self, ecg_dataset):
        min_hr, max_hr = heart_rate_range(ecg_dataset)
        assert min_hr == 60.0, f"Ожидался минимум 60.0, но получен {min_hr}"
        assert max_hr == 100.0, f"Ожидался максимум 100.0, но получен {max_hr}"
        
    @allure.story("Диапазон значений")
    @allure.title("Негативный тест: диапазон для пустого списка")
    def test_heart_rate_range_empty(self, empty_ecg_dataset):
        with pytest.raises(ValueError):
            heart_rate_range(empty_ecg_dataset)