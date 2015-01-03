import accounts
import praw
import sys

r = praw.Reddit('Rammus OK Bot by /u/Xwerve and /u/liquidized')
username = accounts.rammus_ok_bot_user
password = accounts.rammus_ok_bot_pass
subreddits = 'leagueoflegends'
r.login(username, password)
comments = r.get_comments(subreddits)
key_phrase = ['ok', 'ok.']
key_words = ['rammus']
comment_ids = []
sub_ids = []

while True:
	if len(comment_ids) > 100:
		comment_ids.pop(0)
	try:
		comment = next(comments)
	except StopIteration:
		comments = r.get_comments('leagueoflegends')
		comment = next(comments)
	except:
 		os.execv(__file__, sys.argv)
	for phrase in key_phrase:
		if phrase == str(comment).lower() and str(comment.author) != username and str(comment.id) not in comment_ids:
			print(comment, 'posted by', comment.author)
			comment.upvote()
			comment_ids.append(str(comment.id))
			comment.reply('ok')
	for word in key_words:
		if word in str(comment).lower() and str(comment.author) != username and str(comment.id) not in comment_ids:
			print(comment, 'posted by', comment.author)
			comment.upvote()
			comment_ids.append(str(comment.id))
			comment.reply('ok')