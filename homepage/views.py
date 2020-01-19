from django.contrib import auth
from django.shortcuts import render


# Create your views here.

def index_page(request):
    return render(request, 'homepage/index.html', {'username': auth.get_user(request).username, 'image': img})


def articles(request):
    return render(request, 'homepage/articles.html', {'username': auth.get_user(request).username})


img = {
    'mainbuilding': '<div id="sloi-1" style="display: block; background: rgba(0, 0, 0, 0) url(static/img/map.png) no-repeat scroll 0% 0% / 100%; width: 500px; height: 600px;"><svg id="svgmainid-sloi-1" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" width="500" height="600" viewBox="0 0 500 600" preserveAspectRatio="xMinYMin meet" fixpropchecked="true"><a href="#poligon" id="apoly-1" onclick="perehodKSloy(\'sloi-2\')"><polygon id="poly-1" points=" 168,367 160,384 168,388 174,372" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a></svg></div>',
    'hoz_korp': '<div id="sloi-2"  style="display: none; background: rgba(0, 0, 0, 0) url(static/img/f.png) no-repeat scroll 0% 0% / 100%; width: 500px; height: 500px;"><svg id="svgmainid-sloi-1" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" width="500" height="500" viewBox="0 0 500 500" preserveAspectRatio="xMinYMin meet" fixpropchecked="true"><a href="#poligon" id="apoly-4"><polygon id="poly-4" points=" 74,41 69,125 213,125 209,42" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-8"><polygon id="poly-8" points=" 423,127 423,213 355,213 355,128" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-9"><polygon id="poly-9" points=" 228,148 174,148 174,211 228,210" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-10"><polygon id="poly-10" points=" 137,148 173,148 172,211 137,210" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-11"><polygon id="poly-11" points=" 73,128 73,209 135,211 137,129" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-12"><polygon id="poly-12" points=" 213,40 215,124 373,125 373,88 420,85 420,44" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-13"><polygon id="poly-13" points=" 375,88 375,124 420,124 420,90" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-14"><polygon id="poly-14" points=" 314,154 313,208 354,209 354,153" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-15"><polygon id="poly-15" points=" 270,146 270,209 313,209 313,148" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-16"><polygon id="poly-16" points=" 314,129 314,151 353,149 355,130" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a><a href="#poligon" id="apoly-17"><polygon id="poly-17" points="" fill="#d2d2d2" fillhover="#e5e5e5" stroke-width="1" fill-rule="nonzero" fill-opacity="0.8" stroke-linecap="round" stroke-linejoin="round" stroke="#333333"></polygon></a></svg></div></svg></div>',
}
