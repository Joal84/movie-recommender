# MOVIE RECOMMENDER

A movie recommendation website powered by an unsupervised learning non-negative matrix factorization algorithm. This project provides users with personalized movie recommendations based on their viewing history and preferences.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Algorithm](#algorithm)
- [Contributing](#contributing)

## Introduction

In a world overflowing with movies, it's often challenging to decide what to watch next. This movie recommendation website aims to solve that problem by leveraging the power of unsupervised learning. Using non-negative matrix factorization, the algorithm analyzes user preferencesto generate personalized movie recommendations.

## Features

- User-friendly web interface for discovering and selecting movies.
- User-specific movie recommendations.
- Movie details including synopsis and artwork.

## Getting Started

To get this project up and running on your local machine, follow these steps:

### Prerequisites

- Python 3.10.9

### Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/Joal84/movie-recommender.git
   cd movie-recommender
   ```

   
2. Create and activate a virtual environment (optional but recommended):
   ```
   virtualenv venv
   source venv/bin/activate
   ```
3. Install the project dependencies:
   ```
   cd flask
   pip install -r requirements.txt
   ```
4. Start the development server:
   ```
   python app.py
   ```
## Usage
- Rate and write the name of 5 movies than submit your choices
- A selection of 8 movies will be presented to you

## Algorithm
The movie recommendation algorithm in this project is based on non-negative matrix factorization (NMF). NMF is a popular technique for collaborative filtering in recommendation systems. It decomposes the user-movie interaction matrix into two lower-dimensional matrices, which capture latent features of users and movies. These latent features are used to make movie recommendations for each user.

The model was trained on small MovieLens dataset (ml-latest-small) which describes 5-star rating and free-text tagging activity from [MovieLens](http://movielens.org). It contains 100836 ratings and 3683 tag applications across 9742 movies. These data were created by 610 users between March 29, 1996 and September 24, 2018. This dataset was generated on September 26, 2018.
Users were selected at random for inclusion. All selected users had rated at least 20 movies. 

## Contributing
Contributions to this project are welcome! If you have ideas for improvements, bug reports, or new features, please open an issue or submit a pull request. For major changes, please discuss them in the project's issue tracker.
