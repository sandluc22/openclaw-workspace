<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = strip_tags(trim($_POST["nombre"]));
    $telefono = strip_tags(trim($_POST["telefono"]));
    $email = strip_tags(trim($_POST["email"]));
    $fecha_nacimiento = strip_tags(trim($_POST["fecha_nacimiento"]));
    $aseguradora_interes = strip_tags(trim($_POST["aseguradora_interes"]));
    $seguro = strip_tags(trim($_POST["seguro"]));

    $destinatario = "info@crecimientofinancieroglobal.com";
    $asunto = "Nuevo contacto desde CFG - $seguro";

    $cuerpo = "Nuevo formulario de contacto:\n\n";
    $cuerpo .= "Nombre: $nombre\n";
    $cuerpo .= "Teléfono: $telefono\n";
    $cuerpo .= "Email: $email\n";
    $cuerpo .= "Fecha de nacimiento: $fecha_nacimiento\n";
    $cuerpo .= "Aseguradora de interés: $aseguradora_interes\n";
    $cuerpo .= "Seguro solicitado: $seguro\n";

    $cabeceras = "From: no-reply@crecimientofinancieroglobal.com\r\n";
    $cabeceras .= "Reply-To: $email\r\n";
    $cabeceras .= "X-Mailer: PHP/" . phpversion();

    if (mail($destinatario, $asunto, $cuerpo, $cabeceras)) {
        header("Location: https://crecimientofinancieroglobal.com/?ok=1");
        exit;
    } else {
        header("Location: https://crecimientofinancieroglobal.com/?error=1");
        exit;
    }
} else {
    header("Location: https://crecimientofinancieroglobal.com/");
    exit;
}
