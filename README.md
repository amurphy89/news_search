# News Search
 
A command line Python application to allow a user to perform queries on documents stored in a text file. Users can use the AND and OR search operators and terms to query existing documents. Thr program returns the indices of documents matching the queries.

## Getting Started

Open a command prompt in the root of the project and run:

```pip install -e .```

Then from your command line run:

```news_search [search_type] [terms]```

You can search using OR and AND type operators.

i.e ```news_search OR Care Quality Commission```

This will return the indices of any matching documents.

### Prerequisites

This project requires Python3 to be installed, you may as want to run the application in a virtual Python environment. You can learn to install Python3 and virtualenv here:
https://docs.python-guide.org/dev/virtualenvs/

## Running the tests

To run the tests please install pytest with ```pip install pytest``` and run ```pytest``` in the root folder.

## Authors

* **Ash Murphy**