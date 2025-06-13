document.addEventListener('DOMContentLoaded', () => {
  
  const roomName = JSON.parse(document.getElementById('room-name').textContent);

  // Crée la WebSocket vers le serveur
  const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
  );

  // Quand on reçoit un message du serveur
  chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const log = document.getElementById('chat-log');
    log.textContent += (data.author + ': ' + data.message + '\n');
  };

  // Envoi du message quand on clique sur le bouton
  document.querySelector('#chat-message-submit').onclick = function() {
    const inputField = document.querySelector('#chat-message-input');
    const message = inputField.value;
    chatSocket.send(JSON.stringify({ 'message': message }));
    inputField.value = '';
  };
});