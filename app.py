from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        risco = request.form.get("risco").upper()
        valor = float(request.form.get("valor"))

        if risco not in ["BX", "AL"]:
            resultado = f"{risco} é inválido para o grau de risco"
        else:
            if risco == "BX":
                tipo = "Poupança" if valor < 1000 else "Renda Fixa"
            else:
                tipo = "Bitcoins" if valor < 1000 else "Ações"

            resultado = f"Você deve investir em {tipo}"

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
