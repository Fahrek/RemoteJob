from django.shortcuts import render, redirect
# from django.contrib import messages
# from autenticacion.views import acceder, VistaRegistro
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
# from .models import CV

import psycopg2
import psycopg2.extras


# def cv_getUserData(request):
#
#     conn = psycopg2.connect(dbname="tecnojob00", user="postgres", password="47601469W", host="localhost", port=5432)
#     cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#
#     if request.user.is_authenticated:
#
#         current_user = request.user
#         user_id = current_user.id
#         # print(current_user.id)
#
#         # nombre_usuario = form.cleaned_data.get("username")
#         # username_id = request.session.get(id)
#
#         cursor.execute(f"SELECT * FROM auth_user WHERE id = %s", (user_id, ))
#
#         user = cursor.fetchall()
#         params = {
#             "user": user,
#             "user_id": id
#         }
#
#         conn.commit()
#         cursor.close()
#         conn.close()
#
#         return render(request, 'cv_create.html', params)


# def cv_getCandidateData(request):
#
#     conn = psycopg2.connect(dbname="tecnojob00", user="postgres", password="47601469W", host="localhost", port=5432)
#     cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#
#     current_user = request.user
#     user_id = current_user.id
#     # print(current_user.id)
#
#     # nombre_usuario = form.cleaned_data.get("username")
#     # username_id = request.session.get(id)
#
#     # if request.user.is_authenticated:
#
#     cursor.execute(f"SELECT * FROM candidate, user_auth WHERE candidate_id = %s", (user_id,))
#
#     user = cursor.fetchall()
#     params = {
#         "user": user,
#         "user_id": id
#     }
#
#     return render(request, 'cv_create.html', params)


