# Alien Invasion

## Project Links

- [Github Repo](https://github.com/poppan2/alien-invasion)

## Project Description

Being a game lover, and wanting to be a game dev myself, I've always wanted to build a game. Henceforth, I'm stretching my skills to build an Alien Invasion game using pygame(Python library)). This game will have a ship that moves right and left, and fires bullets to destroy a fleet of aliens in response to player input. Inspired by Galaga game. 

## Wireframes

- [Game Page](https://imgur.com/N0VpPAj)

### MVP/PostMVP

#### MVP

- Create a ship that can move left/right 
- Create a fleet of aliens to destroy 
- Continue to make refinements, such as setting limits on the number of ships a user can use, 
  increasing the difficulties, etc...
- Add a Scoreboard

#### PostMVP

- Add Bonus features such as increase in fire power/difficulties, restore lives, Leader Board etc ...

## Components

| Component                 |                                  Description                                  |
| ------------------------- | :---------------------------------------------------------------------------: |
| Ship                      | Create a space ship that can move left, right, up, down                       |
| Bullets                   | Allow the ship to shoot bullets                                               |
| Aliens                    | Create a fleet of aliens that can move right, left, down & kill the ship      |
| Game Page                 | View for user to play the game itself. Contain a ship, aliens, & ascore board |
| Score                     | User score calculated based on number of aliens destroyed                     |
| Leaderboard Page(PostMVP) | Leaderboard of user scores, sorted by highest to lowest                       |


| Component           | Priority | Estimated Time | Actual Time |
| ------------------- | :------: | :------------: | :---------: |
| Setting up App      |    H     |      2hrs      |     0hrs    |
| Setting up Routes   |    H     |      2hrs      |     0hrs    |
| Setting up game     |    H     |     48hrs      |    25hrs    |
| Game functionality  |    H     |     10hrs      |    35hrs    |
| User Lives          |    M     |      2hrs      |     2hrs    |
| Score               |    M     |      3hrs      |     3hrs    |
| Leaderboard         |    L     |     10hrs      |     0hrs    |
| Bonus Functionality |    M     |     15hrs      |     0hrs    |
| Total               |          |     92hrs      |    65hrs    |

## Additional Libraries
Pygame

## Code Snippet

Use this section to include a brief code snippet of functionality that you are proud of and a brief description. Code snippet should not be greater than 10 lines of code.

```
def change_direction(ai_settings, screen, aliens):
    """Change direction of aliens upon reaching the screen edges"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        # Check if an alien is at the edge of the screen
        if (alien.rect.right >= screen_rect.right) or alien.rect.left <= 0:
        # if alien.check_alien_edges():
            for alien in aliens.sprites():
                # Drop down by the unit of alien_speed 
                alien.rect.y += ai_settings.alien_speed_y
            # Change the direction of the alien fleet
            ai_settings.alien_direction *= -1
            break
```
This code checks the aliens against the screen edges and move down then change direction.