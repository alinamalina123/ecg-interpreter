import pytest
from ecg_interpreter.models.ecg_data import ECGData, STSegment, Rhythm

@pytest.fixture
def ecg_dataset():
    """Фикстура со списком данных ЭКГ для тестирования агрегаций (среднее, диапазон)."""
    return [
        ECGData(heart_rate=60.0, rhythm=Rhythm.REGULAR, st_segment=STSegment.NORMAL, q_wave=False),
        ECGData(heart_rate=80.0, rhythm=Rhythm.REGULAR, st_segment=STSegment.NORMAL, q_wave=False),
        ECGData(heart_rate=100.0, rhythm=Rhythm.REGULAR, st_segment=STSegment.NORMAL, q_wave=False),
    ]


@pytest.fixture
def normal_ecg_data():
    """Фикстура с валидными данными ЭКГ без патологий."""
    return ECGData(
        heart_rate=75.0,
        rhythm=Rhythm.REGULAR,
        st_segment=STSegment.NORMAL,
        q_wave=False
    )

@pytest.fixture
def infarction_ecg_data():
    """Фикстура с данными ЭКГ для инфаркта (ST + Q)"""
    return ECGData(
        heart_rate = 90.0,
        rhythm = Rhythm.REGULAR,
        st_segment = STSegment.ELEVATION,
        q_wave = True,
    )

@pytest.fixture
def ischemia_ecg_data():
    """Фикстура с данными ЭКГ для ишемии (депрессия ST)."""
    return ECGData(
        heart_rate=80.0,
        rhythm=Rhythm.REGULAR,
        st_segment=STSegment.DEPRESSION,
        q_wave=False
    )


@pytest.fixture
def arrhythmia_ecg_data():
    """Фикстура с данными ЭКГ для аритмии (нерегулярный ритм)."""
    return ECGData(
        heart_rate=70.0,
        rhythm=Rhythm.IRREGULAR,
        st_segment=STSegment.NORMAL,
        q_wave=False
    )

@pytest.fixture
def suspected_infarction_ecg_data():
    """Фикстура для подозрения на инфаркт (элевация ST без зубца Q)."""
    return ECGData(
        heart_rate=90.0,
        rhythm=Rhythm.REGULAR,
        st_segment=STSegment.ELEVATION,
        q_wave=False
    )

@pytest.fixture
def previous_infarction_ecg_data():
    """Фикстура для перенесенного инфаркта (зубец Q без элевации ST)."""
    return ECGData(
        heart_rate=75.0,
        rhythm=Rhythm.REGULAR,
        st_segment=STSegment.NORMAL,
        q_wave=True
    )
@pytest.fixture
def tachycardia_ecg_data():
    """Фикстура для тахикардии (высокий ЧСС, остальное в норме)."""
    return ECGData(
        heart_rate=120.0,
        rhythm=Rhythm.REGULAR,
        st_segment=STSegment.NORMAL,
        q_wave=False
    )

#2 часть
@pytest.fixture
def empty_ecg_dataset():
    """Фикстура с пустым списком данных ЭКГ."""
    return []

@pytest.fixture
def none_ecg_data():
    """Фикстура с отсутствующими данными ЭКГ."""
    return None