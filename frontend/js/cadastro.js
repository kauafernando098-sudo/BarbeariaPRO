async function cadastrar() {

    const username = document.getElementById("username").value
    const senha = document.getElementById("senha").value

    const resposta = await fetch(
        "https://barbeariapro.onrender.com/usuarios/",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                username,
                senha
            })
        }
    )

    const dados = await resposta.json()

    console.log(resposta.status)
    console.log(dados)

    const mensagem = document.getElementById("mensagem")

    if (resposta.ok) {

        mensagem.style.color = "lightgreen"
        mensagem.innerText = "Conta criada com sucesso"
        console.log("REDIRECIONAR PARA LOGIN")
        window.open("login.html", "_self")


    } else {

        mensagem.style.color = "red"
 
        mensagem.innerText = dados.detail
    }
}