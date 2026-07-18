const despensa = document.getElementById("despensa");
const btnDespensa = document.getElementById("btnDespensa");

const token = localStorage.getItem("token");

if (!token) {
    window.location.href = "/login"; 
}

btnDespensa.addEventListener("click", async () => {

    const res = await fetch("/despensa", { // Este fecth trae los datos de los productos que hay en la dispensa.
    headers: {
        Authorization: `Bearer ${token}`
    }
})
    
//     .then(async res => {

//     if (res.status === 401) {
//         localStorage.removeItem("token");
//         window.location.href = "/login";
//         return;
//     }

//     return res.json();
// });

    console.log("este es el token ", token);
    
    const data = await res.json();

    console.log(data)
    despensa.innerHTML = "";

    data.productos.forEach(producto => {

        const tarjeta = document.createElement("div");
        tarjeta.className = "producto-despensa";
        tarjeta.innerHTML = `

            <span>
                🛒 ${producto.nombre}
            </span>

            <strong>
                ${producto.precio}
            </strong>
        `;

        despensa.appendChild(tarjeta);

    });

});

// --------------------------------------------------------
const inputFactura = document.getElementById("factura");
const boton = document.getElementById("btnAnalizar");
const estado = document.getElementById("estado");

boton.addEventListener("click", async () => {

    if (inputFactura.files.length === 0) {

        alert("Selecciona una factura.");
        return;
    }

    const archivo = inputFactura.files[0];

    const formData = new FormData();

    formData.append("img", archivo); // dice img porque es asi como lo cree en el endpoint en el backend.

    estado.textContent = "Procesando factura...";

    try {
        const respuesta = await fetch("/facturas", {

            method: "POST",
            headers: {
                Authorization: `Bearer ${token}`
            },
            body: formData,
        });

        const datos = await respuesta.json(); // Creamos la salida en formato json

        console.log(respuesta.status);
        console.log(datos);
        
        // Creamos las constantes de cada dato que se mostrara por pantalla
        const resultado = document.getElementById("resultado");
        const empresa = document.getElementById("empresa");
        const fecha = document.getElementById("fecha");
        const total = document.getElementById("total");
        const productos = document.getElementById("productos");

        const factura = datos.resultado; // creamos una constante la cual es la contenedora de la respuesta

        // Agregamos los datos al DOM
        empresa.textContent = factura.empresa;
        fecha.textContent = factura.fecha;
        total.textContent = factura.total;

        productos.innerHTML = "";
        
        // Recorremos el array de todos los productos para luego mostrarlos
        factura.productos.forEach(producto => {

        const tarjeta = document.createElement("div");

        tarjeta.className = "producto";

        tarjeta.innerHTML = `

        <div class="producto-info">
            <div class="producto-nombre">
                🛒 ${producto.nombre}
            </div>
        </div>

        <div class="producto-precio">
            ${producto.precio}
        </div>
    `;

    productos.appendChild(tarjeta);

});
        // Mostramos el contenido
        resultado.style.display = "block";
        console.log(datos);
        estado.textContent = "✅ Factura procesada correctamente.";

    }

    catch (error) {
        console.error(error);
        estado.textContent = "❌ Error al procesar la factura.";
    }
    

});