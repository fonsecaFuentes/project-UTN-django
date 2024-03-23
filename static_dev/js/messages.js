document.addEventListener('DOMContentLoaded', function() {
    let messageContainer = document.getElementById('message-container');

    if (messageContainer) {
        // Mostrar el mensaje
        messageContainer.style.display = 'block';

        // Ocultar el mensaje después de 5 segundos
        setTimeout(function() {
            messageContainer.style.display = 'none';
        }, 5000);
    }
});


