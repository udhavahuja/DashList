# DashList

#### Video Demo: https://youtu.be/a0Gxhq8n-Vk

#### Description:

DashList is a personal media tracking web application built with **Flask** that lets users organize movies, TV shows, and books in one place. Whether you're planning what to watch next, keeping track of your current reads, or revisiting your favorites, DashList makes managing your entertainment library simple and intuitive.

## Features

* Secure user authentication
* Search for movies and TV shows using the **TMDB API**
* Search for books using the **Google Books API**
* Add media to your personal library
* Organize media with custom statuses:

  * Planned
  * Ongoing
  * Completed
  * Dumpped
* Rate and review completed media
* Filter your library by media type and status
* Personal dashboard with library statistics
* Edit or remove media entries
* Responsive interface for desktop and mobile
* Built-in dark mode

## Tech Stack

**Backend**

* Python
* Flask
* SQLite

**Frontend**

* HTML
* CSS
* Bootstrap
* JavaScript

**APIs**

* TMDB API
* Google Books API

## Live Demo

**Website:** [DashList](https://dashlist.onrender.com)

## Screenshots

<h3>Login</h3>
<p align="center">
    <img src ="Screenshots/Login.png" width="700">
</p>

<h3>Register</h3>
<p align="center">
    <img src ="Screenshots/Register.png" width="700">
</p>

<h3>Dashboard</h3>
<p align="center">
    <img src ="Screenshots/Dashboard.png" width="700">
</p>

<h3>Browse</h3>
<p align="center">
    <img src ="Screenshots/browse-movies.png" width="32%">
    <img src ="Screenshots/browse-tv.png" width="32%">
    <img src ="Screenshots/browse-books.png" width="32%">
</p>

<h3>Library</h3>
<p align="center">
    <img src ="Screenshots/library.png" width="48%">
    <img src ="Screenshots/library-edit.png" width="48%">
</p>

<h3>Dark Mode</h3>
<p align="center">
    <img src ="Screenshots/Dashboard-dark.png" width="23.5%">
    <img src ="Screenshots/browse-dark.png" width="23.5%">
    <img src ="Screenshots/library-dark.png" width="23.5%">
    <img src ="Screenshots/library-edit-dark.png" width="23.5%">
</p>

## Future Improvements

* Personalized recommendations
* Custom collections and playlists
* Friend sharing and recommendations
* Import/Export library
* Advanced search and filtering
* Reading and watching analytics

## License

This project was developed as the **CS50 Final Project** and is intended for educational purposes.

## Deployment Notes

The live demo is hosted on Render's free tier using SQLite

Since Render's free web services do not support persistent disks, the SQLite databases is stored on an ephmeral filesystem. As a result, user accounts and media ;ibraries in the live demo may occasionally reset after service restarts or redepolyments.

This is a limitation of hosting environment rather than application itself.

## Author

**Udhav Ahuja**
