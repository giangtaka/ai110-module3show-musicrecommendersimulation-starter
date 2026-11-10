# 🎵 Music Recommender Simulation

## Project Summary

This project is a small content-based music recommender. 
It compares a user's preferences with features from each song, 
calculates a score, and ranks the songs from strongest to weakest match.

The goal is not to recreate Spotify, 
but to understand how simple data and scoring rules 
can produce recommendations that feel personalized.

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

Real recommendation platforms may combine many types of information, including listening history, likes, skips, playlists, and similarities between users. Collaborative filtering uses behavior from many users to find patterns, while content-based filtering compares characteristics of items directly with a user's preferences.

My project uses a simplified content-based approach.

Each song contains:
- genre
- mood
- energy
- tempo
- valence
- danceability
- acousticness

The user profile contains:

- favorite genre

- favorite mood

- target energy

- acoustic preference

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

I tested the system using several different user profiles:

- High-Energy Pop

- Chill Lofi

- Deep Intense Rock

- A conflicting profile that wanted high-energy intense ambient music

The profiles produced noticeably different rankings because genre, mood, and energy affected the scores differently.

I also tested a weight change where energy became twice as important and genre became less important. 
High-energy songs began ranking higher across genre boundaries. 
This showed how sensitive a recommendation system can be to manually chosen weights.
## Limitations and Risks

This recommender uses a very small synthetic catalog, so it cannot represent the variety of real music.

The scoring system depends heavily on manually assigned labels such as genre and mood. Music can fit multiple genres or moods, but this model treats those fields as simple exact matches.

The model also has no listening history, skips, likes, lyrics, cultural context, or feedback from other users. Because of this, its recommendations should be treated as a classroom simulation rather than predictions of a person's real musical taste.

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

One thing I learned is that a recommendation system does not have to use a complicated machine-learning model to feel personalized. 
Even a small scoring formula can create noticeably different results when the user's preferences change.

I also learned that the design decisions behind the model matter a lot. 
Changing one weight can completely change which songs appear at the top. 
AI helped me brainstorm scoring rules and edge cases, 
but I still needed to understand the calculations, 
run different profiles, and check whether the results actually made sense.
