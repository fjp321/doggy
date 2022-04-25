# Doggy Recipes Generation

## What is Doggy

<<<<<<< HEAD
## Usage

## Design Choices

### Why json instead of SQL

### Why no windows support

### Why no GUI

## Resources
=======
Doggy is a python library for the creation and management of recipe databases. It also has functionality for generating randomized grocery lists for a specified number of recipes. 

## Usage

To use this library, simply add doggy.py to where ever your python path points. This library will be added to pypi, and when this is implemented, We will update the README. 

## [Documentation](https://fjp321.github.io/doggy)

## Design Choices

### Why SQL instead of json

The reason for sql, and  by extension python, is for the [sqlite](https://en.wikipedia.org/wiki/SQLite) python library, and a database is the better format for a scalability. The goal of Doggy is to manage potentially hundreds of recipes and ingredients, so scalability is incredibly important. 

### Why no GUI

There is no gui, but there is a command line helper script, planet. The reason this is prioritized over a gui is so that adding this helper script to a [cron job](https://en.wikipedia.org/wiki/Cron)is as simple as possible. If you want a gui, please look into making one yourself! Consider using [pyqt](https://en.wikipedia.org/wiki/PyQt) If you run into any issues regarding the doggy functions, please feel free to open an issue.

## Resources

SQLite: https://en.wikipedia.org/wiki/SQLite
Cron: https://en.wikipedia.org/wiki/Cron
Pyqt: https://en.wikipedia.org/wiki/PyQt

## [Planned Updates]()
>>>>>>> staging

## Contributors
fjp321
Spencer-Potter
