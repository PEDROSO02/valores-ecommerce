from flask import Flask, render_template, request
from precificacao import shopee, mercado_livre, elo7, tiktok

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/precificacao", methods=["GET", "POST"])
def precificacao_page():
    resultado = None

    if request.method == "POST":
        valor = float(request.form["valor"])
        lucro = float(request.form["lucro"])
        plataforma = int(request.form["plataforma"])

        if plataforma == 1:
            resultado = mercado_livre.calculo_ml(valor, lucro)

        elif plataforma == 2:
            resultado = shopee.calculo_shopee(valor, lucro)

        elif plataforma == 3:
            resultado = elo7.calculo_elo(valor, lucro)

        elif plataforma == 4:
            resultado = tiktok.calculo_tiktok(valor, lucro)

    return render_template("precificacao.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)