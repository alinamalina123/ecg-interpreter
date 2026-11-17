import pytest
import allure
from ecg_interpreter.ecg.risk_analyzer import risk_score


@allure.epic("Анализ риска")
@allure.feature("Расчет показателя risk_score")
class TestRiskAnalyzer:

    @allure.title("Риск для нормальной ЭКГ")
    def test_risk_score_normal(self, normal_ecg_data):
        # base=0.0 (Urgency.NONE), heart_rate_comp=0.0 (NORMAL), mult=1.0
        result = risk_score(normal_ecg_data)
        assert result == pytest.approx(0.0), f"Ожидался риск 0.0, но получен {result}"

    @allure.title("Риск для тахикардии")
    def test_risk_score_tachycardia(self, tachycardia_ecg_data):
        # base=25.0 (PLANNED), heart_rate_comp=0.2 (override TACHYCARDIA), mult=1.2
        # (25.0 * 0.2) * 1.2 = 6.0
        result = risk_score(tachycardia_ecg_data)
        assert result == pytest.approx(6.0), f"Ожидался риск 6.0, но получен {result}"

    @allure.title("Риск для инфаркта (при нормальном ЧСС)")
    def test_risk_score_infarction(self, infarction_ecg_data):
        # base=80.0 (URGENT), heart_rate_comp=0.0 (NORMAL, т.к. ЧСС=90), mult=2.0
        # (80.0 * 0.0) * 2.0 = 0.0
        result = risk_score(infarction_ecg_data)
        assert result == pytest.approx(0.0), f"Ожидался риск 0.0, но получен {result}"

    @allure.title("Негативный тест: передача None в risk_score")
    def test_risk_score_none(self, none_ecg_data):
        with pytest.raises(ValueError, match="Данные ЭКГ не могут быть пустыми"):
            risk_score(none_ecg_data)