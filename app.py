from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        sep_len = request.form['sl']
        print(sep_len)
        sep_width = request.form['sw']
        petal_len = request.form['pl']
        print(petal_len)
        petal_width = request.form['pw']
        model = pickle.load(open('iris.pkl','rb'))
        input=np.array([[sep_len,sep_width,petal_len,petal_width]]).astype(np.float64)
        pred=model.predict(input)
        if pred == 0:
            classification = 'Setosa'
        elif pred== 1:
            classification = 'Vercicolor'
        else :
            classification = 'Virginica'
        return render_template('prediction.html', output=classification)
    else:
        return render_template('prediction.html')
    


if __name__ =='__main__':
    app.run()