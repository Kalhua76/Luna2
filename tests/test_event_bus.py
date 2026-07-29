from luna.events.event import Event
from luna.events.event_bus import EventBus

def test_publish():
    bus=EventBus()
    data=[]
    bus.subscribe("ping", lambda e:data.append(e.payload["ok"]))
    bus.publish(Event("ping",{"ok":True}))
    assert data==[True]