def cv_create(request):

    conn = psycopg2.connect(dbname="tecnojob00", user="postgres", password="47601469W", host="localhost", port=5432)
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # if not request.session.exists(request.session.session_key):
    #
    #     session_key = request.session.create()
    #
    # else:

    # session_key = request.session.session_key

    # session_key = request.session.create()
    #
    # session = Session.objects.get(session_key=session_key)
    # session_data = session.get_decoded()
    # # print session_data
    # uid = session_data.get('_auth_user_id')
    # user_id = User.objects.get(id=uid)

    # conn = psycopg2.connect(dbname="tecnojob00", user="postgres", password="47601469W", host="localhost", port=5432)
    # cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # if request.user.is_authenticated():

    # username = User.objects.all()[0]
    # id = User.objects.get(id=1).pk
    # print(id)

    # uid = user_id.cv.id

    # uid = request.user.id

    # username = User.objects.all()
    # print(user_id)

    # username.CV

    # CV.objects.all()
    # cv = CV()
    # cv.id = user_id
    # print(cv.id)


        # current_user = request.user
        # user_id = current_user.id

        # current_id = Session.objects.get(id)
        # user_id = current_id.id
        # print(current_user.id)

        # username = form.cleaned_data.get("username")
        # user_id = request.session.get(id)

    # cursor.execute(f"SELECT * FROM cv_crud_cv, auth_user WHERE cv_crud_cv.user_id = auth_user.%s;", (uid, ))
    # cursor.execute(f"SELECT * FROM cv_crud_cv, auth_user WHERE cv_crud_cv.user_id = auth_user.id;")
    # cursor.execute(f"SELECT * FROM candidate WHERE id = %s;", (1, ))
    # cursor.execute(f"SELECT * FROM candidate WHERE id = { 1 };")

    # candidate = cursor.fetchall()
    # print(candidate)
    # params = {
    #     "candidate": candidate,
    #     "candidate_id": id
    # }

    # conn.commit()
    # cursor.close()
    # conn.close()

    # return render(request, "cv_create.html", params)

    # elif request.user.is_authenticated() and request.method == 'POST':

    # conn = psycopg2.connect(dbname="tecnojob00", user="postgres", password="47601469W", host="localhost", port=5432)
    # cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    edu_dates   = request.POST.getlist("edu_dates[]",  default=None)
    edu_schools = request.POST.getlist("edu_school[]", default=None)
    edu_awards  = request.POST.getlist("edu_awards[]", default=None)

    exp_dates     = request.POST.getlist("exp_dates[]",     default=None)
    exp_companies = request.POST.getlist("exp_companies[]", default=None)
    exp_positions = request.POST.getlist("exp_position[]",  default=None)

    course_dates = request.POST.getlist("course_dates[]", default=None)
    course_names = request.POST.getlist("course_names[]", default=None)
    course_infos = request.POST.getlist("course_info[]",  default=None)

    skill_names = request.POST.getlist("skill_names[]", default=None)
    skill_infos = request.POST.getlist("skill_info[]",  default=None)

    lang_names  = request.POST.getlist("lang_names[]", default=None)
    lang_levels = request.POST.getlist("lang_level[]", default=None)

    hobby_names = request.POST.getlist("hobby_name[]", default=None)
    hobby_infos = request.POST.getlist("hobby_name[]", default=None)

    project_names = request.POST.getlist("project_name[]", default=None)
    project_infos = request.POST.getlist("project_info[]", default=None)

    other_names = request.POST.getlist("other_name[]", default=None)
    other_infos = request.POST.getlist("other_info[]", default=None)

    for edu_date in edu_dates:
        cursor.execute("INSERT INTO education (edu_date) VALUES (%s);", (edu_date, ))

    for edu_school in edu_schools:
        cursor.execute("INSERT INTO education (edu_school) VALUES (%s);", (edu_school, ))

    for edu_award in edu_awards:
        cursor.execute("INSERT INTO education (edu_awards) VALUES (%s);", (edu_award, ))

    for exp_date in exp_dates:
        cursor.execute("INSERT INTO explab (exp_date) VALUES (%s);", (exp_date, ))

    for exp_company in exp_companies:
        cursor.execute("INSERT INTO explab (exp_company) VALUES (%s);", (exp_company, ))

    for exp_position in exp_positions:
        cursor.execute("INSERT INTO explab (exp_position) VALUES (%s);", (exp_position, ))

    for course_date in course_dates:
        cursor.execute("INSERT INTO course (course_date) VALUES (%s);", (course_date, ))

    for course_name in course_names:
        cursor.execute("INSERT INTO course (course_name) VALUES (%s);", (course_name, ))

    for course_info in course_infos:
        cursor.execute("INSERT INTO course (course_info) VALUES (%s);", (course_info, ))

    for skill_name in skill_names:
        cursor.execute("INSERT INTO skill (skill_name) VALUES (%s);", (skill_name, ))

    for skill_info in skill_infos:
        cursor.execute("INSERT INTO skill (skill_info) VALUES (%s);", (skill_info, ))

    for lang_name in lang_names:
        cursor.execute("INSERT INTO lang (lang_name) VALUES (%s);", (lang_name, ))

    for lang_level in lang_levels:
        cursor.execute("INSERT INTO lang (lang_level) VALUES (%s);", (lang_level, ))

    for hobby_name in hobby_names:
        cursor.execute("INSERT INTO hobby (interest_name) VALUES (%s);", (hobby_name, ))

    for hobby_info in hobby_infos:
        cursor.execute("INSERT INTO hobby (interest_info) VALUES (%s);", (hobby_info, ))

    for project_name in project_names:
        cursor.execute("INSERT INTO project (project_name) VALUES (%s);", (project_name, ))

    for project_info in project_infos:
        cursor.execute("INSERT INTO project (project_info) VALUES (%s);", (project_info, ))

    for other_name in other_names:
        cursor.execute("INSERT INTO other (other_name) VALUES (%s);", (other_name, ))

    for other_info in other_infos:
        cursor.execute("INSERT INTO other (other_infos) VALUES (%s);", (other_info, ))

    # cv_txt = request.POST.get("cv_txt", default=None)
    #
    # cursor.execute("INSERT INTO cv (cv_to_txt) values (%s)", (cv_txt, ))

    # conn.commit()
    # cursor.close()
    # conn.close()

    # messages.success(request, "El currículum se ha generado correctamente")

    # else:

    # messages.error(request, "El currículum no se ha guardado correctamente")

    conn.commit()
    cursor.close()
    conn.close()

    # return render(request, "cv_create.html", params)
    return render(request, "cv_create.html")


def cv_generate(request):
    return render(request, "cv_generate.html")
    # return redirect("leer_cv")