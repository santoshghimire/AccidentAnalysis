rom models import *
from django.shortcuts import render_to_response


def vote_nepal_page(request):
	parameters = {}
	try:
		election = Election.manager.get().order_by('Election__ElectionDate__election_date')[1:5]
		for ele in election:
			print ele
	except election.DoesNotExist:
		election = None
	parameters['election'] = election
	return render_to_response('vote_nepal_page.html',parameters)

