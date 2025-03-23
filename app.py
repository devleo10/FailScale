from flask import Flask, render_template, request
import random

app = Flask(__name__)


MEME_COMMENTS = {
    "high": [
        "Wow look at Mr. Productivity over here!",
        "Someone's trying too hard to adult!",
        "Found the overachiever!",
        "Do you even Netflix, bro?"
    ],
    "medium": [
        "Basic human functionality achieved!",
        "Mediocrity at its finest!",
        "Congratulations, you're average!",
        "Could be worse... could be better"
    ],
    "low": [
        "Are you even trying?",
        "Professional couch potato!",
        "Living that sofa-king lazy life!",
        "Is your spirit animal a sloth?"
    ]
}


GIFS = {
    "high": "https://i.imgur.com/8CAx0ES.gif", 
    "medium": "https://media1.tenor.com/m/1YXq17YXn98AAAAd/chill-dude-chill.gif", 
    "low": "https://media1.tenor.com/m/BE2tstTEGEcAAAAC/reaction-meme-stan-twt.gif"      
}
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/assess', methods=['POST'])
def assess():
  
    procrastination = int(request.form['procrastination'])
    coffee = int(request.form['coffee'])
    motivation = int(request.form['motivation'])
    weekend_plans = int(request.form['weekend_plans'])
    
   
    total_score = (procrastination * 3) + (coffee * 2) + motivation + (weekend_plans * 2)
    
    
    if total_score >= 60:
        category = "high"
    elif total_score >= 30:
        category = "medium"
    else:
        category = "low"
    
  
    result = {
        "score": total_score,
        "comment": random.choice(MEME_COMMENTS[category]),
        "gif": GIFS[category],
        "category": category
    }
    
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)