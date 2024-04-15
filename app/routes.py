from flask import Flask, url_for, render_template, request, redirect, session
from app import app
from wtforms.fields.html5 import IntegerRangeField
from .forms import SkillsForm
from .helpers import get_soft_skills_data, format_anon_user, get_role, format_skills
import recommender.recommender as rc
#import serpstack as ss
#from app import mongo

@app.route('/')
def home():
    """ route for the home view
    """
    return render_template('home.html', page_name="Home")

@app.route('/about')
def about():
    """ route for the about view
    """
    return render_template('about.html', page_name="About")

@app.route('/myskills', methods=['GET', 'POST'])
def skills_profile():
    """ route for entering soft skills
    """
    # get soft skills categories data
    soft_skills_data = get_soft_skills_data()
    class F(SkillsForm):
        pass
    for skill in soft_skills_data:
        setattr(F, skill["term"], IntegerRangeField(skill["label"], 
            default=0) )
    form = F(username='anonymous')
    if request.method == 'POST' and form.validate():
        session['FORMDATA'] = request.form.to_dict()
        # generate recommendations
        return redirect(url_for('matches'))
    else:
        return render_template('skills_profile.html', page_name='Soft Skills', form=form)

@app.route('/matches')
def matches():
    """ route which displays role matches for user """
    # define users array from anonymous form data
    if session.get('FORMDATA', None):
        # create user from form data
        anon_user = format_anon_user( session.get('FORMDATA') )
        # initialise graph
        G = rc.initialise_graph([anon_user])
        # get job match data
        matches = [m[0] for m in rc.n_best_matches(G, 'anonymous', 10)]
        data = []
        for match in matches:
            role = get_role(match)
            skills = format_skills( rc.get_skills(G, match) )
            data.append({"title": match, "description": role['snippet'], "skills": skills, "url": role['Url']})
        # send match data to template
        return render_template('matches.html', page_name='My Matches', matches=data) 
    else:
        return redirect(url_for('skills_profile'))
