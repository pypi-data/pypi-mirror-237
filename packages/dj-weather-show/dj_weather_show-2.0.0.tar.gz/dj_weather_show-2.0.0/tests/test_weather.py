from dj_weather_show.weather_show import weather_show, get_weather

def test_weather():
    weather_show()
    assert True

def test_get_weather():
    r = get_weather()
    assert type(r) is tuple
    assert r[0] == "동작구 신대방2동"
