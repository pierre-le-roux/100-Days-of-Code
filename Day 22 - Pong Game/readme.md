# Pong Game

## Run the game
    main.py

## Classes

### Player
    Movement
        - Up and down the side of the screen
        - Stay within boarders
    Hit the ball
        - Return the ball
            - Incoming side
                - Ball is returned with the same outgoing angle as the incoming angle
            - Opposite side
                - Ball is returned with the same outgoing angle as the incoming angle, but flipped horisontally

### Ball
    Movement
        - Constant rate
        - Stay within boarders
    Boundry
        - Continues the angle of approach
    Goal
        - Ball is stopped after going past a player

### Scoreboard
    Score
        - Keeping score of each player
        - If ball goes out the screen behind player the other player gets a point
