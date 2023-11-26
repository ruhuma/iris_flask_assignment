from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        sep_len = request.form['sl']
        sep_width = request.form['sw']
        petal_len = request.form['pl']
        petal_width = request.form['pw']
        #model = pickle.load(open('model.pkl','rb'))
        #input=np.array([[sep_len,sep_width,petal_len,petal_width]]).astype(np.float64)
        #pred=model.predict(input)
        return render_template('prediction.html', output=sep_width)
    else:
        return render_template('prediction.html')
    


if __name__ =='__main__':
    app.run()