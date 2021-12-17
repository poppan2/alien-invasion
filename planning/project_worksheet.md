# Alien Invasion

## Project Links

- [Github Repo](https://github.com/poppan2/alien-invasion)
- [Deployed Site]()

## Project Description

Being a game lover, and wanting to be a game dev myself, I've always wanted to build a game. Henceforth, I'm stretching my skills to build an Alien Invasion game using Python (Pygame). This game will have a ship that moves right and left, and fires bullets to destroy a fleet of aliens in response to player input. Inspired by Battlestar Galactica/Galaga game. 

## Wireframes

- [Landing Page](https://imgur.com/witmlcG)
- [Game Page](https://imgur.com/N0VpPAj)
- [Leaderboard Page (PostMVP)](https://imgur.com/oOcwsk0)
- [About Page](https://imgur.com/lGciait)

## React Architecture Tree
I am not certain if I can integrate React into Python, I'll have to figure that out. However, the following would
be the structure I'd use to design my app regardless of a framework/library.  

- App
  - Header
  - Body
    - Menu/Landing Page
    - Game Page
      - Score
      - Timer
      - Grid
    - Leaderboard Page
      - User
    - About Page
  - Footer

### MVP/PostMVP

#### MVP

- Set up a landing page with info about the game
- Create a ship that can move left/right (Haven't)
- Create a fleet of aliens to destroy (using dictionaries in Python)
- Continue to make refinements, such as setting limits on the number of ships a user can use, 
  increasing the difficulties, etc...
- Add a Scoreboard and a Leader Board
- Finally, add an about page to give a deep explanation about the game, inspirations and contact links

#### PostMVP

- Add Bonus features such as increase in fire power/difficulties, restore lives etc ...

## Components

| Component                 |                                  Description                                  |
| ------------------------- | :---------------------------------------------------------------------------: |
| App                       |                       Contains Header, Body, and Footer                       |
| Header                    |         Include nav bar linking to Menu, Game, Leaderboard          |
| Body                      |              In depth view of Menu, Game, Leaderboard               |
| Footer                    |                                Copyright text                                 |
| Menu/Landing Page         |                  View for user to get familiar with the game                   |
| Game Page                 |  View for user to play the game itself. Contain a ship, aliens, & ascore board   |
| Score                     |              User score calculated based on number of aliens destroyed        |
| About                     | Description of the game, inspiration, and link to other game and github repos |
| Leaderboard Page(PostMVP) |      Leaderboard of user scores, sorted by highest to lowest      |
| User                      |                              User name and score                              |


| Component           | Priority | Estimated Time | Actual Time |
| ------------------- | :------: | :------------: | :---------: |
| Setting up App      |    H     |      2hrs      |             |
| Setting up Routes   |    H     |      2hrs      |             |
| Setting up game     |    H     |     48hrs      |             |
| Game functionality  |    H     |     10hrs      |             |
| User Lives          |    M     |      2hrs      |             |
| Score               |    M     |      3hrs      |             |
| Leaderboard         |    L     |     10hrs      |             |
| Bonus Functionality |    M     |     15hrs      |             |
| Total               |          |     95hrs      |             |

## Additional Libraries
Pygame

## Code Snippet

Use this section to include a brief code snippet of functionality that you are proud of an a brief description. Code snippet should not be greater than 10 lines of code.

```
function reverse(string) {
	// here is the code to reverse a string of text
}
```