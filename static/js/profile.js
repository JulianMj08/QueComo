const name = document.getElementById("name");
const email = document.getElementById("email");
const logout = document.getElementById("logout");


const token = localStorage.getItem("token");

document.addEventListener("DOMContentLoaded", async () => {

    if (!token) {
        window.location.href = "/login";
        return;
    }

    console.log("Enviando token...");
    console.log(token);

    const res = await fetch("/api/perfil", {
        headers: {
            Authorization: `Bearer ${token}`
        }
    });

    if (!res.ok) {

        localStorage.removeItem("token");

        window.location.href = "/login";

        return;
    }

    const data = await res.json();
    console.log(data);
    

    name.textContent = data.name;

    email.textContent = data.email;


});

logout.addEventListener("click", () => {

    localStorage.removeItem("token");

window.location.href = "/login";
})