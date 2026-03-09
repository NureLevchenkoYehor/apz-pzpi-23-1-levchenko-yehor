from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class GameEventListener(ABC):
    @abstractmethod
    def on_event(self, event_type: str, data: dict) -> None:
        pass


class GameEventSystem:
    def __init__(self) -> None:
        self._listeners: dict[str, List[GameEventListener]] = {}

    def subscribe(self, event_type: str, listener: GameEventListener) -> None:
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(listener)

    def unsubscribe(self, event_type: str, listener: GameEventListener) -> None:
        if event_type in self._listeners:
            self._listeners[event_type].remove(listener)

    def notify(self, event_type: str, data: dict) -> None:
        for listener in self._listeners.get(event_type, []):
            listener.on_event(event_type, data)


class HUDDisplay(GameEventListener):
    def __init__(self) -> None:
        self.health = 100
        self.score = 0

    def on_event(self, event_type: str, data: dict) -> None:
        if event_type == "player_damaged":
            self.health -= data["amount"]
            print(f"[HUD] Health updated: {self.health} HP")
        elif event_type == "score_gained":
            self.score += data["points"]
            print(f"[HUD] Score updated: {self.score} pts")


class SoundSystem(GameEventListener):
    def on_event(self, event_type: str, data: dict) -> None:
        sounds = {
            "player_damaged": "hurt.wav",
            "score_gained": "coin.wav",
            "player_died": "death.wav",
            "level_completed": "fanfare.wav",
        }
        sound = sounds.get(event_type)
        if sound:
            print(f"[Sound] Playing: {sound}")


class AchievementSystem(GameEventListener):
    def __init__(self) -> None:
        self._total_score = 0
        self._unlocked: List[str] = []

    def on_event(self, event_type: str, data: dict) -> None:
        if event_type == "score_gained":
            self._total_score += data["points"]
            if self._total_score >= 100 and "First Century" not in self._unlocked:
                self._unlocked.append("First Century")
                print("[Achievement] Unlocked: 'First Century' — earn 100 points")
        elif event_type == "level_completed":
            level = data.get("level", 0)
            title = f"Level {level} Conqueror"
            if title not in self._unlocked:
                self._unlocked.append(title)
                print(f"[Achievement] Unlocked: '{title}'")


class AnalyticsLogger(GameEventListener):
    def on_event(self, event_type: str, data: dict) -> None:
        print(f"[Analytics] Event logged — type='{event_type}', data={data}")


class Player:
    def __init__(self, name: str, event_system: GameEventSystem) -> None:
        self.name = name
        self._health = 100
        self._events = event_system

    def take_damage(self, amount: int) -> None:
        self._health = max(0, self._health - amount)
        self._events.notify("player_damaged", {"amount": amount, "remaining": self._health})
        if self._health == 0:
            self._events.notify("player_died", {"player": self.name})

    def collect_coin(self, value: int) -> None:
        self._events.notify("score_gained", {"points": value, "player": self.name})


class Level:
    def __init__(self, number: int, event_system: GameEventSystem) -> None:
        self._number = number
        self._events = event_system

    def complete(self) -> None:
        self._events.notify("level_completed", {"level": self._number})

def main():
    events = GameEventSystem()

    hud = HUDDisplay()
    sound = SoundSystem()
    achievements = AchievementSystem()
    analytics = AnalyticsLogger()

    events.subscribe("player_damaged", hud)
    events.subscribe("player_damaged", sound)
    events.subscribe("player_damaged", analytics)

    events.subscribe("score_gained", hud)
    events.subscribe("score_gained", sound)
    events.subscribe("score_gained", achievements)
    events.subscribe("score_gained", analytics)

    events.subscribe("player_died", sound)
    events.subscribe("player_died", analytics)

    events.subscribe("level_completed", sound)
    events.subscribe("level_completed", achievements)
    events.subscribe("level_completed", analytics)

    player = Player("Alice", events)
    level = Level(1, events)

    print("=== Game Session Start ===\n")

    print("-- Player collects coins --")
    player.collect_coin(40)
    print()
    player.collect_coin(35)
    print()
    player.collect_coin(30)

    print("\n-- Player takes damage --")
    player.take_damage(25)

    print("\n-- Player analytics unsubscribes (debug mode off) --")
    events.unsubscribe("score_gained", analytics)
    events.unsubscribe("player_damaged", analytics)
    player.collect_coin(10)
    player.take_damage(10)

    print("\n-- Level completed --")
    level.complete()

    print("\n=== Game Session End ===")

if __name__ == "__main__":
    main()