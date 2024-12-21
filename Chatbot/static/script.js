document.getElementById("uploadForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const file = document.getElementById("file").files[0];
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("/upload-pdf", { method: "POST", body: formData });
    const data = await response.json();

    const messageElement = document.getElementById("uploadMessage");
    messageElement.className = "message"; // Reset class
    if (response.ok) {
        messageElement.textContent = data.message;
        messageElement.classList.add("success");
    } else {
        messageElement.textContent = data.detail || "An unexpected error occurred.";
        messageElement.classList.add("error");
    }
});

async function askQuestion() {
    const question = document.getElementById("question").value.trim();
    if (!question) return;

    const chatBox = document.getElementById("chatBox");
    const userMessage = `<div class="user-message">You: ${question}</div>`;
    chatBox.insertAdjacentHTML("beforeend", userMessage);

    const loadingMessage = document.createElement("div");
    loadingMessage.className = "loading-message";
    loadingMessage.textContent = "Assistant is typing...";
    chatBox.appendChild(loadingMessage);

    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
    });

    chatBox.removeChild(loadingMessage);

    if (response.ok) {
        const data = await response.json();
        const assistantMessage = `<div class="assistant-message">Assistant: ${data.answer}</div>`;
        chatBox.insertAdjacentHTML("beforeend", assistantMessage);
    } else {
        const errorMessage = `<div class="error">Error: ${response.statusText}</div>`;
        chatBox.insertAdjacentHTML("beforeend", errorMessage);
    }

    document.getElementById("question").value = ""; // Clear input
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom
}