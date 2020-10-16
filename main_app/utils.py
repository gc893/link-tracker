from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Link


class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None, user=None):
		self.year = year
		self.month = month
		self.user = user
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, links):
		links_per_day = links.filter(planned_date__day=day, user=self.user)
		d = ''
		for link in links_per_day:
			d += f'<li><a href="{link.address}" target="_blank">{link.title}</a></li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul>{d}</ul></td>"
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, links):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, links)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		links = Link.objects.filter(planned_date__year=self.year, planned_date__month=self.month)
		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, links)}\n'
		return cal