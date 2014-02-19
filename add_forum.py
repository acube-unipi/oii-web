#!/usr/bin/env python

import sys
import gevent

from cms.db import forum, Session

# local = gevent.local.local()

def main():
	# Get session
	session = Session()
	# Apre una sessione e lista i forum
	# forums = session.query(Forum).all()
	forums = session.query(forum.Forum).all()
	print "Forums found: ", len(forums)
	params = {'title': "Discussioni sul sito", 'description': "Per malfunzionamenti, dubbi o suggerimenti relativi al sito."}
	my_forum = forum.Forum(**params)
	session.add(my_forum)
	session.commit()

if __name__ == "__main__":
    sys.exit(main())
