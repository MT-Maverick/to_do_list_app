from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)
list=[]

@app.route('/')
def index():
	return render_template('index.html',tasks=list)

@app.route('/add',methods=['POST'])
def add_task():
	task = request.form['task']
	list.append(task)
	return redirect(url_for('index'))


@app.route('/remove',methods=['POST'])
def remove_task():
	task_index = int(request.form['task_index'])
	if 0 <= task_index < len(list):
		del list[task_index]
	return redirect(url_for('index'))


@app.route('/edit',methods=['GET'])
def edit_task():
	task_index = int(request.args.get('task_index'))
	if 0 <= task_index < len(list):
		task_to_edit = list[task_index]
		del list[task_index]
		return render_template('edit.html',task_to_edit = task_to_edit, task_index = task_index)
	else:
		return "Invalide task index"

@app.route('/update',methods=['POST'])
def update_task():
	task_index = int(request.form['task_index'])
	edited_task = request.form['edited_task']
	if 0<= task_index < len(list)+1:
		list.insert(task_index,edited_task)
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)

