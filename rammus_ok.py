import accounts
import praw

r = praw.Reddit('Rammus OK Bot by /u/Xwerve and /u/liquidized')
username = accounts.rammus_ok_bot_user
password = accounts.rammus_ok_bot_pass
subreddit = r.get_subreddit('thomascirclejerk')
subreddits = 'thomascirclejerk'
r.login(username, password)
posts = subreddit.get_new()
comments = r.get_comments(subreddits)
key_phrase = ['ok', 'ok.']
key_words = ['rammus']
link_words = ['thomas']
comment_ids = []
sub_ids = []

while True:
	try:
		comment = next(comments)
		post = next(posts)
	except StopIteration:
		posts = subreddit.get_new()
		comments = r.get_comments('leagueoflegends')
		comment = next(comments)
		post = next(posts)
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
	for word in link_words:
		if word in str(post).lower() and str(comment.author) != username and str(comment.id) not in comment_ids: