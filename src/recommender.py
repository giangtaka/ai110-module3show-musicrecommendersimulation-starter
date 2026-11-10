from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, asdict
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }

        scored_songs = []

        for song in self.songs:
            song_dict = asdict(song)

            score, _ = score_song(
                user_prefs,
                song_dict
            )

            scored_songs.append(
                (score, song)
            )

        scored_songs.sort(
            key=lambda item: item[0],
            reverse=True
        )

        return [
            song
            for score, song in scored_songs[:k]
        ]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }

        score, reasons = score_song(
            user_prefs,
            asdict(song)
        )

        return ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    songs = []

    with open(
            csv_path,
            "r",
            encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["id"] = int(row["id"])

            row["energy"] = float(
                row["energy"]
            )

            row["tempo_bpm"] = float(
                row["tempo_bpm"]
            )

            row["valence"] = float(
                row["valence"]
            )

            row["danceability"] = float(
                row["danceability"]
            )

            row["acousticness"] = float(
                row["acousticness"]
            )

            songs.append(row)

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    # TODO: Implement scoring logic using your Algorithm Recipe from Phase 2.
    # Expected return format: (score, reasons)
    score = 0.0
    reasons = []

    # Genre match
    if song["genre"].lower() == user_prefs["genre"].lower():
        score += 2.0
        reasons.append(
            "genre match (+2.0)"
        )

    # Mood match
    if song["mood"].lower() == user_prefs["mood"].lower():
        score += 1.0
        reasons.append(
            "mood match (+1.0)"
        )

    # Energy similarity
    energy_gap = abs(
        song["energy"]
        - user_prefs["energy"]
    )

    energy_score = max(
        0.0,
        2.0 * (1.0 - energy_gap)
    )

    score += energy_score

    reasons.append(
        f"energy similarity (+{energy_score:.2f})"
    )

    # Optional acoustic preference
    if "likes_acoustic" in user_prefs:

        likes_acoustic = user_prefs[
            "likes_acoustic"
        ]

        if (
                likes_acoustic
                and song["acousticness"] >= 0.6
        ):
            score += 0.5

            reasons.append(
                "acoustic preference (+0.5)"
            )

        elif (
                not likes_acoustic
                and song["acousticness"] < 0.6
        ):
            score += 0.5

            reasons.append(
                "low acousticness preference (+0.5)"
            )

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    scored = []

    for song in songs:
        score, reasons = score_song(
            user_prefs,
            song
        )

        explanation = ", ".join(reasons)

        scored.append(
            (
                song,
                score,
                explanation
            )
        )

    scored.sort(
        key=lambda item: item[1],
        reverse=True
    )

    return scored[:k]
