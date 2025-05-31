async function summarizeText() {
  const text = document.getElementById("inputText").value.trim();

  if (!text) {
    alert("Please enter some text to summarize.");
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:8000/summarize", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text: text })
    });

    const data = await response.json();

    if (response.ok) {
      document.getElementById("result").innerText = data.summary;
    } else {
      document.getElementById("result").innerText = "Error: " + JSON.stringify(data);
    }
  } catch (error) {
    document.getElementById("result").innerText = "Error: " + error;
  }
}
