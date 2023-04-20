# EDA DBLP using Python and MongoDB

## Project Description

The purpose of this project is to perform exploratory data analysis (EDA) on the DBLP computer science bibliography. By analyzing the bibliographic information on major computer science journals and proceedings, I hope to gain insights into the trends and patterns in computer science research over time. I will use MongoDB to store and manage the data, and use pandas, matplotlib and Seaborn to generate visualizations.

## Approach

- Download the DBLP XML file or any necessary files for the project.
- Load the data into MongoDB using Python, taking care to do so in an efficient manner that doesn't consume too much system memory and CPU.
- Create a new MongoDB database with the name "DBLP".
- Create a new MongoDB collection named "DATA".
- Use MongoDB queries to perform EDA on the data and fetch the necessary information for the analysis.
- Generate visualizations using pandas, matplotlib and seaborn to present the findings.
- Come up with two additional questions related to the data and answer them using visualizations.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
You will need to have Python 3.x installed on your machine. You can download the latest version of [Python](https://www.python.org/downloads/) here.
</br>
You will also need to have Anaconda on your machine. You can download the latest version of [Anaconda](https://www.anaconda.com/) here.

### Installing
Clone this repository onto your local machine.
```
git clone https://github.com/MuhammadAhmedSuhail/EDA-DBLP-using-Python-MongoDB.git
```
Install the required packages.
```
pip install -r requirements.txt
```
**Note**
> Make Sure to have dblp.xml in the same directory as the python program.

## Running the Program
To populate MongoDB, simply execute the following command in your terminal:
```
python populatedb.py
```
To Analyze dblp.xml simply run the Juypter Notebook "EDA.ipynb"

## Built with:
- Python3 - Programming Language Used
- Pandas - Library used for reading/writing and formatting the data
- Seaborn - Library used for Styling the visualizations.
- Matplotlib - Library used for displaying the visualizations. 

## Analysis:
This part includes all the analysis done on dblp.xml data used in this assignment
### Publications per Year
I created a bar chart showing the number of publications per year in the DBLP data. The year-range used in this was (1936-1950).
The plot shows that the publications made per year before 1946 was below 20.

![PublicationsPerYearBetween1936-1950](https://user-images.githubusercontent.com/72251313/233433373-b06bd6f4-3837-4e46-a7ec-913119616c34.png)

### Count of Biblography in Article and Inproceedings Count:
As the plot below shows that the count of both the element types is almost the same.

![ArticleandInproceedingsCount](https://user-images.githubusercontent.com/72251313/233435294-fea1229b-337e-460f-9962-e7d230fae211.png)

### Publications per Year by Element Type:
I created a stacked bar plot showing the number of publications per year from (2009-2023) by element type in the DBLP data. I found that the most common types varied over time, with article and inproceedings being most common in these years.

![ElementTypeCountPerYear](https://user-images.githubusercontent.com/72251313/233435732-f5fc08c5-b422-4c96-a8dc-bf933e4ba8eb.png)

### Phd Thesis per Year after 1990:
I created a stacked bar plot showing the number of phd thesis per year from (1991-2021) in the DBLP data.
I found that after the year 2006 the number of phd thesis was atleast 2500 per Year.

![PHDThesisPerYear](https://user-images.githubusercontent.com/72251313/233436823-371dccdc-8b1d-4af6-bd47-f748fb4b912b.png)

### Number of Publications of Frank Olken vs Russell Turpin:
I created a bar plot comparing the number of publications by Frank Olken and Russell Turpin.
It turns out that Russell Turpin has three times more publications that Frank Olken.

![FrankandRussellCount](https://user-images.githubusercontent.com/72251313/233437895-03970bd8-ca99-432f-a197-8c3df282e810.png)

## Conclusion:
In this project, I have explored the DBLP computer science bibliography and gained insights into the trends and patterns in computer science research over time. I used MongoDB to store and manage the data, and used pandas, matplotlib and seaborn to generate visualizations.

Through my EDA tasks, I found that the number of publications has steadily increased over time, with a sharp increase in the 2000s. I also found that the most common types of bibliography elements were article, inproceedings, and proceedings.

By coming up with my own questions and using visualizations to answer them, I was able to gain even deeper insights into the data. I found that the proportion of PhD theses has decreased over time, and that authors had a higher number of publications overall, but conferences had a higher number of publications in recent years.

## Author:
- Muhammad Ahmed Suhail

## Acknowledgments:
- This project was completed as an assignment for Big Data Analytics at FAST - NUCES Islamabad.













