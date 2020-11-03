# Plant Disease Prediction

An end to end application which predicts whether the cotton plant belongs to the following set of classes.

- Diseased Cotton Leaf.
- Diseased Cotton Plant.
- Fresh Cotton Leaf.
- Fresh Cotton Plant.

## Training
 - For Training Purpose Refer to the following Notebooks.
 - [Click Here to view the training notebooks](https://github.com/R-aryan/Plant_Disease_Prediction/tree/feature/develop/src/training)
 - The training is done on [Google Colab](https://colab.research.google.com/) , if you have your own GPU you can train on your local machine.
 - Dataset can be downloaded from here.[Click Here](https://drive.google.com/file/d/1w5GpRaxKLofHXrAGALWz4ircKmMKcx2l/view?usp=sharing)  
 - After Downloading the dataset **Unzip** it and place it under the Dataset Folder , all the path in the colab notebook is according to my relative path so it needs to be changed accordingly.
 
 
 ## Inference
 
 - For Inference Purpose, create a **virtual environment** and install **requirements.txt** .
 - After performing the above step, run **main.py.**
 - After running the script **Flask Server** will start at **http://127.0.0.1:5001/** , Copy this URL and open it in your browser.
 - Your flask application is now up and running and should look something like this.
 ![Image of Landing Page](https://github.com/R-aryan/Plant_Disease_Prediction/blob/feature/develop/src/msc/demo_image_2.PNG).
 
 - Click on the **Choose** button and upload the plant image , after uploading the image the page will look something like this. 
  ![Image of Landing Page](https://github.com/R-aryan/Plant_Disease_Prediction/blob/feature/develop/src/msc/demo_image_3.PNG).
  
 - After Uploading the Image, click on the **Predict** button, after few seconds the output will appear something like this.
  ![Image of Landing Page](https://github.com/R-aryan/Plant_Disease_Prediction/blob/feature/develop/src/msc/demo_image_4.PNG).
