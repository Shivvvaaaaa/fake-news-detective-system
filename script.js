function checkNews() {
    let text = document.getElementById("newsInput").value;

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ news: text })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerHTML = data.result;
    });
}