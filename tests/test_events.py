from fusion.events import SensorEvent, by_zone


def test_by_zone_sorts_each_zone_by_time():
    evs = [
        SensorEvent(2.0, "pir1", "hall", 1),
        SensorEvent(0.5, "door1", "hall", 1),
        SensorEvent(1.0, "pir2", "garage", 1),
    ]
    zones = by_zone(evs)
    assert [e.sensor_id for e in zones["hall"]] == ["door1", "pir1"]
    assert list(zones) == ["hall", "garage"]
