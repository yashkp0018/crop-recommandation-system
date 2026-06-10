
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn import metrics
import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv("crop_recommendation.csv")
features = df[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]
target = df['label']


# Splitting into train and test data

from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,target,test_size = 0.2,random_state =2)


##random forest algorith 
from sklearn.ensemble import RandomForestClassifier

RF = RandomForestClassifier(n_estimators=20, random_state=0)
RF.fit(Xtrain,Ytrain)

predicted_values = RF.predict(Xtest)

x = metrics.accuracy_score(Ytest, predicted_values)

print("RF's Accuracy is: {:.2f} ".format(x*100))

print(classification_report(Ytest,predicted_values))



from tkinter import *
from PIL import Image,ImageTk
global root
root = Tk()
root.title('Crop Recommendation window')
root.geometry('1500x750')
img=Image.open("a.jpg")
img=img.resize((1500,750))
bg=ImageTk.PhotoImage(img)


lbl=Label(root,image=bg)
lbl.place(x=0,y=0)

label = Label( root, text = 'Crop Recommendation System',font=('arial',24,'bold'),bd=20,background="#CDD954")
label.place(x=300,y=10)



label_1 = Label(root, text ='nitrogen',font=("Helvetica", 18),background="#CDD954")
label_1.place(x=300,y=100)
    
Entry_1= Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_1.place(x=600,y=100)



label_2 = Label(root, text ='phosporus',font=("Helvetica", 16),background="#CDD954")
label_2.place(x=300,y=170)
    
Entry_2 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_2.place(x=600,y=170)
   

    
label_3 = Label(root, text ='pottasium',font=("Helvetica", 18),background="#CDD954")
label_3.place(x=300,y=240)
    
Entry_3 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_3.place(x=600,y=240)



label_4 = Label(root, text ='temperature',font=("Helvetica", 18),background="#CDD954")
label_4.place(x=300,y=310)
    
Entry_4= Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_4.place(x=600,y=310)



label_5 = Label(root, text ='humidity',font=("Helvetica", 18),background="#CDD954")
label_5.place(x=300,y=380)
    
Entry_5 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_5.place(x=600,y=380)



label_6 = Label(root, text ='ph',font=("Helvetica", 18),background="#CDD954")
label_6.place(x=300,y=450)
    
Entry_6 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_6.place(x=600,y=450)



label_7 = Label(root, text ='rainfall',font=("Helvetica", 18),background="#CDD954")
label_7.place(x=300,y=520)
    
Entry_7 = Entry(root,font=("Helvetica", 18),justify=CENTER)
Entry_7.place(x=600,y=520)

def acc():
    image = Image.open("result.jpg")
    image = image.resize((300, 300))
    img = ImageTk.PhotoImage(image)  
    global panel1
    panel1 = Button(root10, image=img,command=close_acc)
    panel1.image = img
    panel1.place(x=575,y=220)
def clear_out():
    out_img.destroy()
    output.configure(text="")
    Entry_1.delete(0,END)
    Entry_2.delete(0,END)
    Entry_3.delete(0,END)
    Entry_4.delete(0,END)
    Entry_5.delete(0,END)
    Entry_6.delete(0,END)
    Entry_7.delete(0,END)
    
    

def predict():
    N = Entry_1.get()
    P = Entry_2.get()
    K = Entry_3.get()
    temperature =Entry_4.get()
    humidity =Entry_5.get()
    ph =Entry_6.get()  
    rainfall = Entry_7.get()   
    out = RF.predict([[float(N),
       float(P),
       float(K),
       float(temperature),
       float(humidity),
       float(ph),
       float(rainfall)]])     
    print(out[0])
    output.configure(text=" you want to grow   "+str(out[0]))
    
    res_img=Image.open("result\\"+str(out[0])+".jpg")
    res_img=res_img.resize((300,300))
    bgg=ImageTk.PhotoImage(res_img)
##    out_img.configure(image=bgg)
    global out_img
    out_img = Button(root,image=bgg,command=clear_out)
    out_img.image=bgg
    out_img.place(x=1000,y=300)
    
    
    
   

b1 = Button(root, text = 'predict',font=("Helvetica", 18),background="#CDD954",command = predict)
b1.place(x=300,y=650)
    

output = Label(root,font=("Helvetica", 18),justify=CENTER)
output.place(x=600,y=650)

    
root.mainloop()






#############################################################################################################






