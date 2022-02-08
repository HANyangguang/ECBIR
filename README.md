# ECBIR
Exact Content-based Image Retrieval System
<h3 align="center">Book Search Engine</h3>
<p align="center">
    An application that allows user to search for their favorite book just by taking a picture of it.
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [License](#license)
* [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
## About The Project

<p align="center">
<img src="/demo/ECBIR.jpg"></img>
</p>

There are many ways to search for a book that you are interested in -  searching it by name, author, ISBN, and any other relevant features. That is all great, but the process is becoming very long as we introduce more and more features in the search system. And what if we want to find the cheapest place to buy the book? We would need to go to multiple websites and type the same query all over again! 

This open-source project tries to solve that problem by leveraging the power of Deep Learning and creating an system that allows an end-user to take a picture of books' cover and find places where they can buy the book. 

This Book Search Engine is an open-source project that demonstrates a way of using Deep Learning in a real-world setting. 

### Built With
* [Tensorflow](https://www.tensorflow.org/)
* [Flask](https://www.palletsprojects.com/p/flask/)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

To run this project you'll need **Python 3.5 or later** and all dependencies listed in the **requirements.txt**. 

To install all dependencies listend in the requirements file:

```sh
 pip install -r requirements.txt 
```

### Installation

1. Clone the repo
```sh
git clone https://github.com/HANyangguang/ECBIR.git
```
2. Create the **dataset** folder and other folders in the static folder
```sh
mkdir static/dataset
mkdir static/feature
mkdir static/resized
mkdir static/uploads
```
3. Download the books covers dataset from the Kaggle and unpack the dataset into the **dataset** folder

Link to the [dataset](https://www.kaggle.com/lukaanicin/book-covers-dataset)

4. Run the script **offline.py** to index the database use DELF and HNSW
```sh
python(3) offline.py
```
5. Start the Flaks server with the **server.py**
```sh
python(3) server.py
```

<!-- USAGE EXAMPLES -->
## Usage examples

<p align="center"> 
   <img src="/demo/ECBIRdemo.png" alt="Example Image" width="550">
</p>

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [DEep Local Features (DELF) paper](https://arxiv.org/pdf/1612.06321.pdf)
* [DELF Reference implementation](https://www.dlology.com/blog/easy-landmark-image-recognition-with-tensorflow-hub-delf-module/)
* [Search Engine](https://github.com/lucko515/search-book-by-cover-server)
* [Web HTML](https://github.com/matsui528/sis)

