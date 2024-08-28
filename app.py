from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def task_list():
    return render_template('task_list.html', tasks=tasks)

# When a task is added, ensure 'completed' is always set to False
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_name = request.form.get('name')
        if task_name:
            new_task = {'name': task_name, 'completed': False}
            tasks.append(new_task)
            print(f"Task added: {new_task}")  # Debug print
            return redirect(url_for('task_list'))
    return render_template('add_task.html')


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('task_list'))

if __name__ == '__main__':
    app.run(debug=True)
