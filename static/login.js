const email = document.getElementById("email");
const password = document.getElementById("password");

const btnLogin = document.getElementById("btnLogin");

const state = document.getElementById("state");

btnLogin.addEventListener("click", async () => {

    const user = {

    email: email.value,

    password: password.value
};

    try {
        const response = await fetch("/login", {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(user)

    });

        const data = await response.json();

        console.log(data);

        state.textContent = data.message;

        setTimeout(() => {

        console.log("Redirigiendo...");
        console.log(data.token)
        window.location.href = "/app";

    }, 3000);

        }

       catch(error){

        console.error(error);

        state.textContent = "Error al iniciar sesion.";


            } 
    

})



