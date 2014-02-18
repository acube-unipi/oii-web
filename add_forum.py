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
	# print "Forums found: ", len(forums)
	params = {'title': "Forum generale", 'description': "Forum generale di discussione per il laboratorio"}
	my_forum = forum.Forum(**params)
	session.add(my_forum)
	session.commit()

if __name__ == "__main__":
    sys.exit(main())
