from flask import Flask , render_template
app = Flask (name)
@app.route(”/form_atualizar_pessoa”)
def form_atualizar_pessoa():
return render_template(’hello.html’)
app.run()