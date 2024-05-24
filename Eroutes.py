# Search
# @app.route('/search', methods=['POST'])
# def search():
#     form = SearchForm()
#     data = data.query
#     if form.validate_on_submit():
#         post_searched = form.searched.data
#         data = data.filter(data.snippet.like('%' + data.searched + '%'))
#         data = data.order_by(data.job_id).all()
#         return render_template("search.html", form=form,
#                                searched = post_searched, 
#                                data = data)
@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query', '').lower()
    results = [role for role in data if query in role['snippet'].lower()]
    return render_template("search.html", form=None, searched=query, data=results)