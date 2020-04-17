# ECBIR
Exact Content-based Image Retrieval System
<h3 align="center">Book Search Engine</h3>
<p align="center">
    An application that allows user to search for their favorite book just by taking a picture of it.
    <br />
    <a href="https://github.com/HANyangguang/ECBIR"><strong>Explore the docs »</strong></a>
    <br />
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

<p align="center">
<img src="/demo/ECBIR.jpg"></img>
</p>

There are many ways to search for a book that you are interested in -  searching it by name, author, ISBN, and any other relevant features. That is all great, but the process is becoming very long as we introduce more and more features in the search system. And what if we want to find the cheapest place to buy the book? We would need to go to multiple websites and type the same query all over again! 

This open-source project tries to solve that problem by leveraging the power of Deep Learning and creating an system that allows an end-user to take a picture of books' cover and find places where they can buy the book. 

This Book Search Engine is an open-source project that demonstrates a way of using Deep Learning in a real-world setting. 

It is opened for contributions. :-)


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
   <img src="/demo/ECBIRdemo.png" alt="Example Image" width="550" height="900">
</p>
  

<!-- CONTRIBUTING -->
## Contributing

Let's improve this project together! :-)

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**. 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature_name/NewFeature`)
3. Commit your Changes (`git commit -m 'Explain your commit'`)
4. Push to the Branch (`git push origin feature_name/NewFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact
Server of the project repo: [https://github.com/HANyangguang/ECBIR](https://github.com/HANyangguang/ECBIR)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [DEep Local Features (DELF) paper](https://arxiv.org/pdf/1612.06321.pdf)
* [DELF Reference implementation](https://www.dlology.com/blog/easy-landmark-image-recognition-with-tensorflow-hub-delf-module/)
* [Original implementation](https://github.com/lucko515/search-book-by-cover-server)
* [Web Structure](https://github.com/matsui528/sis)


## Version Note
### v1
I improve its efficiency by removing the kd tree construction in the find_closest_book function. It reduces query time significantly by almost half of the former time spent.

### v2
0. start to develop my own app by deleting many non-necessary components and add my own function. easier to read. free from the dependence of csv file and generate features only by images themselves.
1. try to cut a ROI using opencv, but failed due to the crash caused by ROI Selector. Wait to repair but paobably give up and turn my direnction to Index using v2.0 branch.

### v3
update the dataset, including Caltech 251, Book Covers Dataset, totally 64,251 images. optimise the html structure.

### v4
Replace kd Tree with HNSW, almost satisfy real-time requirments! 
