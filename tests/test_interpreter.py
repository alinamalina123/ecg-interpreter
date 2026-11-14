from ecg_interpreter.ecg.interpreter import interpret_ecg
from ecg_interpreter.models.interpretation import Interpretation, Diagnosis, Urgency


def test_interpret_ecg_infarction(infarction_ecg_data):
    """Тест: ST + Q = Инфаркт (urgent)"""
    expected = Interpretation(Diagnosis.INFARCTION, Urgency.URGENT)
    result = interpret_ecg(infarction_ecg_data)
    
    assert result == expected, f"Ожидался результат {expected}, но получен {result}"


def test_interpret_ecg_suspected_infarction(suspected_infarction_ecg_data):
    """Тест: ST без Q = Подозрение на инфаркт (urgent)."""
    expected = Interpretation(Diagnosis.SUSPECTED_INFARCTION, Urgency.URGENT)
    result = interpret_ecg(suspected_infarction_ecg_data)
    
    assert result == expected, f"Ожидался результат {expected}, но получен {result}"


def test_interpret_ecg_ischemia(ischemia_ecg_data):
    """Тест: Депрессия ST = Ишемия (планово)"""
    expected = Interpretation(Diagnosis.ISCHEMIA, Urgency.PLANNED)
    result = interpret_ecg(ischemia_ecg_data)
    
    assert result == expected, f"Ожидался результат {expected}, но получен {result}"


def test_interpret_ecg_arrhythmia(arrhythmia_ecg_data):
    """Тест: Нерегулярный ритм = Аритмия (Планово)"""
    expected = Interpretation(Diagnosis.ARRHYTHMIA, Urgency.PLANNED)
    result = interpret_ecg(arrhythmia_ecg_data)
    
    assert result == expected, f"Ожидался результат {expected}, но получен {result}"


def test_interpret_ecg_previous_infarction(previous_infarction_ecg_data):
    """Тест: Зубец Q без ST = Перенесенный инфаркт (планово)"""
    expected = Interpretation(Diagnosis.PREVIOUS_INFARCTION, Urgency.PLANNED)
    result = interpret_ecg(previous_infarction_ecg_data)
    
    assert result == expected, f"Ожидался результат {expected}, но получен {result}"


def test_interpret_ecg_fallback_normal(normal_ecg_data):
    """Тест: Обычные данные ЭКГ передаются в analyze_heart_rate. (норма)"""
    expected = Interpretation(Diagnosis.NORMAL, Urgency.NONE)
    result = interpret_ecg(normal_ecg_data)
    
    assert result == expected, f"Ожидался результат {expected}, но получен {result}"


def test_interpret_ecg_fallback_tachycardia(tachycardia_ecg_data):
    """Тест: Обычные данные ЭКГ передаются в analyze_heart_rate. (тахикардия)"""
    expected = Interpretation(Diagnosis.TACHYCARDIA, Urgency.PLANNED)
    result = interpret_ecg(tachycardia_ecg_data)
    
    assert result == expected, f"Ожидался результат {expected}, но получен {result}"