# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

# VibeMatch 1.0

## 2. Intended Use  

VibeMatch is a classroom music recommendation simulation.

It recommends songs from a small catalog based on a user's preferred genre, mood, energy level, and acoustic preference.

It is designed to demonstrate how a content-based recommendation system works. 
It is not designed to predict a person's real musical taste or replace a commercial recommendation platform.

## 3. How the Model Works  

The system compares each song with the user's preferences and gives the song a score.

A genre match adds 2 points and a mood match adds 1 point. The system also gives up to 2 points based on how close the song's energy level is to the user's target energy.

If the user provides an acoustic preference, the system can add another 0.5 points when the song's acousticness matches that preference.

After every song has been scored, the program sorts the songs from highest to lowest score and returns the top recommendations.

This is a content-based approach because the model uses song attributes instead of behavior from other users.

## 4. Data  

The catalog contains 18 synthetic songs.

The available song features include:

genre

mood

energy

tempo

valence

danceability

acousticness

The original catalog contained 10 songs. 
I added additional songs to increase the variety of genres and moods, 
including acoustic, EDM, indie, R&B, folk, and additional rock, pop, and ambient tracks.

The dataset is still very small compared with a real music catalog. 
It also does not contain lyrics, language, release year, popularity, listening history, or detailed artist information.

## 5. Strengths  

The model works well when the user has clear preferences that are represented in the catalog.

For example, a user who wants happy, high-energy pop music tends to receive upbeat pop tracks near the top of the ranking.

The Chill Lofi profile also gives reasonable results because the catalog contains several low-energy lofi songs.

The recommendation explanations make the system easier to understand because the user can see which factors contributed to each score.

## 6. Limitations and Bias 

The system uses exact genre and mood matches. A song that could reasonably fit multiple genres or moods may receive a lower score simply because its stored label does not exactly match the user's preference.

The catalog is also very small and synthetic, so some genres have more representation than others.

The manually selected scoring weights introduce another form of bias. For example, giving genre two points can cause genre matches to rank higher even when another song has a closer energy level.

The system does not learn from user feedback. A real user could repeatedly skip a recommendation and the model would continue making the same recommendation.
## 7. Evaluation  

I tested the recommender with several user profiles:

- High-Energy Pop

- Chill Lofi

- Deep Intense Rock

- A conflicting high-energy ambient profile

The High-Energy Pop and Chill Lofi profiles produced noticeably different recommendations, 
which showed that the system was responding to the user's preferences.

The rock profile favored intense, high-energy rock songs, 
while the lofi profile shifted toward lower-energy and more acoustic tracks.

The conflicting profile was useful as an edge case 
because no song could strongly satisfy every preference 
at the same time.

I also performed a weight experiment 
by reducing the genre score and increasing the importance of energy. 
This caused high-energy songs from other genres to move higher in the ranking. 
The experiment showed that recommendation results can change significantly 
based on how the scoring weights are chosen.
## 8. Future Work  

If I continued this project, I would:

- Add a much larger and more diverse music catalog.

- Allow multiple favorite genres and moods instead of exact single-value matches.

- Use user behavior such as likes, skips, and listening history to adjust future recommendations.

- Add diversity logic so the top five recommendations are not too similar.

- Explore collaborative filtering or learned similarity instead of relying only on manually chosen scoring weights.

## 9. Personal Reflection  

The biggest thing I learned is that recommendation systems are strongly influenced by how data is represented and weighted. 
Before this project, I thought recommendations mostly required complicated machine-learning models. 
I was surprised that a simple scoring system could already produce results that felt somewhat personalized.

AI was useful for brainstorming scoring ideas, generating edge cases, and explaining different approaches. 
However, I still needed to check the code and run experiments myself. 
A suggestion can sound reasonable but still produce rankings that do not match the intended behavior.

If I continued the project, I would experiment with real user feedback and a larger dataset. 
I would also like to compare this hand-written scoring approach with a recommendation model that learns preferences automatically.