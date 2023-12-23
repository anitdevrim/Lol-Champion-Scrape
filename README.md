# LEAGUE OF LEGENDS CHAMPION DATA SCRAPING

This project aims to scrape all the data for given champion in game called League Of Legends.

# Operation

Data scraping is done by selenium using python.
Data is scraped from https://mobalytics.gg/lol website.
This project is prepared with Docker.

# Requirements

Before start running the program given requirements.txt should be installed. Installation of requirements.txt can be done by copying the command below in your terminal.

```bash
pip install -r requirements.txt
```

# Usage

Firstly, clone this repository into your computer.
```bash
git clone https://github.com/anitdevrim/Lol-Champion-Scrape
```
Go into the directory.
```bash
cd Lol-Champion-Scrape
```
After installing the requirements we run the docker-compose.yml file by

```bash
docker-compose up
```

Now, localhost:4444 is ready for our scraping process.
This process may take few seconds.

Now we use the command below to run our program.

```bash
python3 run.py
```

# I/O

As an input, you should give a correct champion name for program to scrape.
Output will be printed through terminal after few seconds.
