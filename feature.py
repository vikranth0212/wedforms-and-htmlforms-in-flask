from flask import Flask,request,render_template
from flask_wtf import Form
#in flask we dont have inbuilt forms so we are importings Form
#so install flask_wtf from that import Form
from wtforms import StringField,SubmitField
#in wtforms we use stringfield for input text in html page for entering text 
#and submitfield for submitting the data

FAI=Flask(__name__)
#here name will give instance or current object


#how to create forms using html

@FAI.route('/htmlforms',methods=['GET','POST'])
#to get data from html page to webforms we r using get
#post method is used to activate
#first post method will get activate then get data from html page

def htmlforms():

    if request.method=='POST':
        fd=request.form
        #here we have request.form for getting data
        #return fd['un']
        un2=fd['un']
        return un2
       
    return render_template('htmlforms.html')

#this 1 belongs to html page in flask submit and input is not there as a inbuilt
#so we are creating here
class NameForm(Form):
    name=StringField()
    submit=SubmitField()


#how to create  forms in flask

@FAI.route('/webforms',methods=['GET','POST'])
def webforms():
    NFO=NameForm()

    if request.method=='POST':
        NFDO=NameForm(request.form)
        if NFDO.validate():
            return NFDO.name.data
    return render_template('webforms.html',NFO=NFO)




if __name__=='__main__':
    #FAI.run(debug=True,host='192.168.1.159',port=5001)
    FAI.run(debug=True)