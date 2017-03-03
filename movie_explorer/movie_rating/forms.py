from django import forms

# This gives value then name
SortOptions = (
    ('popularity.desc', 'Popularity'),
    ('release_date.desc', 'Release Date Descending'),
    ('release_date.asc', 'Release Date Ascending'),
)

Genres = (
    ('28', 'Action'),
    ('12', 'Adventure'),
    ('16', 'Animation'),
    ('35', 'Comedy'),
    ('80', 'Crime'),
    ('99', 'Documentary'),
    ('18', 'Drama'),
    ('10751', 'Family'),
    ('14', 'Fantasy'),
    ('36', 'History'),
    ('27', 'Horror'),
    ('10402', 'Music'),
    ('9648', 'Mystery'),
    ('10749', 'Romance'),
    ('878', 'Sci-Fi'),
    ('10770', 'TV Movie'),
    ('53', 'Thriller'),
    ('10752', 'War'),
    ('37', 'Western'),
)

class SortForm(forms.Form):
    sort_by = forms.ChoiceField(widget=forms.Select(attrs={'onchange': 'this.form.submit();'}), choices=SortOptions)
