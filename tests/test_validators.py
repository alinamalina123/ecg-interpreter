import pytest
import allure
from ecg_interpreter.ecg.validators import validate_data, validate_dataset, validate_heart_rate


@allure.epic("Валидация данных")
@allure.feature("Негативные сценарии")
class TestValidators:

    @allure.title("Проверка пустых данных ЭКГ")
    def test_validate_data_none(self):
        with pytest.raises(ValueError, match="Данные ЭКГ не могут быть пустыми"):
            validate_data(None)

    @allure.title("Проверка пустого списка измерений")
    def test_validate_dataset_empty(self, empty_ecg_dataset):
        with pytest.raises(ValueError, match="Список измерений не может быть пустым"):
            validate_dataset(empty_ecg_dataset)

    @allure.title("Проверка ЧСС: None")
    def test_validate_heart_rate_none(self):
        with pytest.raises(ValueError, match="Значение ЧСС не может быть пустыми"):
            validate_heart_rate(None)

    @allure.title("Проверка ЧСС: отрицательное значение")
    def test_validate_heart_rate_negative(self):
        with pytest.raises(ValueError, match="Значение ЧСС не может быть отрицательным"):
            validate_heart_rate(-10.0)

    @allure.title("Проверка ЧСС: превышение физиологического максимума")
    def test_validate_heart_rate_too_high(self):
        # MAX_HEART_RATE = 300.0, передаем 301
        with pytest.raises(ValueError, match="Значение ЧСС физиологически невозможно"):
            validate_heart_rate(301.0)

    @allure.title("Проверка ЧСС: NaN (не число)")
    def test_validate_heart_rate_nan(self):
        with pytest.raises(ValueError, match="Значение ЧСС должно быть конечным числом"):
            validate_heart_rate(float('nan'))

    @allure.title("Проверка ЧСС: бесконечность")
    def test_validate_heart_rate_inf(self):
        with pytest.raises(ValueError, match="Значение ЧСС физиологически невозможно"):
            validate_heart_rate(float('inf'))