# DEEP LEARNING: Recognizing Human Facial Expressions In Photographs

## Question/Need:
*What is the framing question of your analysis, or the purpose of the model/system you plan to build?*

- Can my model recognize a smiling faces versus a frowning face (or other facial expressions)?

*Who benefits from exploring this question or building this model/system?*  

A model that can recognize a smiling face has several use-cases.
1. When taking a group picture, it can be difficult to snap a photo at the exact right time. Implementing this system, to trigger the camera to take a photo when all in the group are smiling, will save time and reduce stress for the photographer.

2. With the smartphone functioning as an individuals camera, it is easy for thousands of similar photos to pile up. A system that recognizes smiles could suggest which photos to keep and which to discard from a group of similar photos.

3. Researchers who study [facial expressions](https://www.johngottman.net/wp-content/uploads/2011/05/Facial-Expressions-During-Marital-Conflict.pdf) in their line of work would benefit from this type of automation in their work.

## Data Description:
*What dataset(s) do you plan to use, and how will you obtain the data?*  

I am currently looking through the catalog of free stock photos from Pixabay and Pexels. I am isolating a "[smiling face](https://pixabay.com/images/search/smiling/?cat=people)" group and a "[sad face](https://www.pexels.com/search/sad/)" group.

I will start with 500-1000 photos for each class.   

*What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?*

An individual sample will be one photograph.

## Tools:
*How do you intend to meet the tools requirement of the project?*
- Keras
- Build a convolutional neural net
- Use of dimensionality reduction (?)
- Rigorous validation and tuning

*Are you planning in advance to need or use additional tools beyond those required?*
- Unsure

## MVP Goal:
*What would a minimum viable product (MVP) look like for this project?*
- Data scraped from website
- Organized into train/val/test folders
- Subdivided into smile/sad folders
- Baseline CNN model