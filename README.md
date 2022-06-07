# Senior Project: RDF Construction Model

### Spring 2022

<br>

This program takes in a knowledge graph as input and outputs it in Resource Description Framework (RDF) format. 

### Code Structure

* **excel-parse** : Directory responsible for parsing all data given in excel format by the clients, including fake data to populate DB and ONET to Profile characteristics mappings.
* **onet-parse** : Directory responsible for pinging ONET Web Services API to fetch all STEM jobs and their respective relevant data. 
* **populate.py** : The script gets both directories data and populates DB tables.
