import streamlit as st
import pickle
import numpy as np



def load_model():
    with open('saved_steps.pkl','rb') as file:
        data=pickle.load(file)
    return data
data=load_model()

ET_Model_loaded=data['model']
le_location=data['le_location']
le_online_order=data['le_online_order']
le_book_table=data['le_book_table']
le_rest_type=data['le_rest_type']
le_cuisines=data['le_cuisines']

def show_predict_page():
    st.title("ZOMATO RATING PREDICTION")

    st.write("""### we need some information to predict the rating""")


    oder=(
        "Yes",
        "No"
    )

    table=(
        "Yes",
        "No"
    )

    location=(
        "Koramangala 5th Block",
        "BTM",                     
        "Indiranagar",          
        "Yelahanka",                 
        "Kanakapura Road",           
        "West Bangalore",             
        "Rajarajeshwari Nagar",        
        "KR Puram"        
                
    )

    type=(
        "Casual Dining",             
        "Quick Bites",                 
        "Cafe",                      
        "Dessert Parlor",              
        "Casual Dining, Bar",           
        "Bar, Pub",                        
        "Club, Casual Dining",             
        "Dessert Parlor, Kiosk",           
        "Dhaba",                          
        "Food Court, Casual Dining",  
    )

    cuisines=(
        "North Indian",                                                          
        "North Indian, Chinese",                                                   
        "South Indian",                                                            
        "Cafe",                                                                    
        "South Indian, North Indian, Chinese",                                     
        "North Indian, Mexican, Continental, Street Food",                           
        "BBQ, Arabian, Rolls, Chinese, North Indian, Juices, Kebab, Desserts",       
        "Cafe, Beverages, Fast Food, Street Food",                                   
        "Desserts, Continental",                                                     
        "Thai, Chinese, Momos"  
    )

    oder=st.selectbox('Oder online',oder)
    table=st.selectbox('Book table',table)
    votes=st.slider('Votes',0,750,3)
    location=st.selectbox('Location',location)
    type=st.selectbox('Raurant typesest',type)
    cuisines=st.selectbox('cuisines',cuisines)


    ok=st.button('predict rating')
    if ok:
        test=np.array([[oder,table,votes,location,type,cuisines]])
        test[:,0]=le_online_order.transform(test[:,0])
        test[:,1]=le_book_table.transform(test[:,1])
        test[:,3]=le_location.transform(test[:,3])
        test[:,4]=le_rest_type.transform(test[:,4])
        test[:,5]=le_cuisines.transform(test[:,5])
        test=test.astype(int)

        rating=ET_Model_loaded.predict(test)
        st.subheader(f"Predicted rating is {rating[0]:.2f}")
    
     

