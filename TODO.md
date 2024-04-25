# TODO
### code
* normalize datasets into range [-1, 1] [docs](https://pytorch.org/vision/stable/transforms.html)
* visualize net with tensorBoard [docs](https://pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html) 
* train/test split
* in the `forward` part of the net, don't i need to slap a linear filter (or whatever that filter is called on there to get the output normalized?)
* flip and rotate images for more data? [docs](https://pytorch.org/vision/stable/transforms.html) 
* multithread preprocessing script?

### theory
* look at theory of how to make cnn again
    * in-depth post [link](https://medium.com/bitgrit-data-science-publication/building-an-image-classification-model-with-pytorch-from-scratch-f10452073212) 
    * different layer and filter types:
    * relu
    * pool
    * linear
    * ...
