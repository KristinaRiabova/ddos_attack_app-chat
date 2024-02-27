const socket = new WebSocket("ws://localhost:8000/ws/chat/");
let isUser1Typing = false;

function sendMessage(message, userId) {
    socket.send(
        JSON.stringify({
            message: message,
            user_id: userId,
        })
    );
}
function displayUserMessage(userId, message) {
    const userMessagesDiv = document.getElementById(
        `user${userId}-messages`
    );
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message");

    if (userId === 2) {
        showNotification(message);
    }

    if (message.includes("Sure! Here's the link")) {
        const linkElement = document.createElement("a");
        linkElement.setAttribute("href", "http://localhost:8000/registration");
        linkElement.style.color = "#34eb9e";
        linkElement.style.textDecoration = "underline";
        linkElement.textContent = "Sure! Here's the link";

        messageDiv.appendChild(linkElement);
    } else {
        messageDiv.textContent = message;
    }

    userMessagesDiv.appendChild(messageDiv);
    userMessagesDiv.scrollTop = userMessagesDiv.scrollHeight;
}

function showNotification(message) {
    const notificationBar = document.getElementById("notification-bar");
    notificationBar.textContent = `New message: ${message}`;
    notificationBar.style.display = "block";

    setTimeout(() => {
        notificationBar.style.display = "none";
    }, 3000);
}

socket.onmessage = function (event) {
    const data = JSON.parse(event.data);
    const userId = data["user_id"];
    const message = data["message"];
    displayUserMessage(userId, message);

    if (userId === 1) {
        handleAutoResponse(message);
    }
};

socket.onclose = function (event) {
    document.getElementById("exit-message").style.display = "block";
};

window.onload = function () {
    sendMessage("Hi there!", 1);
};

function handleAutoResponse(message) {
    let response = "";

    if (message.toLowerCase().includes("hello")) {
        response = "Hello! How can I help you?";
    } else if (message.toLowerCase().includes("how are you")) {
        response = "I'm fine, thank you!";
    } else if (message.toLowerCase().includes("duck")) {
        response = "Sure! Here's the link";
    } else {
        response = "Yeap, here's the link";
    }

    setTimeout(function () {
        sendMessage(response, 2);
    }, 1000);
}

document
    .getElementById("send-button")
    .addEventListener("click", function () {
        const messageInput = document.getElementById("message-input");
        const message = messageInput.value.trim();
        if (message !== "") {
            sendMessage(message, 1);
            messageInput.value = "";
        }
    });

document
    .getElementById("message-input")
    .addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            document.getElementById("send-button").click();
        }
    });