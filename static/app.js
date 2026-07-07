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

    formData.append("imagen", archivo);

    estado.textContent = "Procesando factura...";

    try {

        const respuesta = await fetch("/facturas", {

            method: "POST",

            body: formData

        });

        const datos = await respuesta.json();

        console.log(datos);

        estado.textContent = "✅ Factura procesada correctamente.";

    }

    catch (error) {

        console.error(error);

        estado.textContent = "❌ Error al procesar la factura.";

    }
    

});