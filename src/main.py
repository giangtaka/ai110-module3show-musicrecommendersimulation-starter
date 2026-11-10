"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs

def show_recommendations(
    profile_name,
    user_prefs,
    songs
):
    print("\n" + "=" * 50)
    print(profile_name)
    print("=" * 50)

    print(
        f"Genre: {user_prefs['genre']} | "
        f"Mood: {user_prefs['mood']} | "
        f"Energy: {user_prefs['energy']}"
    )

    recommendations = recommend_songs(
        user_prefs,
        songs,
        k=5
    )

    print("\nTop Recommendations:\n")

    for index, rec in enumerate(
        recommendations,
        start=1
    ):
        song, score, explanation = rec

        print(
            f"{index}. "
            f"{song['title']} "
            f"by {song['artist']}"
        )

        print(
            f"   Score: {score:.2f}"
        )

        print(
            f"   Because: {explanation}"
        )

        print()

def main() -> None:
    songs = load_songs("data/songs.csv")

    print(
        f"Loaded songs: {len(songs)}"
    )

    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.9,
            "likes_acoustic": False,
        },

        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.3,
            "likes_acoustic": True,
        },

        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.95,
            "likes_acoustic": False,
        },

        "Conflicting Profile": {
            "genre": "ambient",
            "mood": "intense",
            "energy": 0.95,
            "likes_acoustic": True,
        },
    }

    for profile_name, user_prefs in profiles.items():
        show_recommendations(
            profile_name,
            user_prefs,
            songs
        )


if __name__ == "__main__":
    main()
