async function criarAgendamento() {

    const cliente = document.getElementById("cliente").value
    const horario = document.getElementById("horario").value
    const barbeiro = document.getElementById("barbeiro").value

    const token = localStorage.getItem("token")

    const resposta = await fetch(
        "http://127.0.0.1:8000/agendamentos/",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },

            body: JSON.stringify({
                cliente,
                horario,
                barbeiro
            })
        }
    )

    const dados = await resposta.json()

    alert(dados.mensagem || "Agendamento criado")

    listarAgendamentos()
}

async function listarAgendamentos() {

    const token = localStorage.getItem("token")

    const resposta = await fetch(
        "http://127.0.0.1:8000/agendamentos/",
        {
            headers: {
                "Authorization": `Bearer ${token}`
            }
        }
    )

  const dados = await resposta.json()

console.log(dados)

const lista = document.getElementById("lista")

    lista.innerHTML = ""

    dados.forEach(agendamento => {

       lista.innerHTML += `
    <div class="card">

        <h3>${agendamento.cliente}</h3>

        <p>${agendamento.horario}</p>

        <p>${agendamento.barbeiro}</p>

        <button onclick="deletarAgendamento(${agendamento.id})">
            Deletar
        </button>

    </div>
`
    })
}

listarAgendamentos()

async function deletarAgendamento(id) {

    const token = localStorage.getItem("token")

    await fetch(
        `http://127.0.0.1:8000/agendamentos/${id}`,
        {
            method: "DELETE",

            headers: {
                "Authorization": `Bearer ${token}`
            }
        }
    )

    listarAgendamentos()
}