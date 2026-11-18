from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class SensorEvent:
    """One reading from one sensor.

    `t_s` comes first so a list of events sorts by time. `value` is the
    sensor's own output: 1/0 for PIR and contacts, presence energy for radar.
    """

    t_s: float
    sensor_id: str
    zone: str
    value: float


def by_zone(events):
    """Group events by zone, each group in time order."""
    zones = {}
    for ev in sorted(events):
        zones.setdefault(ev.zone, []).append(ev)
    return zones
