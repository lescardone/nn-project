# **IDENTIFYING MOOD WITH CONVOLUTIONAL NEURAL NETS**
Leslie Cardone  
June 11, 2021  
Metis: Deep Learning



## ABSTRACT

With the smartphone functioning as an individuals camera, it is easy for thousands of similar photos to pile up. A system that recognizes smiles or "happier" images could suggest which photos to keep and which to discard from a group of similar photos.

With this in mind, I aim to classify photos into two categories; happy or sad; using a Convolutional Neural Net.


## DATA

The the photos for this project have been scraped from [Pexels](https://www.pexels.com), a site offering free stock photos. 

There are 2,250 photos, about half "happy" and half "sad." The photos were categorized using the Pexels tagging system. All happy photos were compiled from search results using the search term "happy" and all sad photos were compiled  using the search term "sad."


## DESIGN

*CONVOLUTIONAL NEURAL NET*  
I trained a convolutional neural net from scratch on a relatively small data set. I used 500 samples for both classes in my training data, 300 for my validation set, and a little over 300 in my test set.

My baseline model from scratch achieved a validation accuracy of about 61%. 

I then followed the process to augment more image data. I trained a new network using this data augmentation configuration and added a drop out layer. 

The model generalizes a lot better and I was able to achieve an accuracy of 71%.

My final CNN model used transfer learning, with frozen weights from MobileNet. I used the Adam optimizer, and trained on a batch size of 20. I used early stopping to monitor the binary crossentropy loss.

This model performed with 77% accuracy on my validation set and 76% accuracy on my test set.


## ALGORITHMS/TOOLS

*LIBRARIES*
- Selenium and BeautifulSoup for webscraping
- Numpy and Pandas for data manipulation
- keras to build the CNN and fully connected layers
- Google Colaboratory to train the model
- tf-keras-vis to vizualize the CNN activation
