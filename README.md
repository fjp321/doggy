# Doggy Recipes Generation

## What is Doggy

Doggy is a python library for the creation and management of recipe databases. It also has functionality for generating randomized grocery lists for a specified number of recipes. 

## Usage

To use this library, simply add doggy.py to where ever your python path points. This library will be added to pypi, and when this is implemented, We will update the README. 

## Documentation

[Documentation Home Page](https://fjp321.github.io/doggy)

[Documentation for Doggy Library](https://fjp321.github.io/doggy/html/doggy_8py.html)

## Design Choices

### Why SQL instead of json

The reason for sql, and by extension python, is for the [sqlite](https://en.wikipedia.org/wiki/SQLite) python library, and a database is the better format for a scalability.
The goal of Doggy is to manage potentially hundreds of recipes and ingredients, so scalability is incredibly important. 
Work is currently being down on the staging and sql branch to deploy this functionality.
Currently, we have implemented json and csv files, which are fully loaded to make changes, which is not ideal for overhead.

### Why no GUI

There is no gui in order to focus efforts on command line implementations. 
The reason command line is being prioritezed over a gui is so that adding a script with doggy to a [cron job](https://en.wikipedia.org/wiki/Cron)is as simple as possible. 
If you want a gui, please look into making one and sharing your implementation.
In accordance with the MIT license, you can use this repository and redistribute for yourself.
Consider using [pyqt](https://en.wikipedia.org/wiki/PyQt).
If you run into any issues regarding the doggy functions, please feel free to open an issue.

## Resources

+ SQLite: https://en.wikipedia.org/wiki/SQLite
+ Cron: https://en.wikipedia.org/wiki/Cron
+ Pyqt: https://en.wikipedia.org/wiki/PyQt

## [Planned Updates & Projects](https://github.com/fjp321/doggy/projects)

## Contributors
fjp321
Spencer-Potter
