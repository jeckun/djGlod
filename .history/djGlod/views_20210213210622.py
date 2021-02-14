# -*- coding: utf-8 -*-
import os
import json
from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world ! ")


def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)


def get_json(request):
    jsfile = (
        [1254355200000, 185.35, 186.22, 180.70, 180.86],
        [1254441600000, 181.41, 185.94, 181.35, 184.90],
        [1254700800000, 186.20, 186.86, 184.27, 186.02],
        [1254787200000, 187.74, 190.01, 187.30, 190.01],
        [1254873600000, 189.76, 190.55, 189.03, 190.25],
        [1254960000000, 190.66, 191.45, 188.89, 189.27],
        [1255046400000, 188.97, 190.70, 188.62, 190.47],
        [1255305600000, 191.02, 191.51, 189.64, 190.81],
        [1255392000000, 190.63, 191.17, 189.70, 190.02],
        [1255478400000, 192.25, 192.32, 190.23, 191.29],
        [1255564800000, 189.63, 190.92, 189.53, 190.56],
        [1255651200000, 189.35, 190.36, 187.84, 188.05],
        [1255910400000, 187.85, 190.00, 185.55, 189.86],
        [1255996800000, 200.60, 201.75, 197.85, 198.76],
        [1256083200000, 199.52, 208.71, 199.23, 204.92],
        [1256169600000, 204.70, 207.85, 202.51, 205.20],
        [1256256000000, 205.70, 205.80, 203.23, 203.94],
        [1256515200000, 203.67, 206.75, 200.10, 202.48],
        [1256601600000, 201.66, 202.81, 196.45, 197.37],
        [1256688000000, 197.71, 198.02, 191.10, 192.40],
        [1256774400000, 195.00, 196.81, 192.14, 196.35],
        [1256860800000, 196.06, 196.80, 186.07, 188.50],
    )
    # filename = os.path.join(os.path.dirname(os.path.dirname(
    #     os.path.abspath(__file__))), 'templates', 'jsonp.json')
    # print(filename)

    # def read_json(filename):
    #     with open(filename, 'r', encoding='utf-8') as f:
    #         return json.loads(f.readline(), encoding='utf-8')
    # js = read_json(filename)
    return HttpResponse(json.dumps(jsfile))
