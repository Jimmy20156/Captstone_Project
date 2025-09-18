function submitEvaluation() {
  const content = parseInt(document.getElementById("content").value) || 0;
  const technical = parseInt(document.getElementById("technical").value) || 0;
  const presentation = parseInt(document.getElementById("presentation").value) || 0;
  const contribution = parseInt(document.getElementById("contribution").value) || 0;

  const total = content + technical + presentation + contribution;

  if (total > 0) {
    document.getElementById("evaluation-status").innerHTML =
      `✅ Evaluation submitted. Total Score: ${total}/100`;
    document.getElementById("evaluation-status").style.color = "green";

    // Add to scoring summary
    const history = document.getElementById("scoring-history");
    const li = document.createElement("li");
    li.textContent = `Score: ${total}/100 (Content: ${content}, Technical: ${technical}, Presentation: ${presentation}, Contribution: ${contribution})`;
    history.appendChild(li);
  } else {
    document.getElementById("evaluation-status").innerHTML =
      "⚠ Please input valid scores.";
    document.getElementById("evaluation-status").style.color = "red";
  }
}

function submitFeedback() {
  const feedback = document.getElementById("panel-feedback").value;
  const status = document.getElementById("feedback-status");

  if (feedback.trim()) {
    status.innerHTML = "✅ Feedback submitted successfully!";
    status.style.color = "green";
  } else {
    status.innerHTML = "⚠ Please enter feedback.";
    status.style.color = "red";
  }
}
