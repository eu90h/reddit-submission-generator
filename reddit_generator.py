#!/usr/bin/python3
# Reddit Markov Submission Generator by eu90h
# Uses a markov chain trained on the submission titles of a given subreddit
import praw, unittest, os, sys, argparse
from pymarkovchain import MarkovChain

# Integer String -> List[String]
# grabs N submissions from theredpill, returning a list of strings of the format '<upvotes> :: <title>'
def getSubmissions(N, subreddit):
	r =  praw.Reddit(user_agent='mac:reddit_title_markov_gen:v0.0.1 (by /u/eu90h)')
	submissions = r.get_subreddit(subreddit).get_new(limit=N)
	return [str(x) for x in submissions]

# List[String] -> List[String]
# gets the titles for a list of submissions
def getTitles(submissions):
	return [sub.split(' :: ')[1] for sub in submissions]

# Args -> Void
# initializes the markov chain with trp submission titles and prints N titles to stdout
def main(args):
	markov_filename = "./" + args.subreddit + ".mcd"
	new_chain = os.path.isfile(markov_filename) == False # this must come before the creation of the Markov Chain
	mc = MarkovChain(markov_filename)

	if args.new or new_chain:
		titles = getTitles(getSubmissions(100, args.subreddit))
		training_data = str.join('.', titles)
		mc.generateDatabase(training_data)

	N = args.num_submissions
	while N > 0:
		print(mc.generateString())
		N -= 1

# the entry point, just calls main
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Reddit Submission Generator')
	parser.add_argument('--new', default=False, action='store_true', help='new markov chain with latest top 100 subreddit posts')
	parser.add_argument('--num_submissions', '-n',  metavar="N", type=int, default=1, help='number of submissions to generate')
	parser.add_argument('subreddit', metavar='subreddit', type=str, help='subreddit to train the markov generator with')
	main(parser.parse_args())
