# GitHub Views Botter

GitHub Views Botter is a Python script that automates the process of increasing the view count of a GitHub repository's image file. It does so by sending requests to the image URL, effectively incrementing the view count.

![GitHub Views Botter](https://img.shields.io/badge/version-1.0.0-brightgreen)
![GitHub Views Botter](https://img.shields.io/badge/author-%E2%9C%9F-9cf)

---

## Features

- **Multi-Threaded:** Utilize multiple threads to efficiently increase the view count of the GitHub repository's image file.
- **Easy to Use:** Just provide the image URL, the number of threads you want to use, and your proxy details.
- **Real-Time Stats:** Monitor the number of successful hits and failed attempts.
- **Console Title:** Get real-time statistics in the console title, including Views Per Minute (VPM).

---

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Getting Started

### Prerequisites

To run the GitHub Views Botter, you will need the following:

- Python 3.x
- Requests library

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Devuxious/GitHub-Views-Botter.git
   ```
  
2. Install the required dependencies:
   
   ```bash
   pip install requests
   ```
   
3. Run the script:
   ```bash
   python main.py
   ```


## Usage

1. After running the script, you'll be prompted to enter the number of threads and the image URL you want to target.
2. **Number of Threads:** Input the desired number of threads you want to use. More threads can help increase the view count faster, but be cautious not to overload the target server.
3. **Image URL:** Provide the URL of the image file hosted on the GitHub repository that you want to boost the view count for.
4. The script will start sending requests to the image URL, incrementing the view count.
5. You can monitor the progress in real-time in the console title, where the hits, failures, and Views Per Minute (VPM) will be displayed.
