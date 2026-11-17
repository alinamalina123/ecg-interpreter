import allure
from ecg_interpreter.ecg.interpreter import interpret_ecg
from ecg_interpreter.models.interpretation import Interpretation, Diagnosis, Urgency

@allure.epic("Интерпретация ЭКГ")
@allure.feature("Определение диагноза")
class TestInterpreter:

    @allure.story("Инфаркт")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("ST + Q = Инфаркт")
    def test_interpret_ecg_infarction(self, infarction_ecg_data):
        """Тест: ST + Q = Инфаркт (urgent)"""
        expected = Interpretation(Diagnosis.INFARCTION, Urgency.URGENT)
        result = interpret_ecg(infarction_ecg_data)
        assert result == expected, f"Ожидался результат {expected}, но получен {result}"

    @allure.story("Инфаркт")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("ST без Q = Подозрение на инфаркт")
    def test_interpret_ecg_suspected_infarction(self, suspected_infarction_ecg_data):
        """Тест: ST без Q = Подозрение на инфаркт (urgent)."""
        expected = Interpretation(Diagnosis.SUSPECTED_INFARCTION, Urgency.URGENT)
        result = interpret_ecg(suspected_infarction_ecg_data)
        assert result == expected, f"Ожидался результат {expected}, но получен {result}"

    @allure.story("Ишемия")
    @allure.title("Депрессия ST = Ишемия")
    def test_interpret_ecg_ischemia(self, ischemia_ecg_data):
        """Тест: Депрессия ST = Ишемия (планово)"""
        expected = Interpretation(Diagnosis.ISCHEMIA, Urgency.PLANNED)
        result = interpret_ecg(ischemia_ecg_data)
        assert result == expected, f"Ожидался результат {expected}, но получен {result}"

    @allure.story("Аритмия")
    @allure.title("Нерегулярный ритм = Аритмия")
    def test_interpret_ecg_arrhythmia(self, arrhythmia_ecg_data):
        """Тест: Нерегулярный ритм = Аритмия (Планово)"""
        expected = Interpretation(Diagnosis.ARRHYTHMIA, Urgency.PLANNED)
        result = interpret_ecg(arrhythmia_ecg_data)
        assert result == expected, f"Ожидался результат {expected}, но получен {result}"

    @allure.story("Перенесенный инфаркт")
    @allure.title("Зубец Q без ST = Перенесенный инфаркт")
    def test_interpret_ecg_previous_infarction(self, previous_infarction_ecg_data):
        """Тест: Зубец Q без ST = Перенесенный инфаркт (планово)"""
        expected = Interpretation(Diagnosis.PREVIOUS_INFARCTION, Urgency.PLANNED)
        result = interpret_ecg(previous_infarction_ecg_data)
        assert result == expected, f"Ожидался результат {expected}, но получен {result}"

    @allure.story("Норма")
    @allure.title("Обычные данные ЭКГ = Норма")
    def test_interpret_ecg_fallback_normal(self, normal_ecg_data):
        """Тест: Обычные данные ЭКГ передаются в analyze_heart_rate. (норма)"""
        expected = Interpretation(Diagnosis.NORMAL, Urgency.NONE)
        result = interpret_ecg(normal_ecg_data)
        assert result == expected, f"Ожидался результат {expected}, но получен {result}"

    @allure.story("Тахикардия")
    @allure.title("Высокая ЧСС без патологий ST = Тахикардия")
    def test_interpret_ecg_fallback_tachycardia(self, tachycardia_ecg_data):
        """Тест: Обычные данные ЭКГ передаются в analyze_heart_rate. (тахикардия)"""
        expected = Interpretation(Diagnosis.TACHYCARDIA, Urgency.PLANNED)
        result = interpret_ecg(tachycardia_ecg_data)
        assert result == expected, f"Ожидался результат {expected}, но получен {result}"