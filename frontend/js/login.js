async function login() {

    const username = document.getElementById("username").value
    const senha = document.getElementById("senha").value

    const resposta = await fetch(
        "http://127.0.0.1:8000/usuarios/login",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                senha: senha
            })
        }
    )

    const dados = await resposta.json()

    if (resposta.status == 200) {

        localStorage.setItem(
            "token",
            dados.access_token
        )

        window.location.href = "dashboard.html"

    } else {

       const mensagem = document.getElementById("mensagem")

mensagem.style.color = "red"

mensagem.innerText = dados.detail
    }
}