# Data: [Kaggle Consumer Finance Complaints](https://www.kaggle.com/cfpb/us-consumer-finance-complaints)

 - Input: **consumer_complaint_narrative**
    
 - Output: **product**

# Train:

 - Command: python3 train.py training_data.file parameters.json
 - Example: ```python3 train.py ./data/consumer_complaints.csv.zip ./parameters.json```
 
 A directory will be created during training, and the trained model will be saved in this directory. 

# Predict:

 Provide the model directory (created when running ```train.py```) and new data to ```predict.py```.
 - Command: python3 predict.py ./trained_model_directory/ new_data.file

# Reference:
 - [Implement a cnn for text classification in tensorflow](http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/)
