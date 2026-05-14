async function cadastrar() {

    const username =
        document.getElementById(
            "username"
        ).value

    const senha =
        document.getElementById(
            "senha"
        ).value

    const resposta = await fetch(

        "https://barbeariapro.onrender.com/usuarios/",

        {

            method: "POST",

            headers: {

                "Content-Type":
                "application/json"

            },

            body: JSON.stringify({

                username: username,

                senha: senha,

                role: "cliente"

            })

        }

    )

    const dados =
        await resposta.json()

    document.getElementById(
        "mensagem"
    ).innerText =
    dados.mensagem || dados.detail
}