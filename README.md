# sTODO

sTODO is a program that allows you to keep a list of your tasks. You can easily
add, edit and save your cases.

## Introduction

Welcome screen responsive view

![Tap&Play responsive view](./assets/docs/is-responsive-welcome.png)

Responsive view after a player enter them name

![Tap&Play responsive view](./assets/docs/is-responsive-after-authorization.png)

A site with an online game Blatsk Yatsk. For ease of use, the site is designed
taking into account the screen sizes of most devices.

You can [visit our site here.](https://barkode.github.io/TapAndPlay/)

## Content

- [sTODO](#stodo)
  - [Introduction](#introduction)
  - [Content](#content)
  - [User Experience (UX)](#user-experience-ux)
    - [User stories](#user-stories)
  - [Design](#design)
    - [Website structure](#website-structure)
    - [Wireframes](#wireframes)
    - [Color Scheme](#color-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Accessibility](#accessibility)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries \& Programs Used](#frameworks-libraries--programs-used)
  - [Features](#features)
    - [Favicon](#favicon)
    - [Welcome Screen](#welcome-screen)
    - [Main Page](#main-page)
    - [Logo](#logo)
    - [Statistic Module](#statistic-module)
    - [Clock Module](#clock-module)
    - [Buttons Module](#buttons-module)
    - [Local Storage](#local-storage)
    - [Clear All Data Module](#clear-all-data-module)
    - [Footer](#footer)
    - [Error page](#error-page)
  - [Testing](#testing)
    - [Testing user stories](#testing-user-stories)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JS Validation](#js-validation)
    - [Lighthouse Performance Tests](#lighthouse-performance-tests)
      - [Desktop](#desktop)
      - [Mobile](#mobile)
    - [Manual Testing](#manual-testing)
      - [Testing form validation](#testing-form-validation)
    - [Further Testing](#further-testing)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
    - [Github pages](#github-pages)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Making a Local Clone](#making-a-local-clone)
  - [Future improvements](#future-improvements)
  - [Credits](#credits)
    - [Code \& Content](#code--content)
    - [Media](#media)
    - [Acknowledgment](#acknowledgment)

## User Experience (UX)

### User stories

1. As a user, I want to be able to easily understand the rules of Blackjack so
   that I can start playing quickly. Acceptance Criteria:

- Clear and concise instructions are available on the main menu or accessible
  within the game.
- Instructions include the objective of the game, card values, and basic
  gameplay mechanics.

2. As a user, I want to be able to start a new game of Blackjack easily.

Acceptance Criteria:

- A prominent "Start Game" button is available on the main page.
- Upon starting, the game initializes with a shuffled deck and deals the initial
  cards.

3. As a user, I want to be able to see my current hand and the dealer’s visible
   card so that I can make informed decisions.

Acceptance Criteria:

- The user’s hand is displayed clearly on the screen.
- The dealer’s visible card is shown, with the other card face-down.

4. As a user, I want to have options to 'Hit', 'Stand', or 'Rules' during my
   turn so that I can play the game strategically.

Acceptance Criteria:

- Buttons for 'Hit', 'Stand', and 'Info' are available and functional.

- The game provides feedback for each action.

5. As a user, I want to see the outcome of each round and understand why I won
   or lost so that I can learn and improve my strategy.

Acceptance Criteria:

- The game displays the outcome of each round (win, lose).
- A brief explanation is provided.

6. As a user, I want to be able to track my winnings and losses so that I can
   manage my betting strategy.

Acceptance Criteria:

- A summary of wins and losses is available, either per game or session.

7. As a user, I want the game interface to be visually appealing and intuitive
   so that I can have an enjoyable gaming experience.

Acceptance Criteria:

- The game has a clean, user-friendly interface with attractive graphics.
- The layout is intuitive, with clear buttons and easily readable text.

8. As a user, I want to be able to read the rules of the game.

Acceptance Criteria:

- On the main page there is a button that shows the game rules page.

9. As a user I want to be able to delete all stats and title.

Acceptance Criteria:

- There is a button on the site that deletes all statistics and the username.

- After deleting the statistics and username, you will be redirected to the
  welcome page.

10. As a user, after entering a name, I want the site to remember my name and
    game statistics.

Acceptance Criteria:

- After entering the name, the username should be displayed in the statistics.

- At the next login to the site, the user gets to the main screen with the game
  instead of the welcome screen.
- The next time you log in to the site, you will see your game statistics and
  your name on the main screen.

  [Back to top](#content)

## Design

The design of the game is made in a classic style. The site is built on the
principles of simplicity and functionality. Time was also devoted to creating a
concise design and ease of use of the game.

[Back to top](#content)

### Website structure

The site consists of 2 pages.

- A welcome window greets the user. The user is asked to enter his name and
  confirm that he is already 18 years old.

- The main page displays the main logo and the game field. Statistics are
  located in the upper left corner. At the top and in the center is the clock.
  There are 4 buttons below.

- The start button is responsible for starting the game. The player and the
  dealer are dealt 2 cards each and the game begins.

- The kick and stand buttons control the game. Pressing the button adds another
  card to the player. The stand button informs the player that no more cards are
  needed. Now the dealer takes the cards.

- The rules button displays the rules of the game. At the very bottom of the
  rules window there is a button that allows you to forget all data (username
  and game statistics).

- The second page is a 404 error page. This page is displayed if the user wants
  to open a page that does not exist.

[Back to top](#content)

### Wireframes

Balsamiq was used to create the wireframes during the design process

![Balsamiq welcome screen](./assets/docs/Welcome%20page.png)

![Balsamiq main screen](./assets/docs/Main%20page.png)

![Balsamiq rules screen](./assets/docs/Rules%20screen.png)

[Back to top](#content)

### Color Scheme

![Project used colors](./assets/docs/colors.png)

I was inspired by
[uzaymacar github](https://github.com/uzaymacar/blackjack-with-gui/blob/master/README.md)

[Back to top](#content)

### Typography

Geometric sans serif typefaces have always been popular, and with support for
both the Devanagari and Latin writing systems, BioRhyme is an internationalist
addition to the genre. Many of the Latin glyphs (such as the ampersand) are more
constructed and rationalist than is typical. The font family
'[BioRhyme](https://fonts.google.com/specimen/BioRhyme?query=BioRhyme)' was
downloaded and used from Google Fonts, as it provides an easy-on-the-eye font.
This font was used for all text across the website.

![BioRhyme font](./assets/docs/fonts.png)
![BioRhyme font](./assets/docs/fonts-1.png)

[Back to top](#content)

### Imagery

All images were downloaded from free resources. Pictures for the site were
downloaded from such resources as [Pixels](https://www.pexels.com/),
[Pixabay](https://pixabay.com/) and [Unsplash](https://unsplash.com/).

Icons for the project were found on [FontAwesome](https://fontawesome.com/) and
[FLATICON](https://www.flaticon.com/).

All image sizes were edited using [squoosh](https://squoosh.app/).

[Back to top](#content)

### Accessibility

The following has been done to ensure that the website is as accessible friendly
as possible.

- Using semantic HTML.
- Using descriptive alt attributes on images on the site.
- Ensuring that there is a sufficient color contrast throughout the site.

[Back to top](#content)

## Technologies Used

### Languages Used

- HTML5 - used to write structure and foundation of code for website.
- CSS3 - used for styling all content and page structure on site.
- Git - used to track code changes and as a version control system.
- JavaScript - JavaScript was used as the main programming language to ensure
  the site's interactivity. The logic of the game is also written in JavaScript.
- VSCOde - used as a main IDE.

[Back to top](#content)

### Frameworks, Libraries & Programs Used

- [Google fonts](https://fonts.google.com/knowledge) and
  [google webfonts helper](https://gwfh.mranftl.com/fonts)

  Google fonts and google webfonts helper were used to integrate the 'Poppins'
  font into the style.css file which is used on all pages throughout the project

- [Font Awesome](https://fontawesome.com/)

  Font Awesome was used on all pages throughout the website to add icons for
  aesthetic and UX purposes.

- [Git](https://gitpod.io/)

  Git was used for version control by utilizing the Gitpod terminal to commit to
  Git and Push to GitHub.

- [GitHub](https://github.com/)

  GitHub is used to store the projects code after being pushed from Git.

- [Balsamiq](https://balsamiq.com/wireframes/)

  Balsamiq was used to create [wireframes](#wireframes) for website.

- [Figma](https://www.figma.com/community)

  Figma was used to find inspiration.

- [Visual Studio Code](https://code.visualstudio.com/)

  Used Visual Studio Code as a main IDE.

[Back to top](#content)

## Features

The site contains 2 pages. All pages have a favicon, title, green background.

### Favicon

![Tap&Play favicon image](./assets/docs/favicon.png)

An icon suitable for the subject was found on the
[FlatIcon](https://www.flaticon.com/free-icon/numerology_9288700?term=numerology&page=1&position=4&origin=search&related_id=9288700)
resource.

[Back to top](#content)

### Welcome Screen

![Tap&Play Welcome screen image](./assets/docs/welcome-screen-desk.png)

On the welcome screen, you can enter the player's name and confirm that they are
18 years or older.

Welcome screen on tablet

![Tap&Play Welcome screen image tablet](./assets/docs/welcome-screen-tabl.png)

Welcome screen on mobile

![Tap&Play Welcome screen image mobile](./assets/docs/welcome-screen-mobi.png)

[Back to top](#content)

### Main Page

![Tap&Play Main Page image](./assets/docs/main-page-desk.png)
![Tap&Play Main Page image](./assets/docs/main-page-1-desk.png)

The site was developed taking into account the requirements for adaptability.
Games look good on both desktop and mobile devices.

![Tap&Play Main Page image](./assets/docs/main-page-tabl.png)

![Tap&Play Main Page image](./assets/docs/main-page-mobi.png)

[Back to top](#content)

### Logo

![Tap&Play Logo image](./assets/docs/bg-logo.png)

The logo was created in Figma. The images was downloaded from
[Pixabay](https://pixabay.com/vectors/joker-clown-medieval-jester-6770391/)

The image was chenged in [Figma App](https://www.figma.com/) The logo has a
transparent background.

[Back to top](#content)

### Statistic Module

![Statistic module image](./assets/docs/statistic-desk.png)

The statistics module was written. It displays player and dealer win statistics.
Local storage was used to store statistics.
![Statistic module image](./assets/docs/statistic-tabl.png)

The statistics module was developed taking into account the principles of
adaptive layout.

![Statistic module image](./assets/docs/statistic-mobi.png)

[Back to top](#content)

### Clock Module

The clock module has been designed and developed for user convenience. It is
located at the top of the site in the center.

![clock module image](./assets/docs/statistic-desk.png)

Like other modules, the clock module is designed with different user screen
widths in mind.

![Clock module image](./assets/docs/statistic-tabl.png)

![Clock module image](./assets/docs/statistic-mobi.png)

[Back to top](#content)

### Buttons Module

The button module makes the buttons invisible depending on the stage of the
game. At the very beginning, only the start and rls buttons are closed. After
the game starts, the start button becomes inactive, and the kick and stand
buttons become active.

![Buttons module image](./assets/docs/btn-desk.png)

On mobile

![Buttons module image](./assets/docs/btn-mobi.png)

Button start active

![Buttons module image](./assets/docs/buttons-1-start.png)

Button start inactive

![Buttons module image](./assets/docs/buttons-2-deal-cards.png)

[Back to top](#content)

### Local Storage

The module was designed to store username and game statistics in local storage.
During the first visit, the user's name is written to the local memory, after
that the user is not shown the welcome screen

![Clear all data module image](./assets/docs/read-rules.png)

[Back to top](#content)

### Clear All Data Module

The module was designed for user convenience. The button is located at the
bottom of the rules window. When you press the button, all game data and user
name will be deleted.

![Clear all data module image](./assets/docs/read-rules.png)

[Back to top](#content)

### Footer

![Tap&Play Footer image](./assets/docs/footer-desk.png)

The footer is designed taking into account the requirements for adaptability.
Games look good on both desktop and mobile devices.

![Tap&Play Footer image](./assets/docs/footer-tabl.png)

The link in the footer leads to the game code page.

![Tap&Play Footer image](./assets/docs/footer-mobi.png)

[Back to top](#content)

### Error page

![Error Page](./assets/docs/error-page.png)

An error page notifies the user of an error. Also, the user can return to the
main page. The page is also made taking into account different device widths.

[Back to top](#content)

## Testing

### Testing user stories

**User Story 1:** Understand Rules of Blackjack

**Acceptance Criteria:**

Clear and concise instructions available on the main menu or accessible within
the game. Instructions include the objective of the game, card values, and basic
gameplay mechanics.

**Testing:**

Main Menu: Navigated to the main menu and found a clearly labeled "Rules" or
"Instructions" button.

Instructions: Clicked on the "Rules" button and verified that the instructions
were clear, concise, and covered the objective of the game, card values, and
basic gameplay mechanics.

Result: **Pass**

**User Story 2:** Start a New Game of Blackjack

**Acceptance Criteria:**

A prominent "Start Game" button is available on the main page. Upon starting,
the game initializes with a shuffled deck and deals the initial cards.

**Testing:**

Start Button: Located a prominently displayed "Start Game" button on the main
page. Game Initialization: Clicked the "Start Game" button and confirmed that
the game initialized with a shuffled deck and dealt the initial cards to both
the player and the dealer.

Result: **Pass**

**User Story 3:** See Current Hand and Dealer’s Visible Card

**Acceptance Criteria:**

The user’s hand is displayed clearly on the screen. The dealer’s visible card is
shown, with the other card face-down.

**Testing:**

User’s Hand: Verified that the user’s hand was clearly displayed on the screen.
Dealer’s Card: Confirmed that the dealer’s visible card was shown with the
second card face-down.

Result: **Pass**

**User Story 4:** Options to 'Hit', 'Stand', or 'Rules'

**Acceptance Criteria:**

Buttons for 'Hit', 'Stand', and 'Info' are available and functional. The game
provides feedback for each action.

**Testing:**

Buttons Availability: Ensured that 'Hit', 'Stand', and 'Info' buttons were
present and clearly labeled. Functionality: Tested each button to confirm they
performed the correct actions and provided appropriate feedback.

Result: **Pass**

**User Story 5:** Outcome of Each Round

**Acceptance Criteria:**

The game displays the outcome of each round (win, lose). A brief explanation is
provided.

**Testing:**

Round Outcome: Played a few rounds and verified that the game displayed the
outcome (win, lose) after each round. Explanation: Confirmed that a brief
explanation of the outcome was provided.

Result: **Pass**

**User Story 6:** Track Winnings and Losses

**Acceptance Criteria:**

A summary of wins and losses is available, either per game or session.

**Testing:**

Summary Display: Checked the interface for a summary of wins and losses.
Accurate Tracking: Verified that the summary accurately tracked the results of
multiple games or sessions.

Result: **Pass**

**User Story 7:** Visually Appealing and Intuitive Interface

**Acceptance Criteria:**

The game has a clean, user-friendly interface with attractive graphics. The
layout is intuitive, with clear buttons and easily readable text.

**Testing:**

Visual Appeal: Evaluated the game’s graphics and overall aesthetic appeal.
User-Friendly: Assessed the intuitiveness of the layout, button placement, and
readability of the text.

Result: **Pass**

**User Story 8:** Read the Rules

**Acceptance Criteria:**

On the main page, there is a button that shows the game rules page.

**Testing:**

Rules Button: Located the button on the main page that leads to the game rules.
Accessing Rules: Clicked the button and verified that it navigated to the game
rules page.

Result: **Pass**

**User Story 9:** Delete All Stats and Title

**Acceptance Criteria:**

There is a button on the site that deletes all statistics and the username.
After deleting the statistics and username, you will be redirected to the
welcome page.

**Testing:**

Delete Button: Found the button for deleting all statistics and the username.
Functionality: Clicked the button and confirmed that it deleted the statistics
and username, then redirected to the welcome page.

Result: **Pass**

**User Story 10:** Remember Name and Game Statistics

**Acceptance Criteria:**

After entering the name, the username should be displayed in the statistics. At
the next login to the site, the user gets to the main screen with the game
instead of the welcome screen. The next time you log in to the site, you will
see your game statistics and your name on the main screen.

**Testing:**

Name Display: Entered a name and verified that it was displayed in the
statistics. Remembering Data: Logged out and back in to confirm that the site
remembered the username and statistics, and navigated directly to the main game
screen.

Result: **Pass**

[Back to top](#content)

### HTML Validation

![HTML Validator OK](./assets/docs/w3c-html-validator.png)

All informational messages refer to the trailing slash at the end of empty
elements. This is a feature of the Prettier expansion.

[Back to top](#content)

### CSS Validation

![CSS Validator](./assets/docs/w3c-validation.png)

The document has been verified. No errors were found. Non-critical comments were
found.

[Back to top](#content)

### JS Validation

![JS Validator](./assets/docs/indexjs-jshint.png)

JSHint validator. Index.js

![JS Validator](./assets/docs/uijs-jshint.png)

JSHint validator. UI.js

![JS Validator](./assets/docs/utilsjs-jshint.png)

JSHint validator. Utils.js

![JS Validator](./assets/docs/gameCountsjs-jshint.png)

JSHint validator. GameCounts.js

[Back to top](#content)

### Lighthouse Performance Tests

#### Desktop

![Index Page Lighthouse image](./assets/docs/lh-desk-index.png)

![Index Page Lighthouse image](./assets/docs/lh-desk-entered.png)

[Back to top](#content)

#### Mobile

![Index Page Lighthouse](./assets/docs/lh-mobi-index.png)

![Index Page Lighthouse](./assets/docs/lh-mobi-entered.png)

[Back to top](#content)

### Manual Testing

| Test                                                    | Steps                                                   | Expected                                                       | Actual      |
| ------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------- | ----------- |
| Enter Player name without click checkbox                | Enter player name and do not click checkbox             | Enter warning message                                          | As expected |
| Disabled button on welcome screen                       | Try to click button "Lets Play"                         | Button is inactive                                             | As expected |
| Form shows warning message when user doesn't enter name | click lets play button                                  | shows warning message                                          | As expected |
| Don't show welcome screen after user enter name         | refresh the page                                        | user enter to main page                                        | As expected |
| The clock shows current time                            | enter to main page                                      | The clock shows current time                                   | As expected |
| The player name saves in local storage                  | Enter name on welcome screen. Refresh page              | User name shows in statistic corner                            | As expected |
| Hit and Stand buttons disabled                          | enter to main page                                      | Hit and stand buttons are disabled                             | As expected |
| The game starts                                         | Enter to main page and click start button               | 2 cards will be dealt                                          | As expected |
| Hit Button                                              | click hit button                                        | the player will be dealt one card                              | As expected |
| Stand button                                            | Click stand button                                      | the dealer will be dealt several cards                         | As expected |
| Rules button                                            | click rules button                                      | displays screen with rules                                     | As expected |
| Clear all statistic data button                         | click rules button after click clear all statistic data | delete all info from local storage. Redirect to welcome screen | As expected |
| Save statistic                                          | play several games. Refresh the page                    | saved statistics in the statistics module will be shown.       | As expected |
| Show win-lose message                                   | Play several games                                      | show modal window with name who win                            | As expected |

#### Testing form validation

- Form button not active

![Form button not active image](./assets/docs/form-1-button-not-active.png)

- Input field on focus

![Form button not active image](./assets/docs/form-2-button-not-active.png)

- The Player writes they name

![Form button not active image](./assets/docs/form-3-Player-enter-name.png)

- The Player does't click checkbox

![Form button not active image](./assets/docs/Form-4-not-confirm-age.png)

- The Player delete they name and tray to confirm form.

![Form button not active image](./assets/docs/form-5-not-enter-name.png)

[Back to top](#content)

### Further Testing

In the future, it is possible to check the functionality of the site for further
optimization.

Testing on more devices to find optimal values.

Using more devices to determine optimal color shades.

[Back to top](#content)

## Bugs

- When creating the site, it was difficult to come up with a beautiful and
  simple site design. I looked at many sites for inspiration.
- In the process of writing the code, it was difficult to choose a simple and
  beautiful effect that would fit the theme of the site.
- During performance testing, it was found that all images needed to be reduced
  in size.
- Need to fix performance on mobile devices.
- Not smooth card animation

[Back to top](#content)

## Deployment

### Github pages

- This project was deployed to GitHub Pages using the following steps

  - Log in to GitHub and locate the GitHub Repository
  - At the top of the Repository (not top of page), locate the "Settings" Button
    on the menu.
  - Scroll down the Settings page until you locate the "GitHub Pages" Section.
  - Under "Source", click the dropdown called "None" and select "Main Branch".
  - The page will automatically refresh.
  - Scroll back down through the page to locate the now published site link in
    the "GitHub Pages" section.
  - live link for the page can be found here
    [Bake's JOY](https://barkode.github.io/bake-with-joy/)

[Back to top](#content)

### Forking the GitHub Repository

- By forking the GitHub Repository we make a copy of the original repository on
  our GitHub account to view and/or make changes without affecting the original
  repository by using the following steps
- Log in to GitHub and locate the GitHub Repository
- At the top of the Repository (not top of page) just above the "Settings"
  Button on the menu, locate the "Fork" Button.
- You should now have a copy of the original repository in your GitHub account.

[Back to top](#content)

### Making a Local Clone

- Log in to GitHub and locate the GitHub Repository
- Under the repository name, click "Clone or download".
- To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
- Open Git Bash
- Change the current working directory to the location where you want the cloned
  directory to be made
- Type git clone, and then paste the URL you copied in Step 3.
  - $ git clone <https://github.com/YOUR-USERNAME/YOUR-REPOSITORY>
- Press Enter. Your local clone will be created.

[Back to top](#content)

## Future improvements

- Add a selection from multiple card collection.
- Add sounds effects.
- Add a new functionality with double button.
- Add a new functionality with split button.
- Add the ability to make bets.

[Back to top](#content)

## Credits

### Code & Content

- [Stack overflow](https://www.stackoverflow.com/),
  [MDN Web Docs](https://developer.mozilla.org/en-US/),
  [W3 Schools](https://www.w3schools.com/),
  [LogRocket](https://blog.logrocket.com/)

  Help in solving problems. Help in implementing best practices. Search for the
  best practices. Good documentation.

- [Figma](https://www.figma.com/design/fDlsHwelyuOVsfUmCzm3dA/%D0%A1%D1%83%D1%87%D0%B0%D1%81%D0%BD%D1%8F-%D0%BF%D0%B5%D0%BA%D0%B0%D1%80%D0%BD%D1%8F?node-id=0-1&t=VeNx8IUKIo2EOdRB-0)

  Figma as a search platform for inspiration and as a graphic editor.

- Love running project from [Code Institute](https://codeinstitute.net/ie/)

  I was inspired by the Gallery page and some of the code for the site's gallery
  was taken.

- [UIVerse](https://uiverse.io/)

  credits for hover effect over images and other effects for elements goes to

- [LogRocket](https://blog.logrocket.com/responsive-image-gallery-css-flexbox/)

  credits for gallery goes from

- [Google Maps](https://www.google.ie/maps/)

  Was used to show the location

- [ZelL Liev](https://medium.com/free-code-camp/how-to-check-if-an-input-is-empty-with-css-1a83715f9f3e)

  A piece of code to implement form validation using CSS and regular
  expressions.

- [freeformatter.com](https://www.freeformatter.com/css-minifier.html#before-output)

  It was used to minimize css

- [W3C Markup Validator](https://validator.w3.org/)

  This service was used to validate HTML files

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

  This service was used to validate CSS files

- [JavaScript Info](https://javascript.info/)

  There is a lot of js documentation on this site

- [Google](https://google.com)

  Search engine to find information

- [ChatGPT](https://chatgpt.com/)

  As a good helper in finding information

[Back to top](#content)

### Media

- [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/)

  Images on the site are taken from these resources.

- [app-logo](https://app.logo.com/)

  the resource is used to generate an idea and automatically create a logo for
  the site

- [MDN Web Docs](https://developer.mozilla.org/en-US/)

  Instructions on how to connect the favicon to the site have been taken.

- [FlatIcon](https://www.flaticon.com/)

  The icon for the site was found on this resource.

- [Squoosh](https://squoosh.app/)

  The service was used to optimize pictures

- [FLATICON](https://www.flaticon.com/free-icon/numerology_9288700?term=dice&page=1&position=59&origin=search&related_id=9288700)

  Site favicon

[Back to top](#content)

### Acknowledgment

- I want to thank my tutor [Marko Tot](https://github.com/tmarkec) for his daily
  care and help. For the desire to create a favorable atmosphere for learning
  and creativity.
- I would like to thank my mentor, Anthony Ugwu, for his helpful advice on
  writing the project.
- I would also like to thank the entire
  [Code Institute](https://codeinstitute.net/ie/) and
  [Kerry College](https://kerrycollege.ie/) for giving me the opportunity to
  study and participate in this project.

[Back to top](#content)
