
## Movie Reccomender
This repo contains codes for the **movie recommender system**.
<br>
The dataset was available on Kaggle by the name of tmdb - the movie database. It is a quite an elaborate dataset and pretty much sufficed for my task. <br>
- Algoritthm employed is `KMeans` and from elbow chart , the optimal choice came to ke `k=20` and PCA variances had been used to establish significant attributes to work with. 
- To recommend similar movies for a particular movie of our dataset, I first identified which cluster the movie belongs to and then computed Euclidean distance of that movie with all the other movies of the same cluster. Then, presenting a list of five movies which are closest to that particular movie.

<!-- <br> some ranting 😝<br> 
  A Recommender System is class of information filtering system that tries to predict the rating or preference of a product for an user. On a more simple note, a recommender system tries to understand the user’s interests and provide contents to the user based on its understanding. Now- a-days the usage of good recommender system is universal, be it in recommending similar songs to the user (Spotify), similar movies or tv-shows to the user (Netflix, Amazon Prime etc.), similar videos to the users (YouTube, TikTok etc). It has also been developed in many other areas such as online-shopping, research articles, collaborators, and financial services. -->
<br>
cheers 🙌

