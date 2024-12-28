import pathlib, re
from django.http import HttpResponse
from django.shortcuts import render
# import table from database
from visits.models import PageVisit
# `from proj.context_processors import page_visit_count` is importing the `page_visit_count` function
# from the `context_processors` module within the `proj` package. This function is likely used to
# handle some logic related to counting page visits or processing context data for rendering templates
# in the Django project.
# from proj.context_processors import page_visit_count
# The line `from collections import defaultdict` is importing the `defaultdict` class from the
# `collections` module in Python. `defaultdict` is a subclass of the built-in `dict` class that
# returns a default value when a key that does not exist in the dictionary is accessed. This can be
# useful in scenarios where you want to ensure that a certain default value is returned for keys that
# are not present in the dictionary.
# from collections import defaultdict


this_dir = pathlib.Path(__file__).resolve().parent.parent

dict_ = {
  'developer_name':'Filip Isakovic',
  'title':'Santa Cruz College student',
  'visited_count': 0,
  'visited_total':0,
}

def home_page_view(request, *args, **kwargs):
  html_template = 'main.html'
  # page_visit_count('main')
  record = PageVisit.objects.get(id=1) 
  record.main +=  1
  record.save()
  r = PageVisit.objects.filter(id=1)[0]
  dict_['visited_count'] = r.python
  dict_['visited_total'] = r.python + r.main + r.template + r.extended + r.login  
  return render(request, html_template, dict_)

def python_load_home_page(request, *args, **kwargs):

  # html_ = re.sub("XX", "{developer_name}", home_file_path.read_text()).format(**dict_)
  html_ = (this_dir / 'templates/home.html').read_text()
  
  record = PageVisit.objects.get(id=1) 
  record.python += 1
  record.save()
  r = PageVisit.objects.filter(id=1)[0]
  dict_['visited_count'] = r.python
  dict_['visited_total'] = r.python + r.main + r.template + r.extended + r.login
  
  #  page loaded with read_text() looses placeholders ability so we just replace manually 
  html_ = re.sub("{{ developer_name }}", dict_["developer_name"], html_)
  html_ = re.sub("{{ visited_count }}", str(dict_["visited_count"]), html_)
  html_ = re.sub("{{ visited_total }}", str(dict_["visited_total"]), html_)
  html_ = re.sub("{{ title }}", "Dictionary value replaced and rendered with Django Templating Engine", html_)
  
  return HttpResponse(html_)

def template_home_page(request, *args, **kwargs):
  dict = {
    'developer_name':'Filip Isakovic',
    'title': 'Dictionary value replaced and rendered with Django Templating Engine',
    'visited_count':0
  }
  html_template = 'home.html'
  record = PageVisit.objects.get(id=1) 
  record.template += 1
  record.save()
  r = PageVisit.objects.filter(id=1)[0]
  dict['visited_count'] = r.template
  dict['visited_total'] = r.python + r.main + r.template + r.extended + r.login
  return render(request, html_template, dict)

def template_extended_page(request, *args, **kwargs):
  html_template = 'extended.html'
  record = PageVisit.objects.get(id=1) 
  record.extended += 1
  record.save()
  r = PageVisit.objects.filter(id=1)[0]
  dict_['visited_count'] = r.extended
  dict_['visited_total'] = r.python + r.main + r.template + r.extended + r.login
  return render(request, html_template, dict_)

def login_extended_page(request, *args, **kwargs):
  html_template = 'login.html'
  
  return render(request, html_template, dict_)
