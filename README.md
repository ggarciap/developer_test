# Developer Test
## About
This repository contains all the scripts and answers to the developer test. 

## Question 1-6: 
The queries for these questions can be found on the folder named `./Q1-Q6`

## Question 7 and 8: Installation and Scripts Execution 
For **Q7** the file `./db_create_tables.py` contains all the schema and the tables described in the question. 

For **Q8** I decided to use docker becuase of the advantages of fast installation and capability of allowing developers use different operating systems. 

Make sure to have docker:
    
    pip install docker

Pull postgres image from docker hub:

    docker pull mysql

Create docker container `mydb`:

    docker run --name=mydb -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_USER=root -e MYSQL_DATABASE=db -e MYSQL_ROOT_HOST=% -d -p 3306:3306 mysql/mysql-server

Execute this command to make the script runnable:
    
    chmod u+x job-Q8.sh

Once we have a container we can execute the shell script that will create and populate the database known as first_dibs:

    ./job-Q8.sh


To access the mysql docker instance:

    docker exec -it mydb bash

To use MySQL monitor, password: `'my-secret-pw'`:

    mysql -u root -p

Select database:

    USE db;

## Question 9:
The SQL code used to generate the answer to this question can be found in the folder named `./Q9-Q13` as `q9_topline.sql`

## Question 10:
### Which of the three emails should be sent out to the larger list in order to maximize actions? Why do you think this is? Please limit your answer to one or two sentences.

According to the topline summary done to the data Mailing B has the highest number of actions per recipient, which makes it a great  candidate to be sent out to a larger list.

## Question 11:
The SQL code used to generate the answer to this question can be found in the folder named `./Q9-Q13` as `q11_topline.sql`

## Question 12:
The SQL code used to generate the answer to this question can be found in the folder named `./Q9-Q13` as `q12_topline.sql`
 
## Question 13:
Execute this command to make the script runnable:
    
    chmod u+x job-Q13.sh

Execute the following shell script that will create the .CSV file corresponding to **Q9**. File with name `csv_creation.py` cointains all the code required to query the database:


    ./job-Q13.sh

After running this shell script a new .CSV file named `Q9-output.csv` should be present on project directory. 

## Question 14:
Execute this command to make the script runnable:
    
    chmod u+x job-Q14.sh

Execute the following shell script that will create the .CSV file corresponding to **Q14**. File with name `github-api.py` cointains all the code required to query the database:


    ./job-Q14.sh

After running this shell script a new .CSV file named `Q14-output.csv` should be present on project directory. 

## Question 15:
### 15.a How do you identify these sales regions? 
From the tracking of interactions with clients and potential clients we can use the phone numbers and map them to their corresponding area codes to have a better prespective of which states and regions have the largest volumes of calls. Furthermore, we could complement the data that we have with some income indicators depending the area where completed transactions and attempted trasactions have had large quantities or where ad-placement responses have had positve responses. In addition, the possibility of using the phone number as a tool of finding social media presence (ex. Facebook, Likedin) can be of used to map interests, education status, Company/workplace and user activity. 

### 15.b What information would you use to predict high value regions? (You will not be penalized for assuming we have information that we don't actually have.)
Possible features:
Age of clients and potential clients, City and State of clients and potential clients, longitude, lattitude, income, education status, education major(s) and employer industry and total number of impressions per user (ad views)

### 15.c What techniques or tools would you use to confirm which pieces of data from (15.b) correlate with a region’s sales, and how would you determine how much weight to give each data point?

Using an correlation matrix as an intial tool for visualizing the features can help us understand the possible relations that can exist. Furthermore, we can perfom lasso regression and use the beta coefficients as way to indicate the unique strength of relationship between a predictor and criterion variable, and in this way we can determine the 'weight' of each data feature. Finally, if we want to narrow down the number of features and determine statistical significance we can perform a t-test and in this way making sure to examine each coefficient individually.

### 15.d How would you verify your prediction?
We would have to perform training-validation-test split of the data set which would allows us to first use the training dataset to train a frew candidate models. The second step would be to use the validation dataset to evaluate the candidate models (in this case using linear regression), and once the candidate is chosen based on metrics such as Root mean squared error (RMSE) or Mean squared error (MSE). Afterwards, the model selected is trained with a new training dataset and then the model is evaluated the the test dataset (using again the metrics previously mentioned).  

