I trained a convolutional neural net from scratch on a relatively small data set. I have 500 samples for both classes in my training data, 300 for my validation set, and a little over 300 in my test set.

My baseline model from scratch achieved a validation accuracy of about 61%. The model is overfit.

I then followed the process to augment more image data. I trained a new network using this data augmentation configuration and added a drop out layer. 

The model generalizes a lot better and I was able to achieve an accuracy of 71%.

For my next steps, I am going to look through my images and remove noisy samples (images that don't actually show what I am trying to train my model on). I would also like to include more samples and utilize transfer learning.