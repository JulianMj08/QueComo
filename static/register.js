const name = document.getElementById("name");
const email = document.getElementById("email");
const password = document.getElementById("password");

const btnRegister = document.getElementById("btnRegister");

const state = document.getElementById("state");

btnRegister.addEventListener("click", async () => {

    const user = {

    name: name.value,

    email: email.value,

    password: password.value

};

    try {
        const response = await fetch("/registro", {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(user)

    });

        const data = await response.json();

        console.log(data);

        state.textContent = data.message;

        }

        catch(error){

        console.error(error);

        state.textContent = "Error al crear el usuario.";


            }
});



