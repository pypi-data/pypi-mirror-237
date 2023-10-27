

'''
plan:

import prevail

prevail.abundantly ({
	"build": [{
		"kind": "header"
	}]
})

'''

import prevail.kinds.header as header
import prevail.kinds.company as company
import prevail.kinds.project as project

from flask import Flask

def abundantly (OBJECT):
	BUILDS = OBJECT ["build"]
	
	html_document = {
		"start": (
"""
<html>
<head></head>
<body>
<style>
h1, h2, h3, p, ul, li {
	margin: 0;
	padding: 0;
}

ul {
	padding-left: 20px;
}

main {
	position: relative;
	margin: 0 auto;
	width: 8.5in;
	height: 11in;
}

</style>
<main>

"""),
		"main": "",
		"end": (
"""
</main>
</body>
""")
	}
	
				
	

	for structure in BUILDS:
		kind = structure ["kind"]
		fields = structure ["fields"]
		
		if (kind == "header"):
			html_document ["main"] += header.build ({
				"name": structure ["fields"] ["name"]
			})
		
		elif (kind == "company"):
			html_document ["main"] += company.introduce (fields)
		
		elif (kind == "academics"):
			pass;
			
		elif (kind == "projects"):
			html_document ["main"] += project.present (fields)
			
		else:
			print (f'Kind "{ kind }" is not an option.')
			

	html_string = (
		html_document ["start"] + 
		html_document ["main"] + 
		html_document ["end"]
	)


	app = Flask (__name__)
	@app.route ("/")
	def prevail ():
		return html_string

	app.run (
		debug = True
	)

	return;