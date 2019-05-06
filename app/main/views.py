from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Technology, TechCom, Science, SciCom, Employment,EmpCom, Sports, SpoCom, Religion, RelCom
from .. import db,photos
from flask_login import login_required, current_user
from .forms import *
import markdown2



@main.route('/')
def index():

    return render_template('index.html')

@main.route('/technology', methods = ['GET','POST'])
@login_required
def technology():
    form = TPitchForm()
    title = 'Technology pitches'
    if form.validate_on_submit():
        pitch = form.pitch.data
        new_technology = Technology(pitch=pitch, user=current_user)
        db.session.add(new_technology)
        db.session.commit()
        return redirect(url_for('.alltechpitches'))

    return render_template("technology/technology.html", title = title, tpitch_form= form)


@main.route('/technology/<int:id>',  methods=['GET', 'POST'])
@login_required
def techid(id):

    technology = Technology.query.get(id)
    form = CommentTPitchForm()
    if form.validate_on_submit():
        techcom = form.techcom.data
        new_techcom = TechCom(techcom=techcom, tech_id=id, user=current_user)
        new_techcom.save_techcom()

    techcom = TechCom.query.filter_by(tech_id=id).all()
    return render_template('technology/techies.html',techform=form, techcomments = techcom, technology=technology)

@main.route('/technologies')
@login_required
def alltechpitches():
    title = 'all techpiches'
    pitches = Technology.query.order_by(Technology.id).all()
    return render_template("technology/tech.html", title=title, pitches=pitches )


@main.route('/employment', methods = ['GET','POST'])
@login_required
def employment():
    form = TPitchForm()
    title = 'Employment pitches'
    if form.validate_on_submit():
        pitch = form.pitch.data
        new_employment= Employment(pitch=pitch, user=current_user)
        db.session.add(new_employment)
        db.session.commit()
        return redirect(url_for('.allemploypitches'))

    return render_template("employment/employment.html", title = title, epitch_form= form)


@main.route('/employment/<int:id>',  methods=['GET', 'POST'])
@login_required
def employid(id):

    employment = Employment.query.get(id)
    form = CommentEPitchForm()
    if form.validate_on_submit():
        empcom = form.empcom.data
        new_empcom = EmpCom(empcom=empcom, employ_id=id, user=current_user)
        new_empcom.save_empcom()

    empcom = EmpCom.query.filter_by(employ_id=id).all()
    return render_template('employment/employ.html',employform=form, employcomments = empcom, employment=employment)

@main.route('/employments')
@login_required
def allemploypitches():
    title = 'employment pitches'
    pitches = Employment.query.order_by(Employment.id).all()
    return render_template("employment/emp.html", title=title, pitches=pitches )


@main.route('/science', methods = ['GET','POST'])
@login_required
def science():
    form = SCPitchForm()
    title = 'Science pitches'
    if form.validate_on_submit():
        pitch = form.pitch.data
        new_science = Science(pitch=pitch, user=current_user)
        db.session.add(new_science)
        db.session.commit()
        return redirect(url_for('.allsciencepitches'))

    return render_template("science/science.html", title = title, scpitch_form= form)


@main.route('/science/<int:id>',  methods=['GET', 'POST'])
@login_required
def scienid(id):

    science = Science.query.get(id)
    form = CommentSCPitchForm()
    if form.validate_on_submit():
        scicom = form.scicom.data
        new_scicom = SciCom(scicom=scicom, scien_id=id, user=current_user)
        new_scicom.save_scicom()

    scicom = SciCom.query.filter_by(scien_id=id).all()
    return render_template('science/scien.html',scienceform=form, sciencecomments = scicom, science=science)

@main.route('/sciences')
@login_required
def allsciencepitches():
    title = 'science pitches'
    pitches = Science.query.order_by(Science.id).all()
    return render_template("science/sciences.html", title=title, pitches=pitches )



@main.route('/sports', methods = ['GET','POST'])
@login_required
def sports():
    form = SPitchForm()
    title = 'Technology pitches'
    if form.validate_on_submit():
        pitch = form.pitch.data
        new_sports = Sports(pitch=pitch, user=current_user)
        db.session.add(new_sports)
        db.session.commit()
        return redirect(url_for('.allsportpitches'))

    return render_template("sports/sports.html", title = title, spitch_form= form)


@main.route('/sports/<int:id>',  methods=['GET', 'POST'])
@login_required
def sportsid(id):

    sports = Sports.query.get(id)
    form = CommentSPitchForm()
    if form.validate_on_submit():
        spocom = form.spocom.data
        new_spocom = SpoCom(spocom=spocom, sport_id=id, user=current_user)
        new_spocom.save_spocom()

    spocom = SpoCom.query.filter_by(sport_id=id).all()
    return render_template('sports/sport.html',sportform=form, sportcomments = spocom, sports=sports)

@main.route('/sportify')
@login_required
def allsportpitches():
    title = 'all techpiches'
    pitches = Technology.query.order_by(Technology.id).all()
    return render_template("sports/sportify.html", title=title, pitches=pitches )




@main.route('/religion', methods = ['GET','POST'])
@login_required
def religion():
    form = RPitchForm()
    title = 'Religion pitches'
    if form.validate_on_submit():
        pitch = form.pitch.data
        new_religion = Religion(pitch=pitch, user=current_user)
        db.session.add(new_religion)
        db.session.commit()
        return redirect(url_for('.allreligionpitches'))

    return render_template("religion/religion.html", title = title, rpitch_form= form)


@main.route('/religion/<int:id>',  methods=['GET', 'POST'])
@login_required
def religid(id):

    religion = Religion.query.get(id)
    form = CommentRPitchForm()
    if form.validate_on_submit():
        relcom = form.relcom.data
        new_relcom = RelCom(relcom=relcom, relig_id=id, user=current_user)
        new_relcom.save_relcom()

    relcom = RelCom.query.filter_by(relig_id=id).all()
    return render_template('religion/religous.html',relform=form, relcomments = relcom, religion=religion)

@main.route('/religous')
@login_required
def allreligionpitches():
    title = 'religion pitches'
    pitches = Religion.query.order_by(Religion.id).all()
    return render_template("religion/rel.html", title=title, pitches=pitches )



@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))
