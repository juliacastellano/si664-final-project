# Hospital Payment and Value of Care

## Purpose
I am interested in creating a database and Django app for a dataset related to healthcare.
For the Django application, I believe it would be helpful to have a list of
states to choose from. Once a state is chosen, it will show all of the hospitals
within that state that have data. The user can then choose a hospital, where they
will then see a list of the different ailments. Once the user chooses a specific
ailment to look at, they will see the payment and value of care information for
that particular illness at that specific hospital. I think this is the best way
to do it because the hospitals have data for different ailments. I also think it
would be a good idea to have a hospital information tab, where the user can choose
a specific hospital and it will display the address and phone information for the
hospital.

## Data set
I chose the “Hospital Payment and Value of Care dataset
(https://www.kaggle.com/cms/paymentandvalue2017).
This dataset includes information on payment and value of care for a number of
hospitals in the United States. The dataset includes data for a variety of common
ailments, such as heart attack and pneumonia.

## Data model
![alt text](https://github.com/juliacastellano/si664-final-project/blob/master/static/img/UPDATED-si664-final-project-datamodel.png)

## Package Dependencies
Package                Version   
---------------------- ----------
certifi                2018.11.29
chardet                3.0.4     
coreapi                2.3.3     
coreschema             0.0.4     
defusedxml             0.5.0     
Django                 2.1.4     
django-allauth         0.38.0    
django-cors-headers    2.4.0     
django-crispy-forms    1.7.2     
django-filter          2.0.0     
django-rest-auth       0.9.3     
django-rest-swagger    2.2.0     
djangorestframework    3.9.0     
idna                   2.8       
itypes                 1.1.0     
Jinja2                 2.10      
MarkupSafe             1.1.0     
mysqlclient            1.3.14    
numpy                  1.15.3    
oauthlib               2.1.0     
openapi-codec          1.3.2     
Pillow                 5.3.0     
pip                    18.1      
PyJWT                  1.7.1     
python3-openid         3.1.0     
pytz                   2018.7    
PyYAML                 3.13      
requests               2.21.0    
requests-oauthlib      1.0.0     
setuptools             39.0.1    
simplejson             3.16.0    
six                    1.12.0    
social-auth-app-django 3.1.0     
social-auth-core       2.0.0     
uritemplate            3.0.0     
urllib3                1.24.1    
virtualenv             16.0.0    
wheel                  0.30.0    
wordcloud              1.5.0  