function uploadProposal() {
  const fileInput = document.getElementById("proposal-file");
  const status = document.getElementById("proposal-status");
  if (fileInput.files.length > 0) {
    status.innerHTML = "✅ Proposal uploaded: " + fileInput.files[0].name;
    status.style.color = "green";
  } else {
    status.innerHTML = "❌ Please select a file first.";
    status.style.color = "red";
  }
}

function sendMessage() {
  const messageBox = document.getElementById("message-box");
  const chatLog = document.getElementById("chat-log");

  if (messageBox.value.trim() !== "") {
    const newMessage = document.createElement("p");
    newMessage.textContent = "You: " + messageBox.value;
    chatLog.appendChild(newMessage);
    messageBox.value = "";
  }
}
