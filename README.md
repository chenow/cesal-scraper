# Cesal Scraper

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

## Overview

The Cesal Scraper is a Python-based bot designed to check the availability of any of the 6 residences on the [Cesal](https://logement.cesal.fr/) website. When a rental becomes available, it will send you a notification through a Telegram chatbot.

> [!WARNING]
> As websites can evolve, it is not guaranteed that the scraper will work in the future if not maintained.

## Features

- Scrapes Cesal website for available housing.
- Sends notifications to a Telegram chat when rentals are found.
- Supports multiple arrival dates for comprehensive checks.
- Uses `Docker` for easy setup and deployment.
- Ensures code quality with `ruff`.

## Prerequisites

- Docker and Docker Compose installed on your machine.
- A Telegram bot token from [@BotFather](https://t.me/BotFather).
- Your Telegram chat ID from [@userinfobot](https://t.me/userinfobot).

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/chenow/cesal-scraper.git
   cd cesal-scraper
   ```

2. **Create a `.env` file and edit the variables:**

   ```bash
   cp .env.template .env
   ```

3. **Build and run the bot:**

   ```bash
   docker compose build
   make scrape
   ```
