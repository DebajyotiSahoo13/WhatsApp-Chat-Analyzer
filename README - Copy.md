# Potato Leaf Disease Classification

<p align="center">
  <img class="center" src ="https://postimg.cc/Wdct7cNZ" alt="Drawing" style="width: 1400px; height: 600px">
</p>

<b>Description : </b> Here I used **Artificial Intelligence** in diagnosing plant diseases. Various diseases like early blight and late blight immensely influence the quality and quantity of the potatoes and manual interpretation of these leaf diseases is quite time-taking and cumbersome. Therefore I created a **Web App** using <b>Streamlit</b> which simply classify <b>Potato Leaf Diseases</b> and, finally deployed the Web-app on **Heroku**. Internally, our model is built using a simple <b>Convolutional Neural Network Architecture</b> to classify <b>Potato Leaf Diseases</b>. Initially I collected ready-made data from internet. Then due to small size of dataset, I used one of the simple and effective method, called <b>Data Augmentation</b> to increase the size of dataset as well as to reduce overfitting of our model. At the end built a **Deep Learning Model** to detect or classify Potato Leaf Diseases and got a **test accuracy of 97%.**

<b>Heroku App : https://potato-leaf-disease-detection.herokuapp.com/</b><br>
<b>Dataset Source : https://www.kaggle.com/arjuntejaswi/plant-village</b><br>

<b>Sample Output : </b> The output is showing 3 thing's.

- <b>Predicted Class : </b>The model's output.
- <b>Actual Class : </b>The actual output.
- <b>Confidence : </b>How confident our model is.

https://user-images.githubusercontent.com/63307564/145527457-cd9f8844-fe5d-47d2-ba18-759bdc667489.mp4

<p align="center">
  <img class="center" src ="/main/sample/potato.png" alt="Drawing" style="width: 1400px; height: 800px">
</p>

<b>Folder Structure : </b>

```
                    Potato Leaf Dataset       --> main folder
                      ----| train
                          ----| Potato_Healthy
                              ----| img1.jpg
                              ----| img2.jpg
                              ----| img3.jpg
                          ----| Potato_Early_Blight
                              ----| img1.jpg
                              ----| img2.jpg
                              ----| img3.jpg
                          ----| Potato_Late_Blight
                              ----| img1.jpg
                              ----| img2.jpg
                              ----| img3.jpg

                      ----| test
                          ----| Potato_Healthy
                              ----| img1.jpg
                              ----| img2.jpg
                              ----| img3.jpg
                          ----| Potato_Early_Blight
                              ----| img1.jpg
                              ----| img2.jpg
                              ----| img3.jpg
                          ----| Potato_Late_Blight
                              ----| img1.jpg
                              ----| img2.jpg
                              ----| img3.jpg

                      ----| valid
                          ----| Potato_Healthy
                              ----| img1.jpg
                              ----| img2.jpg
                              ----| img3.jpg
                          ----| Potato_Early_Blight
                              ----| img1.jpg
                              ----| img2.jpg
                              ----| img3.jpg
                          ----| Potato_Late_Blight
                              ----| img1.jpg
                              ----| img2.jpg
                              ----| img3.jpg
```
