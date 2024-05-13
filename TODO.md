# TODO
### code
* normalize datasets into range [-1, 1] [docs](https://pytorch.org/vision/stable/transforms.html)
* visualize net with tensorBoard [docs](https://pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html) 
* train/test split
* in the `forward` part of the net, don't i need to slap a softmax on the end? (or whatever that filter is called on there to get the output normalized?)
* flip and rotate images for more data? [docs](https://pytorch.org/vision/stable/transforms.html) 
* multithread preprocessing script?
* move to GPU
* (once everything works): make data preprocessing so it can handle other ascii things as well, not just from the dataset i created with my script


### theory
* understand how the heck the sizes of the network work
* look at theory of how to make cnn again
    * in-depth post [link](https://medium.com/bitgrit-data-science-publication/building-an-image-classification-model-with-pytorch-from-scratch-f10452073212) 
    * different layer and filter types:
    * relu
    * pool
    * linear
    * ...
* review loss and optimizers
