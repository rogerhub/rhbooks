{% extends 'main.html.tpl' %}
{% load staticfiles %}
{% block head %}
<script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script type="text/javascript" src="{% static "books/results.js" %}"></script>
{% endblock %}
{% block content %}
<div class="results">
	<div class="results-box">
		<h2 class="result-query">Recently Added Books</h2>
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
{% endblock %}
