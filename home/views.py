from django.shortcuts import render

# Create your views here.
def index(request):
	return render(
		request,
		'index.html',
		{
			"introduction" : {
				"name" :"Henrique Oliveira", 
				"text" : "Software Developer, Agile Enthusiast"
			},
			"links" : {
				"twitter" : "https://twitter.com/henriqueso",
				"github" : "https://github.com/henriqueso",
				"linkedin" : "https://br.linkedin.com/in/henriqueso"
			}
		}
	)