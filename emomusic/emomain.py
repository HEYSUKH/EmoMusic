from urllib.request import HTTPHandler
def main(emotion):

    # Url for Drama genre of song against emotion Sad
    if(emotion == "sad"):
     print("https://www.jiosaavn.com/song/o-bedardeya-from-tu-jhoothi-main-makkaar/CCsafyNnRnQ \nhttps://www.jiosaavn.com/song/zihaal-e-miskin/OQAgUxlXTmM")
    # Url for Musical genre of song against emotion Disgust
    elif(emotion == "disgust"):
        print("https://open.spotify.com/track/2DnJjbjNTV9Nd5NOa1KGba?si=db81ad2a7edf4515 \nhttps://open.spotify.com/track/1KGi9sZVMeszgZOWivFpxs?si=73e101ed374b4b9e")

    # Url for Sport genre of song against emotion Fear
    elif(emotion == "fear"):
            print("https://www.jiosaavn.com/song/tum-jo-aaye-jindagi/JgYbX1lodX0 \nhttps://open.spotify.com/track/2WObGIQXhjveq6yuXvf6VQ?si=0de211110fad4eae")

    # Url for Thriller genre of song against emotion Enjoyment
    elif(emotion == "happy"):
        print("https://open.spotify.com/track/45QyDvYY6hL5dhVACaCMAU?si=32f96a54556e4fa1 \nhttps://open.spotify.com/track/1zffEtIghkEg8AKrK7bgqT?si=8f1163987bcf4cc1")

    # Url for Film_noir genre of song against emotion Surprise
    elif(emotion == "surprise"):
        print("https://open.spotify.com/track/22bPsP2jCgbLUvh82U0Z3M?si=a3b0c360e2d949b3 \nhttps://open.spotify.com/track/0tQ9vBYpldCuikPsbgOVKA?si=f89a035ade4b42cf")

    else: print("invalid emotion")

!pip install deepface &> /dev/null
print ("Deep Face installed sucessfully!!")

from deepface import DeepFace
##Load and display input image
import cv2
import matplotlib.pyplot as plt

img1=cv2.imread("/content/happy woman.jpg")
plt.imshow(img1)
plt.imshow(img1[:, :, ::-1 ])
plt.show()
obj=DeepFace.analyze(img1, actions = ['emotion'])
print(obj)
print(type(obj))
final_obj={}
for i in obj:
    final_obj.update(i)
print (final_obj)
print(type(final_obj))
em=(final_obj['dominant_emotion'])
emotion= em

print("\n")
print("\n EMOTION BASED PLAYLIST RECOMMENDATION")
print("Recommended songs for",em,"emotion")
result= main(emotion)
