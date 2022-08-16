from flask import render_template, url_for
from yc import app, db
from yc.models import Company, Founder

# db.drop_all()
# db.create_all()
# companies = st.load('pkl/companies_with_founders')
# ncs = []
# for com in companies:
#     nc = Company(name=com.name)
#     db.session.add(nc)
#     for founder in com.founders:
#         nf = Founder(name=founder.name, twitter=founder.twitter, linkedin=founder.linkedin, company=nc)
#         if founder.linkedin == 'https://www.linkedin.com/in/kylevogt/':
#             print(nf.company)
#         db.session.add(nf)
# db.session.commit()

@app.route('/')
@app.route('/home')
def home():
    founders = Founder.query.all()
    return render_template('home.html', founders=founders)
