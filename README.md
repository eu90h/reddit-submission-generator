# reddit-submission-generator
Generates reddit submissions using a Markov generator trained on submissions from a given subreddit. The results could use improvement, but it was just for fun anyway.

Usage
-----

	python3 reddit_generator.py --help

	usage: reddit_generator.py [-h] [--new] [--num_submissions N] subreddit

	Reddit Submission Generator

	positional arguments:
  	subreddit             subreddit to train the markov generator with

	optional arguments:
  	-h, --help            show this help message and exit
  	--new                 new markov chain with latest top 100 subreddit posts
		--num_submissions N, -n N
    	                    number of submissions to generate
