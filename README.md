# Images-Classifier
Image Recognition of upto 30 classes using a resnet50 model 

## Installation(Ubuntu):
Requirement:
 1. Keras
 2. Tensorflow
 3. Numpy
 4. Pretrained-Resnet50 Weights

* Clone this Repo
* Install required packages using pip or conda 

### Pip

```
$ pip install --upgrade tensorflow \
                         keras \
                         numpy \
````
### Conda
```
$ conda install -c conda-forge keras 
$ conda install -c conda-forge tensorflow 
$ conda install -c anaconda numpy 
```

* Run

```
$ python classify.py --image /Images/elephant.jpeg
```

 Or
```
$ python classify.py --image_url http://i.imgur.com/wpxMwsR.jpg
```

## Example

#### Input 
<img align="center" width="300" height="500" src='https://cdn-images-1.medium.com/max/800/1*sSVTQaSTMti6ZcJRcsnSbA.jpeg'>

#### Output 
<img align="center" width="800" height="250" src='https://cdn-images-1.medium.com/max/800/1*JUgxIkYpZGuJBEsDmRZ3hg.png'>


 

                    
