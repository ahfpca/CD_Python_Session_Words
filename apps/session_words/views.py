from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from time import strftime

# Create your views here.
def index(request):
    return render(request, "session_words/index.html")


def add_word(request):
    if request.method == "POST":
        if not "words" in request.session:
            request.session["words"] = []

        #print("\n", "#" * 50, "\n", request.POST)

        if len(request.POST["word"].strip()) > 0:
            records = request.session["words"]

            font_mode = "size1"
            # if "font_mode" in request.POST:
            #     font_mode = "size2"
            if request.POST.get("font_mode", False):
                font_mode = "size2"
                

            curDateTime = datetime.now().strftime('%I:%M:%S%p, %B %d %Y')

            rec = {
                "word": request.POST["word"],
                "color": request.POST["color"],
                "font_mode": font_mode,
                "created_at": curDateTime
            }

            records.append(rec)

            request.session["words"] = records
            #print("\n", "#" * 50, "\n", records)

    return redirect("/session_words")


def clear(request):
    if request.method == "POST":
        request.session.flush()
    
    return redirect("/session_words")
