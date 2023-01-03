# # # # #
from flask import Flask,request,render_template,jsonify
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
###
@app.route('/')
def test0():
    return render_template('Test0.html')

@app.route('/Test1')
def test1():
    return render_template('Test1.html')

@app.route('/Test2')
def test2():
    return render_template('Test2.html')

@app.route('/Test3')
def test3():
    return render_template('Test3.html')

@app.route('/Test4')
def test4():
    return render_template('Test4.html')

@app.route('/Test5')
def test5():
    return render_template('Test5.html')

@app.route('/data')
def data():
    m1 = request.args.get('m1')
    m2 = request.args.get('m2')
    if m1 == '' or m2 == '' or m1 == None or m2 == None:
        m1 = 0
        m2 = 100000
    else:
        m1 = int(m1)
        m2 = int(m2)

    import pandas as pd
    df = pd.DataFrame.from_dict()
    df = df[(df.visits >= m1) & (df.visits <= m2)]
    return jsonify(df.to_dict(orient='records'))

@app.route('/chart')
def chart():
    x1 = float(request.args.get('x1'))
    x2 = int(request.args.get('x2'))
    x3 = int(request.args.get('x3'))

    x1 = x1/30

    from joblib import load
    import pandas as pd
    from sklearn.metrics import classification_report, confusion_matrix


    # x1=3.49 # 價格
    # x2=0 # 0:小, 1:大, 2:中, 3:中下
    # x3=1 # 0:沒成就, 1:有成就
    x4 = pd.DataFrame({'price': pd.Series(x1), 'publisher_count_clustering_4' : pd.Series(x2), 'is_achievements' : pd.Series(x3)})

    AdaBoostc = load('C:\\workspace\\CSS\\model\\AdaBoostc.joblib')
    rfc = load("C:\\workspace\\CSS\\model\\rfc.joblib")
    GradientBoost = load('C:\\workspace\\CSS\\model\\GradientBoost.joblib')


    y1 = AdaBoostc.predict(x4)
    y2 = rfc.predict(x4)
    y3 = GradientBoost.predict(x4)


    y_final = y1+y2+y3

    if y_final >= 2:
        y = 1       
        print(y)
        return render_template('Test5y_1.html')
    else:
        y = 0        
        print(y) # 1:好評, 0:壞評
        return render_template('Test5y_0.html')




    # return render_template('Test5_play.html')






@app.route('/temp')
def temp():
    return render_template('Test5.html')


# @app.route('/play',methoods=['POST'])
# def postInput():
#     #前端傳來的數值
#     # insertValues = request.get_json()
#     x1=request.args.get('x1')
#     x2=request.args.get('x2')
#     x3=request.args.get('x3')
#     input=(x1,x2,x3)
#     return render_template('Test5_play',input)

#     #result = model.play(input)
#     #return jsonify({'return':result})

# @app.route('/result')
# def result():
#     return render_template('Test5.html')

###
app.run()