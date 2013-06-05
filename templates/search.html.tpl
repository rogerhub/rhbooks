{% extends 'main.html.tpl' %}
{% load staticfiles %}
{% block head %}
<script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script type="text/javascript" src="{% static "books/search.js" %}"></script>
<script type="text/javascript" src="{% static "books/results.js" %}"></script>
{% endblock %}
{% block content %}
<div class="search-form">
	<div class="search-box">
		<form action="/search" method="get">
			<input type="text" name="q" class="search-text" placeholder="Type here to search" value="{{ query }}" /><br />
			<button type="submit" class="search-submit">Search Books</button>
		</form>
	</div>
</div>
{% if results %}
<div class="results">
	<div class="results-box">
		{% if query %}<h2 class="result-query">Results for "{{ query }}"</h2>{% endif %}
		<ul class="result-list">
		{% for result in queryset %}
		<li class="result">
			<h3 class="result-title"><a href="{{ result.get_url }}" data-track="/hit?id={{ result.id }}" class="js-track">{{ result.title }} by {{ result.author }}</a></h3>
		</li>
		{% empty %}
		<div class="result-empty">No results found.</div>
		{% endfor %}
		</ul>
	</div>
</div>
{% endif %}
{% endblock %}
