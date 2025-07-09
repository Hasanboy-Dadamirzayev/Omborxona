from django.shortcuts import render
from django.views import View


class StatsView(View):
    def get(self, request):
        return render(request, 'statistikalar.html')

