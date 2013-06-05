{% load staticfiles %}
<!doctype html>
<html>
	<head>
    	<meta http-equiv='Content-Type' content='text/html; charset=utf-8'>
		<title>{{ title }}</title>
		<link rel="stylesheet" type="text/css" href="{% static "books/books.css" %}" />
		{% block head %}{% endblock %}
	</head>
	<body>
		<div class="header">
			<div class="branding">
				<h1 class="site-name">Roger's Book Search</h1>
				<div class="site-navigation"><a href="/">Search Books</a><a href="/top">Most Popular</a><a href="/latest">Recently Added</a></div>
				<div class="clear-both"></div>
			</div>
		</div>
		{% block content %}{% endblock %}
	</body>
</html>
