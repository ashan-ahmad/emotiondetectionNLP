let RunSentimentAnalysis = () => {
  const textToAnalyze = document.getElementById("textToAnalyze").value;

  const xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("system_response").innerHTML = JSON.parse(
        xhttp.responseText
      ).output;
    } else if (this.readyState == 4) {
      document.getElementById("system_response").innerHTML = JSON.parse(
        xhttp.responseText
      ).output;
    }
  };
  xhttp.open("POST", "/emotion_detector", true);
  xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhttp.send("text=" + encodeURIComponent(textToAnalyze));
};
