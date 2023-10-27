
'''
import prevail.kinds.header as header
header.build (structure)
'''

def build (structure):
	name = structure ["name"]

	return (
f"""<section
	style="
		border: .05in solid black;
		border-radius: .1in;
		padding: .25in;
	
		margin-bottom: .1in;
	
		display: flex;
		justify-content: space-between;
		align-items: center;
	"
>
	<div>
		<h1>{ name }</h1>
	</div>
</section>"""
	)