# Human-Benchmark-Bots

**Human benchmark was never meant for bots**

The main goal of this bots is to complete the benchmarks as quickly as possible and get the highest score

Bots run on selenium in the python language for www.humanbenchmark.com

## Table of Contents

- [Progress](#progress)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)
- [Extra Credit](#extra-credit)

## Progress
Here is the progression of the project so far and their percentiles:

- [x] [Aim Trainer](https://github.com/Perseus333/Human-Benchmark-Bots/blob/main/Aim-Trainer.py) (Top 99.9%) - Best score: 26ms
- [x] [Number Memory](https://github.com/Perseus333/Human-Benchmark-Bots/blob/main/Number-Memory.py) (Top 100%) - Best score: ∞
- [x] [Sequence Memory](https://github.com/Perseus333/Human-Benchmark-Bots/blob/main/Sequence-Memory.py) (Top 100%) - Best score: ∞
- [x] [Verbal Memory](https://github.com/Perseus333/Human-Benchmark-Bots/blob/main/Reaction-Time.py) (Top 100) - Best score: ∞
- [x] [Visual Memory](https://github.com/Perseus333/Human-Benchmark-Bots/blob/main/Visual-Memory.py) (Top 100%) - Best score: ∞
- [x] [Reaction Time](https://github.com/Perseus333/Human-Benchmark-Bots/blob/main/Reaction-Time.py) (Top 99.9%) - Best score: 28ms
- [x] [Typing Test](https://github.com/Perseus333/Human-Benchmark-Bots/blob/main/Typing-Test.py) (Top 100%) - Best score: 8200 WPM
- [x] [Chimp Test](https://github.com/Perseus333/Human-Benchmark-Bots/blob/main/Chimp-Test.py) (Top 100%) - Best score: 41(max) in 33.864s


## Installation
The scripts are meant for **Python 3.9**
The scripts can be run independently from each other.

### Dependencies
Before you run make sure that you have installed the required dependencies which are:

1. **Selenium** - Allows to scrape the website and interact with it.
2. **Webdriver Manager** - Removes the need to install a chromedriver manually and specify its location path

To install both of them just run:

```
pip install selenium webdriver-manager
```
### Running the files

Clone this repository to your local machine:

```bash
git clone https://github.com/Perseus333/Human-Benchmark-Bots.git
```


Move to the directory containing the scripts:

```
cd Human-Benchmark-Bots
```

You have two options, either executing a standalone script, or main.py to be able to execute them all multiple times

### Standalone

Run a python file, AimTrainer.py for example:

```bash
cd standalones
python Aim-Trainer.py
```

### main.py

Run main.py:

```bash
python main.py
```

You should know that main.py requires certain commands to open each test, here is a table with the values

| Command | Function         |
|---------|------------------|
| typing  | typing_test      |
| sequence| sequence_memory  |
| aim     | aim_trainer      |
| reaction| reaction_time    |
| number  | number_memory    |
| chimp   | chimp_test       |
| visual  | visual_memory    |
| verbal  | verbal_memory    |

So, when asked just type in the correct command

## Contributing
Feel free to suggest improvements and contribute to the code!

 ## License

This project is licensed under the GPL-3.0 license - see the [LICENSE](LICENSE) file for details.

## Extra Credit
The visual memory, aim trainer, and typing test have part of the code or are inspired from [Alorans'](https://github.com/alorans) [AutoHumanBenchmark](https://github.com/alorans/AutoHumanBenchmark)
